# 主規格書 (`spec.md`) 針對階段 2 之相關章節摘錄

### 第 1 章：全系列 NVIDIA 硬體自適應、熱控與 VRAM/RAM 協同調度

#### 1.1 跨世代 NVIDIA 顯示卡自適應引擎 (`UniversalNvidiaProfiler`)
系統啟動時透過 `torch.cuda.get_device_properties()` 與 `pynvml` 自動掃描本機所有 NVIDIA 顯示卡之 Compute Capability (CC)、顯存容量、PCIe 通道代數與散熱狀態，動態配置運算精度與載入策略：
* **GTX 16 / RTX 20 系列 (Turing CC 7.5，含開發基準 RTX 2080 Super 8GB VRAM)**：硬體不支援原生 `BF16`，系統於張量載入層強制攔截純 BF16 模型並自動轉型為 `FP16` 或 `GGUF (Q4_K_M / Q5_K_M)` 量化格式；自動啟用 `Attention Slicing` 與 `xFormers / SDPA`。
* **RTX 30 系列 (Ampere CC 8.6)**：自動解鎖原生 `BF16 (bfloat16)` 與 `TF32`，提升生圖數值穩定度並消除 FP16 溢位黑圖。
* **RTX 40 / 50 系列 (Ada CC 8.9 / Blackwell CC 10.0+)**：自動解鎖商城中之 `FP8 (e4m3fn)` 高速權重，實現算圖速度翻倍與顯存佔用減半。
* **容量分級與多卡分工**：
  * `LOW_VRAM (4GB~6GB)`：強制啟動 `--lowvram --cpu-vae` 逐層流式借用系統 RAM。
  * `MID_VRAM (8GB~12GB，如 RTX 2080S)`：啟動 `--medvram` 智慧組件分層借用系統 RAM。
  * `HIGH/ULTRA_VRAM (16GB~24GB+)`：啟動 `--highvram` 全顯存常駐模式，並支援雙卡路由（如 GPU #0 專責算圖/生影、GPU #1 常駐 LLM 與 TTS）。

#### 1.2 自訂模型庫根目錄與自動子目錄拓撲
於「系統設定」指定模型庫根目錄（如 `D:/OmniAgent_Models/`），資料庫僅儲存相對路徑，系統自動建立並維護以下標準目錄（支援 NTFS Hardlink / Symlink 免複製掛載外部既有 ComfyUI 模型庫）：
* `llm_agents/`（劇本/分鏡 GGUF 權重）
* `image_checkpoints/`（Flux / SDXL 主模型）
* `video_models/`（Wan2.1 / LTX-Video / AnimateDiff 權重）
* `loras/character/` 與 `loras/camera_motion/`（角色鎖定與運鏡微調權重）
* `controlnet_ipadapter/`（Depth / OpenPose / IP-Adapter FaceID 權重）
* `audio_tts/`（XTTS-v2 / CosyVoice / Wav2Lip / MuseTalk / RMBG-2.0 去背權重）
* `upscalers/`（Real-ESRGAN 超分與 RIFE 補幀模型）
* `fonts_and_luts/`（內嵌開源 CJK 字型檔與電影級 `.cube` 3D LUT 調色檔）
* `temp_downloads/`（斷點續傳暫存區，通過 SHA256 與 `safetensors` Header 完整性校驗後自動移入正式目錄）

#### 1.3 8GB VRAM 嚴格緩衝、Pinned Memory 加速與智慧熱保護 (`Pass 1 強化`)
* **鎖定 1.0GB VRAM 安全緩衝區 (`--reserve-vram 1.0`)**：嚴格防止顯存 100% 溢滿而觸發 Windows WDDM 驅動層級極慢的 Shared GPU Memory 強借卡死。
* **PCIe Pinned Memory (頁鎖定記憶體) 加速**：當向系統 RAM 借用空間時，強制於系統 RAM 分配 `pin_memory=True` 緩衝池，透過 DMA (Direct Memory Access) 將 CPU $\leftrightarrow$ GPU 權重搬移速度從 \~6 GB/s 提升至 **\~13.5 GB/s**。
* **按需上傳與即刻釋放 (JIT VRAM Lifecycle)**：模型僅在開始生圖/生影/推理瞬間上傳至 VRAM；切換任務或空間不足時，立即發送 `keep_alive: 0` (Ollama) 與 `/free` (ComfyUI) 並執行 `torch.cuda.empty_cache()` 與 `torch.cuda.ipc_collect()`。
* **NVML 智慧溫控與防降頻保護 (Thermal Throttling Guard)**：當長篇電影連續算圖數小時，GPU 核心溫度 $\ge 82^\circ\text{C}$ 時，調度器自動在兩個 Task 之間插入 `3~8 秒` 的冷卻休眠（Cooling Breather），防止顯卡過熱觸發硬體降頻或重開機。

---


### 第 2 章：全域介面架構：頂部三視圖、畫布 LOD 引擎與 NLE 交換標準

主視窗頂部常駐專案資訊列（包含多畫布分頁切換 `畫布 1 v`、累積消耗積分、專案名稱如 `一葦渡江`、即時 GPU VRAM/溫度儀表板），中央配置三大核心工作區切換標籤：

#### 2.1 `[ 🫧 畫布 (Canvas) ]`：無邊際點陣節點工作流畫布 (`Pass 3 強化`)
* **左側直立快捷工具列**：抓手平移 (`Space`)、節點清單檢視、新增節點 (`+`)、複製節點、畫布內容置中對齊 (`F`)。
* **左下角畫布工程控制列**：網格吸附對齊、小地圖導航 (`Minimap`)、一鍵樹狀自動排版 (`Auto-Layout`，採用 Sugiyama 階層圖演算法自動拉齊成對分鏡卡)、貝茲曲線連線顯示/隱藏、縮放比例控制 (`- 66% +`)。
* **三段式 LOD (Level of Detail) 與視角剔除渲染引擎**：為確保 90 分鐘電影（超過 1,000 個節點）在畫布縮放時維持 60 FPS 流暢度：
  * 縮放比例 $< 30\%$：僅繪製色塊標題與連線，卸載高解析縮圖紋理。
  * 縮放比例 $30\% \sim 70\%$：載入 `256px` 輕量快取縮圖。
  * 縮放比例 $> 70\%$：完整渲染高清預覽圖、懸浮工具列與視頻動態預覽。畫面外節點自動執行 `Frustum Culling` 不消耗繪圖資源。

#### 2.2 `[ 🎬 影片編輯 (Video Editor) ]`：非線性多軌時間軸剪輯台 (`Pass 4 強化`)
* **左側功能導航欄**：`智慧助理`、`媒體`、`畫布`、`文字 (標題字卡)`、`字幕`、`結束 (秒, 選填)`、`開始 (秒)` 精確時間碼裁剪器。
* **媒體櫃 (Media Bin)**：支援搜尋框、來源切換 (`畫布素材 v`)、**7 色圓點色彩標籤過濾（白、紅、橘、黃、綠、藍、紫）**、自動同步畫布已生成之圖片與帶時長標記 (`0:15`) 之視頻縮圖，底部設 `[ + 點擊或拖入檔案上傳 ]` 區域。
* **中上寬銀幕預覽器與 Proxy 代理流**：當時間軸超過 50 個片段時，背景自動生成 `480p ProRes/H.264 Proxy` 代理預覽流確保拖拉時間軸 0 延遲；正式點擊 **`[ 🖊️ 合成 ]`** 時自動切回原始高清母片渲染。
* **底部多軌時間軸與專業軟體匯出**：支援復原/重做 (`Undo/Redo Command Stack`)、游標分割 (`Split`)、刪除、磁吸對齊、音軌關鍵幀音量包絡線 (`Volume Envelope Keyframes`)、主軌鎖定 (`🔒`) 與隱藏 (`👁️`)。除了直接合成 `.mp4`，更支援匯出 **`OpenTimelineIO (.otio)`、`Final Cut Pro XML (.fcpxml)` 與 `DaVinci Resolve (.edl)`** 工程檔。

#### 2.3 `[ 🎞️ 成片 (Final Exports) ]`：成品庫與渲染佇列監控中心
* 右上角常駐 **`[ 渲染佇列中有 N 個任務 ]`** 狀態按鈕；中央展示歷次匯出成片卡片（含檔案大小、耗時、使用模型摘要），支援點擊 **`[ 🖊️ 再次編輯 ]`** 從現有草稿回溯修改。

---


### 第 11 章：任務佇列、GPU 調度與雲端非同步恢復
* **全面佇列化原則**：所有算圖任務一律進入 `Queue Manager` 依四級優先權（`HIGH`、`NORMAL`、`LOW`、`BACKGROUND`）排隊。
* **雲端非同步任務防重複扣款 (`Async Polling Recovery`)**：商用生影任務寫入 `remote_job_id`，斷網重連後優先憑單號向雲端取回已算完之成品，防止重複扣點。

---


### 第 22 章：專案標準目錄結構與核心程式碼函式庫架構

```text
OmniAgent_Studio/
 ├── main.py                              # 應用程式入口 (啟動 Pre-Flight 體檢、Watchdog 與 PySide6 主視窗)
 ├── config/
 │    ├── format_presets.py               # 六大影視體裁時間結構設定檔 (1分短片 ~ 90分電影)
 │    └── camera_lighting_dict.py         # 23種運鏡與12種布光之圖文及 Prompt 映射字典
 ├── database/
 │    ├── db_manager.py                   # SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
 │    ├── vector_index_engine.py          # sqlite-vec / HNSW 毫秒級資產向量檢索器
 │    └── project_archiver.py             # 專案版本快照與 .omni_pack 打包匯出/還原器
 ├── core/
 │    ├── gpu_auto_profiler.py            # 全系列 NVIDIA 顯卡偵測、NVML 溫控保護與 FP16/BF16/FP8 適配
 │    ├── vram_ram_hybrid_manager.py      # 1GB VRAM 緩衝、Pinned Memory DMA 加速與系統 RAM 組件卸載
 │    ├── comfy_graph_compiler.py         # ComfyUI 動態 AST 節點注入編譯器与 Custom Node 依賴自癒
 │    ├── model_store_crawler.py          # HF/Civitai 爬蟲、safetensors 標頭修復續傳與商用模型註冊表
 │    ├── model_menu_provider.py          # 雙分區商城對接畫布下拉選單與 Strict Local-First 路由
 │    ├── workflow_runtime.py             # DAG 循環檢測、Dirty Propagation 與雙模式 Gate 狀態機
 │    ├── task_queue_dispatcher.py        # 4級優先權 GPU 調度器、Token Bucket 限流與 remote_job_id 恢復
 │    ├── frame_continuity_engine.py      # 智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背
 │    └── master_video_assembler.py       # 音素級指定臉孔對嘴、J/L-Cut 混音、CJK 字卡、M&E 軌與 OTIO 匯出
 ├── providers/                           # 第16章 Decoupled Provider 抽象層
 │    ├── base_provider.py                # BaseLLM / BaseImage / BaseVideo / BaseTTS 抽象介面
 │    ├── local_providers.py              # Ollama (GBNF 約束) / ComfyUI / XTTS / CosyVoice 本地實作
 │    └── commercial_providers.py         # Seedream / Seedance / Veo 3.1 / GPT Image / Wan 雲端實作
 ├── agents/
 │    ├── multi_agent_graph.py            # 6大智能體協同管線、Pydantic 強型別驗證與時長裁決邏輯
 │    └── story_bible_memory.py           # Agent 長期記憶檢索、角色關係圖與跨集狀態防穿幫注入
 └── ui/
      ├── main_window.py                  # 頂部三視圖切換 (畫布 / 影片編輯 / 成片) 與硬體遙測狀態列
      ├── canvas/
      │    ├── infinite_dot_canvas.py     # 無邊際點陣畫布、3段式 LOD 視角剔除、小地圖與自動排版
      │    ├── asset_container_node.py    # 角色(藍)/場景(綠)/道具(黃) 資產容器與 PC 拖放沙盒上傳
      │    └── shot_pair_node_widget.py   # 左圖右影成對分鏡卡、白名單縮圖列、運鏡/布光/參數懸浮框
      ├── editor/
      │    └── nle_timeline_editor.py     # 7色標籤媒體櫃、480p Proxy 預覽器、音量包絡線與多軌時間軸
      └── dialogs/
           ├── model_store_dialog.py      # 雙分區模型商城 QTableView 介面
           └── settings_budget_dialog.py  # 模型庫根目錄設定、API 金鑰驗證與三層級預算上限面板
```
