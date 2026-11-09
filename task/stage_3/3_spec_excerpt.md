# 主規格書 (`spec.md`) 針對階段 3 之相關章節摘錄

### 第 1 章：全系列 NVIDIA 硬體自適應、熱控與 VRAM/RAM 協同調度

#### 1.1 跨世代 NVIDIA 顯示卡自適應引擎 (`UniversalNvidiaProfiler`)
系統啟動時透過 `torch.cuda.get_device_properties()` 與 `pynvml` 自動掃描本機所有 NVIDIA 顯示卡之 Compute Capability (CC)、顯存容量、PCIe 通道代數與散熱狀態，動態配置運算精度與載入策略：
* **GTX 16 / RTX 20 系列 (Turing CC 7.5，含開發基準 RTX 2080 Super 8GB VRAM)**：硬體不支援原生 `BF16`，系統於張量載入層強制攔截純 BF16 模型並自動轉型為 `FP16` 或 `GGUF (Q4_K_M / Q5_K_M)` 量化格式；自動啟用 `Attention Slicing` 與 `xFormers / SDPA`。
* **RTX 30 系列 (Ampere CC 8.6)**：自動解鎖原生 `BF16 (bfloat16)` 與 `TF32`，提升生圖數值穩定度並消除 FP16 溢位黑圖。
* **RTX 40 / 50 系列 (Ada CC 8.9 / Blackwell CC 10.0+)**：自動解鎖商城中之 `FP8 (e4m3fn)` 高速權重，實現算圖速度翻倍與顯存佔用減半。
* **容量分級與多卡分工**：
  * `LOW_VRAM (4GB~6GB)`：強制啟動 `--lowvram --cpu-vae` 逐層流式借用系統 RAM。
  * `MID_VRAM (8GB~12GB，如 RTX 2080S)`：啟動 `--medvram
...(章節截斷)...

### 第 3 章：雙分區模型商城、動態選單驅動與破損自癒機制

「模型商城」為全系統所有生成下拉選單的**唯一真實數據源 (Single Source of Truth)**，採用傳統清單表格 (`QTableView`) 分為兩大專區：

#### 3.1 分區 A：網路爬蟲免費開源模型庫 (`FREE_LOCAL`)
* 背景 `QThread` 定時透過 Hugging Face Hub API 與 Civitai v1 API（支援配置國內/區域高速鏡像站如 `hf-mirror.com`）爬取最新模型與版本，自動過濾不支援之純 BF16 格式，並依本機顯卡標註相容燈號（`🟢 純VRAM極速` / `🟡 需借用系統RAM` / `🔴 記憶體不足`）。
* **破損權重自動檢測與分塊自癒 (`Pass 7 強化`)**：支援 HTTP Range 斷點續傳與內嵌 `QProgressBar`；下載完成後自動解析 `.safetensors` JSON Header 與 SHA256，若發現檔案截斷損毀，自動針對損毀區塊重新拉取，並透過 `Custom Node Dependency Resolver` 自動補齊缺失之 ComfyUI 節點。
* 僅當模型 `is_downloaded = 1` 且啟用時，自動注入畫布對應類別之生成選單。

#### 3.2 分區 B：主流商用雲端 API 模型庫 (`COMMERCIAL_API`)
* 內建並同步主流商用模型清單與預估扣點/成本徽章：
  * **生圖商用模型**：`Seedream 5.0 Pro`（支援最多 10 張參考圖的 1K/2K 圖片生成與編輯，`🪙 20`）、`Nano Banana 2` (`🪙 18`)、`GPT Image 2` (`🪙 15`)、`GPT Image 2.5 Flare` (`🪙 15`)、`GPT Image 2.5 Sunburst` (`🪙 15`)、`Grok Imagine 圖片` (`🪙 6`)、`Qwen Image 3.0` (`🪙 7`)。
  * **生影商用模型**：`Grok Imagine 1.5 預覽` (`🪙 19`)、`Grok Imagine 視頻` (`🪙 14`)、`Seedance 2.0 Mini`（多模態視頻生成，成本優先，`🪙 147`）、`Veo 3.1` (`🪙 365`)、`Veo 3.1 Fast` (`🪙 93`)、`Veo 3.1 Reference` (`🪙 93`)、`Wan 2.7 視頻` (`🪙 115`)。
* **金鑰強制驗證與本地敏感詞預檢 (`Pass 9 強化`)**：商用模型必須於設定頁輸入 API Key（存於系統 `keyring`）並通過 Ping 驗證 (`key_status = 'VERIFIED'`) 方可解鎖顯示於選單中。發送雲端 API 前，先經本地輕量審核器預檢 Prompt 與圖片是否觸犯雲端 NSFW 規則，避免遭雲端攔截卻被扣除 API 費用。

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
