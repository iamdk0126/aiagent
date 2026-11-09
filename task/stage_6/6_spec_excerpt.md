# 主規格書 (`spec.md`) 針對階段 6 之相關章節摘錄

## 官方綜合技術與架構規格書 (Master Technical & Architectural Specification v5.0 — Production-Frozen Edition)


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


### 第 6 章：創作者人性化體驗：8 大殺手級 UX 增強功能

為提供直覺流暢的創作體驗，平台在 UI/UX 層深度實作了以下 8 大專屬功能：

1. **塗鴉與火柴人構圖引導 (Sketch-to-Scene Canvas)**：左卡旁內建極簡 30 秒手繪畫板，滑鼠手繪色塊或火柴人骨架自動轉為 ControlNet 構圖約束，一秒解決角色站位與鏡頭視角焦慮。
2. **風格吸管工具 (Style Eyedropper)**：上傳任意電影截圖，本地 Vision LLM 自動反推色溫、膠片顆粒與光影角度轉寫成專業 Prompt，並提取色彩查找表 (3D LUT) 套用到整場。
3. **智慧 `@` 標籤與膠囊積木 (Smart `@Tag` Autocomplete & Pills)**：在 Prompt 編輯框輸入 `@` 即彈出帶縮圖的選單，選中後自動轉為膠囊標籤，滑鼠懸停預覽或點擊直接切換角色差分（如戰損版）。
4. **10秒動態毛片預覽 (Animatic Preview)**：正式算圖前一鍵透過靜態圖與 TTS 快速合成有聲音字幕的毛片預覽，10 秒內確認全劇節奏，省下 80% 盲抽時間。
5. **4秒四連抽草稿 (4-Grid Fast Draft)**：結合极速 LoRA 瞬間產出四宮格低解析草稿供一眼挑選，點擊「放大精煉」才算高清首幀。
6. **麥克風語氣示範 (Voice Acting Guide)**：按住麥克風示範對白語氣，透過語音轉語音克隆（Speech-to-Speech）保留真人抑揚頓挫與情緒，完美套用到角色聲線。
7. **平行劇情分支 (Story Branching)**：在任意分鏡右鍵一鍵建立平行劇情樹狀分支，讓創作者無痛實驗不同結局。
8. **掛機睡眠模式與手機推播 (Overnight Batch & Push)**：設定排程在全部算完後自動休眠關機，並透過 Webhook 發送 LINE/Telegram 進度推播通知。

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
 │    └── master_video_assembler.py       # 音素級指定臉
...(章節截斷)...
