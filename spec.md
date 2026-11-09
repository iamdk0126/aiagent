# OmniAgent Studio — 地端與混合式全自動影音智能體創作平台

## 官方綜合技術與架構規格書 (Master Technical & Architectural Specification v5.1 — Production-Frozen Edition)

---

### ⚠️ 第 0 章：核心工程開發準則與注意事項 (Core Engineering Guidelines & Development Mandates)
> **【團隊最高開發鐵則】**：所有參與本專案之架構師、前後端工程師與 AI 協作開發者，在撰寫任何一行程式碼前，必須無條件遵守以下 10 大工程準則。違反任一準則之程式碼禁止合併入主分支 (Main Branch)。

#### 準則 1：單一職責與程式碼檔案規模限制 (Modularization & Anti-God-Object Rule)
* **嚴禁巨型單一檔案 (No Monolithic Files)**：嚴格禁止將多種不同特性的邏輯塞入同一個 `.py` 檔案中。**單一 Python 檔案原則上不得超過 `400 ~ 500` 行，單一函式 (Function/Method) 不得超過 `60` 行**。一旦超過，必須立即依職責拆分為獨立的子模組 (Sub-module) 或輔助類別 (Helper Class)。
* **嚴格四層架構隔離 (Strict 4-Tier Separation)**：
  1. **UI 視圖層 (`ui/`)**：僅負責 PySide6 畫面渲染、動畫與使用者事件捕捉，**絕對禁止在 `ui/` 檔案中撰寫任何 SQL 語句、FFmpeg 指令或 AI 模型推理邏輯**。
  2. **業務與調度核心層 (`core/` & `agents/`)**：負責工作流狀態機、VRAM 計算、尾幀篩選與 Agent 協同邏輯，不直接依賴具體外部工具。
  3. **供應商抽象與驅動層 (`providers/`)**：專門封裝 Ollama、ComfyUI、FFmpeg 子行程與各家雲端 API 的通訊細節。
  4. **資料持久化層 (`database/`)**：唯一允許執行 SQLite 讀寫、向量檢索與檔案沙盒複製的層級。

#### 準則 2：UI 主執行緒零阻塞鐵則 (Zero-Blocking Main Thread Policy)
* **禁止同步耗時操作**：PySide6 的主執行緒 (GUI Event Loop) 必須永遠維持 **60 FPS** 的極致流暢度。任何超過 `30ms` 的操作（包含：網路爬蟲、API 請求、模型下載、SHA256 校驗、FFmpeg 抽幀、OpenCV 色彩校正、大量圖片縮圖載入），**100% 必須封裝於 `QThread`、`QRunnable (QThreadPool)` 或非同步 Worker 中執行**。
* **信號槽通訊 (`Signal / Slot`)**：背景執行緒嚴禁直接操作任何 UI 元件（會導致 Qt 記憶體崩潰閃退），一律透過自定義 `Signal(dict)` 將進度或結果傳回主執行緒更新畫面。

#### 準則 3：VRAM 與系統記憶體生命週期防護 (Strict VRAM & Memory Hygiene)
* **用畢即釋放與顯存防漏**：針對 RTX 2080S (8GB VRAM) 基準，任何載入 PyTorch / CUDA 張量的函式，在離開作用域或發生 Exception 時，必須透過 `try...finally` 區塊確保張量解除引用 (`del tensor`)、呼叫 `gc.collect()` 並執行 `torch.cuda.empty_cache()`。
* **禁止常駐霸佔**：LLM、生圖、生影、去背、TTS 等模型嚴禁同時常駐於 8GB 顯存中；所有算圖任務啟動前必須先經過 `HybridMemoryOffloadEngine.prepare_vram_for_task()` 進行顯存清算與組件卸載。

#### 準則 4：資料庫單一寫入佇列與防鎖死規範 (SQLite Thread-Safety & Anti-Lock Mandate)
* **嚴禁裸寫 `sqlite3.connect()`**：全專案禁止在各模組私自呼叫 `sqlite3.connect()`。所有資料庫存取必須統一透過 `database/db_manager.py` 提供的 Thread-Safe Context Manager 進行。
* **讀寫分離與參數化查詢**：讀取操作可多執行緒併行（依賴 `WAL` 模式），但所有寫入操作 (`INSERT / UPDATE / DELETE`) 必須經過單一寫入鎖 (`threading.RLock` 或專用 Write Queue) 排隊執行，且**全面強制使用 `?` 參數化查詢**（嚴禁使用 f-string 拼接 SQL，防止因劇本台詞含有單引號 `'` 或特殊字元導致語法崩潰）。

#### 準則 5：強型別標註與結構化資料驗證 (Strict Type Hinting & Pydantic Validation)
* **全面 Type Hints**：所有函式簽章（參數與回傳值）必須 100% 加上 Python `typing` 型別標註。
* **跨層傳遞禁用裸字典 (No Raw Dicts Across Boundaries)**：模組與模組之間、以及 Multi-Agent 輸出的 JSON 資料，一律使用 `Pydantic BaseModel` 或 `@dataclass` 定義資料契約（Data Contract），在進入下一階段前完成欄位型別與預設值驗證。

#### 準則 6：地端優先與雲端扣點熔斷防呆 (Local-First & Cost Circuit-Breaker)
* **雲端呼叫三道鎖**：任何準備發往商用雲端 API (`COMMERCIAL_API`) 的請求，在發送前必須依序通過：
  1. `KeyStatus == VERIFIED` 檢查；
  2. `BudgetGuard` 檢查當前消耗是否超過單鏡/單集/專案預算上限；
  3. 記錄 `remote_job_id` 防重複發送。
* 只要任一條件不滿足或網路超時，**必須無條件、靜默且自動 Fallback 切換至本地免費模型 (`FREE_LOCAL`)**，絕不可因雲端錯誤而中斷使用者的創作流程。

#### 準則 7：跨平台相對路徑與專案沙盒隔離 (Pathlib & Sandboxed Asset Isolation)
* **全面採用 `pathlib.Path`**：程式碼中嚴禁使用字串拼接路徑（如 `folder + "\\" + file`），一律使用 `pathlib.Path` 處理路徑。
* **資料庫僅存相對路徑**：SQLite 資料庫內所有檔案路徑欄位，一律儲存「相對於模型庫根目錄」或「相對於專案沙盒目錄 (`projects/{id}/`)」的相對路徑，確保使用者更換硬碟代號（如 `C:` 移至 `D:`）或匯出 `.omni_pack` 給其他團隊成員時 100% 免修改即可讀取。

#### 準則 8：外部子行程安全管控與防殭屍行程 (Subprocess Safety & Zombie Prevention)
* **隱藏黑框與串流日誌**：呼叫 `FFmpeg`、`Ollama` 或 `ComfyUI` 子行程時，在 Windows 環境下必須加上 `creationflags=subprocess.CREATE_NO_WINDOW` 避免彈出黑色命令提示字元視窗干擾使用者。
* **資源回收**：所有子行程必須註冊於全域 `ProcessWatchdog` 中，當主程式關閉或任務取消 (`CANCELLED`) 時，確保強制終止子行程樹 (`psutil.Process.children()`)，嚴禁留下背景殭屍行程繼續偷吃 GPU 資源。

#### 準則 9：錯誤可恢復性與使用者友善異常處理 (Graceful Degradation & Actionable Errors)
* **嚴禁裸奔 `except Exception: pass`**：捕捉異常時必須使用結構化 Logger 記錄完整 Stack Trace 至 `logs/omni_runtime.jsonl`。
* **錯誤訊息白話化**：呈現給 UI 的錯誤提示必須具備「可操作性（Actionable）」——例如不可只顯示 `CUDA Error 2`，必須轉譯為：`「顯存空間不足：已自動為您切換為系統記憶體分層借用模式 (--medvram) 並重試中」`。

#### 準則 10：可測試性與無頭乾跑支援 (Testability & Headless Dry-Run Support)
* 所有核心業務類別（如工作流引擎、分鏡拆解、預算計算、FFmpeg 命令生成器）必須支援注入 `MockProvider`（無需真正消耗 GPU 算力或雲端點數，即可在 5 秒內跑完一部 60 分鐘連續劇的假圖/假音訊完整流程測試），確保單元測試與 CI/CD 自動化驗證可隨時執行。

---

### 📋 執行摘要與系統定位 (System Vision & Positioning)

**OmniAgent Studio** 是一套專為影視創作者、獨立動畫工作室與長篇劇集製作打造的 **「地端與混合式全自動影音智能體作業系統 (Local AI Movie Production Operating System)」**。

* **核心定位**：結合「無邊際點陣節點畫布」、「多智能體協同 (Multi-Agent)」、「非線性時間軸剪輯 (NLE)」與「多平台自動化發布」的全棧式桌面端影視生產平台。

* **技術棧基準**：採用 `Python 3.10+`、`PySide6 (Qt6 + OpenGL Viewport)` 原生桌面 GUI、本地 `SQLite (WAL 高併發模式 + sqlite-vec 向量擴充)` 資料庫，並透過抽象層整合 `Ollama`、`ComfyUI API`、`LiteLLM` 與 `FFmpeg 6.1+`。

* **地端優先鐵則 (`Strict Local-First`)**：系統預設在離線與零雲端費用的環境下 100% 獨立運作；商用雲端 API 僅作為有驗證金鑰且在預算上限內的可選加速通道。

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

### 第 4 章：素材資料庫（資產容器）、PC 上傳與嚴格白名單控制

畫布左側設立分類資產容器：**「👤 角色資產 (藍框)」**、**「🏞️ 場景資產 (綠框)」**、**「📦 道具資產 (黃框)」** 及 **「🗣️ 音源資產」**：

1. **雙管道入庫與沙盒化歸檔**：

   * **平台內生成自動納管**：由劇本與分鏡自動提煉繪圖 Prompt 填入素材編輯框，使用者可確認、重複修改文字並重新生成圖片（保留 `V1, V2...` 完整歷史版本）；確認後自動寫入 `project_assets` 表並掛載至畫布容器。

   * **多視角角色設定圖與羽化去背 (`Pass 5 強化`)**：內建 `Front / Back / Side` 全身角色設定圖模板，整合本地去背模型 (`RMBG-2.0 / BiRefNet`) 自動轉為透明通道 PNG (RGBA)，並執行 `1.5px Alpha Matte Edge Feathering (邊緣消鋸齒與去白邊)`。

   * **PC 端上傳與沙盒複製**：支援從電腦拖放上傳圖片或音檔，入庫瞬間自動複製至專案沙盒目錄 `projects/{project_id}/assets/`，杜絕外部檔案移動導致之媒體遺失。

2. **素材命名與特徵說明雙向綁定**：

   * 支援自訂素材名稱（如：`女孩母親`、`船夫`、`南朝長江渡口`、`木製念珠`、`草鞋`、`一根枯黃蘆葦`）與詳細文字說明；Agent 撰寫分鏡 Prompt 時自動引用該說明。

3. **嚴格指定素材白名單、深度融合與多人分區防混臉 (`Pass 5 強化`)**：

   * 分鏡懸浮編輯框頂部設有「指定素材參考縮圖列」（可點擊 `+` 新增或 `×` 移除，如 `E1S02` 同時鎖定 `[達摩]`、`[南朝長江渡口]`、`[木製念珠]`、`[木船]`、`[草鞋]`）。

   * **硬性隔離與 Z-Depth 深度融合**：算圖引擎嚴格限制僅能讀取縮圖列白名單中之素材。當把角色或道具合成進指定場景時，自動提取場景之 `Depth Anything V2` 深度圖與環境光色溫，確保人物雙腳精準踩在地面透視上且受環境光染色，絕無生硬貼紙感。當單一鏡頭同時綁定 $\ge 2$ 位角色時，自動啟動 `Regional IP-Adapter / Attention Masking` 分區遮罩，防止不同角色臉部或服裝特徵混淆。

### 第 5 章：成對分鏡節點、智慧尾幀連續與運鏡/布光控制系統

畫布中每個分鏡以 `E{集數}S{鏡號}`（如 `E1S01`, `E1S02`）成對排列為「左卡：生圖節點」與「右卡：生影節點」，並以紫色貝茲曲線串聯：

#### 5.1 左卡（生圖）與右卡（生影）懸浮編輯器與微工具列

* **左卡結構化 Prompt**：自動依劇本生成並可重複修改 `Style:`（美學風格、色調、光影）與 `Scene:`（場景、人物互動、**`Gaze_Direction` 180度軸線視線方向標籤**）。

* **右卡結構化 Prompt**：自動生成並可修改 `Action:`（動態描述）、`Camera_Motion:`（運鏡指令）與 `Ambiance_Audio:`（環境音效描述）。

* **懸浮微工具列與獨立重試**：輸入框具備 `5000` 字數統計、全螢幕展開與 **`[ ✨ 魔法棒 Prompt 智慧擴寫 ]`**；節點上方工具列提供**字幕生成、首/尾幀檢視、局部塗抹重繪 (Inpainting)、水平翻轉 (`⇄` 修正視線越軸)、音軌配音、HD 超分放大、前後廢幀裁剪 (`✂️`)、加入素材庫與本地下載**。左右卡狀態獨立記錄，右卡若顯示「失敗」可單獨重跑。

#### 5.2 智慧尾幀篩選、時域去閃爍與跨段無縫連續管線 (`Pass 5 強化`)

* **智慧最佳尾幀挑選（防動態模糊與閉眼）**：上一段視頻（如 `E1S01` 右卡）算圖完成時，系統自動掃描結尾最後 `0.5 秒（約 12 影格）`，透過 OpenCV 計算 **Laplacian 清晰度分數** 與 **臉部特徵完整度**，自動挑選出最清晰無崩壞的一幀存為 `E1S01_last_frame.png`，並自動修剪掉其後的模糊廢幀。

* **跨鏡直方圖色彩校正與時域去閃爍 (`Histogram Matching & Temporal Deflicker`)**：以該場戲 (`Scene`) 第一張基準圖為色彩錨點，對抽出的尾幀執行 LAB 色彩空間均值對齊，並在合成時套用滑動視窗亮度平滑濾鏡，徹底消除跨 10 段以上連續生成時的色溫偏移、過曝或畫面閃爍。

* **雙模式傳遞接續**：

  1. **直接首幀接續 (`[首]` 模式)**：將上一段最佳尾幀鎖定為下一段視頻之首幀（縮圖標示 **`[首]`**），實現一鏡到底動作接續。

  2. **跨鏡構圖光影參考 (`[E1S01]` 模式)**：將 `E1S01` 尾幀自動掛載至 `E1S02` 左卡參考列最後一格，結合新登場素材生成光影連貫的新角度畫面。

#### 5.3 生圖與生影細部參數彈窗

* **生圖參數**：`布光`、`質量`（`高` / `標準`）、`畫幅比例`（`21:9`、`16:9`、`9:16` 等）、`NSFW 檢查`（摘要顯示如 `21:9 · 高 · 開啟 v`）。

* **生影參數**：`模式`（`首幀` / `首尾幀` / `參考圖`）、`布光`、`分辨率`（`720p` / `1080p`）、`畫幅比例`（`21:9` 等）、`時長`（`[-]` `15s` `[+]`）、`動態強度 (Motion Strength)`、`Seed 鎖定`，以及 `生成音頻`、`聯網搜索`、`NSFW 檢查` 開關（摘要顯示如 `首幀 · 21:9 · 720p · 15s v`）。

#### 5.4 視覺化「運鏡 (`📹 運鏡 v`)」完整字典庫 (共 23 項細分動作)

`1. 跟隨拍攝`、`2. 盤旋下降`、`3. 盤旋抬升`、`4. 鏡頭前推`、`5. 鏡頭後移`、`6. 環繞拍攝`、`7. 第一視角`、`8. 無人機`、`9. 固定鏡頭`、`10. 鏡頭上搖`、`11. 鏡頭下搖`、`12. 鏡頭左搖`、`13. 鏡頭右搖`、`14. 鏡頭上升`、`15. 鏡頭下降`、`16. 鏡頭左移`、`17. 鏡頭右移`、`18. 變焦推進`、`19. 變焦拉遠`、`20. 柯克變焦`、`21. 滾筒旋轉`、`22. 高空航拍`、`23. 手持拍攝`。

#### 5.5 視覺化「布光」完整字典庫 (共 12 項)

`1. 無`、`2. 低調 / 戲劇光`、`3. 黃金時刻`、`4. 自然光`、`5. 霓虹`、`6. 輪廓光`、`7. 高調 / 明亮`、`8. 藍調時刻`、`9. 暖色鎢絲燈`、`10. 剪影 / 逆光`、`11. 體積光 / 丁達爾`、`12. 陰天柔光`。

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

### 第 7 章：半自動與全自動雙模式 Multi-Agent 協同管線 (`Pass 2 強化`)

系統內建 6 大智能體（**總導演 Director**、**編劇 Scriptwriter**、**美術資產設計 Asset Designer**、**分鏡映射 Storyboard Mapper**、**QA 品質審查員**、**連戲設定集管理員 Archivist**）：

* **GBNF / Pydantic 強制結構化輸出鎖定**：底層透過 Ollama `format: json_schema` 在 Token 取樣階段強制約束輸出結構，確保分鏡拆解與素材提取 100% 符合欄位規範。

* **半自動模式 (`SEMI_AUTO`)**：於 5 大查核點（`Gate 1` \~ `Gate 5`）自動暫停，由使用者審核核准、手動修改或退回重寫。

* **全自動模式 (`FULL_AUTO`)**：零人工干預直出成片，遇瑕疵由 QA 採指數退避策略自動重試（單鏡雲端重試上限 2 次，超過自動降級回本地免費模型）。

### 第 8 章：多體裁動態分段架構與廣播級終極合成引擎

* **六大市場主流體裁預設**：支援 `SHORT_1MIN` (1分短片)、`SHORT_3MIN` (3分微短劇)、`MINI_SERIES_10MIN` (10分小短劇)、`TV_DRAMA_60MIN` (60分電視劇) 與 `FEATURE_FILM_90MIN` (90分以上電影)。

* **音素級多語系指定角色對嘴 (`Phoneme-Aligned Target Speaker LipSync`)**：透過 `WhisperX` 與 `CosyVoice` 零樣本 3 秒情緒語音克隆，依 `speaker_asset_id` 臉部向量鎖定發話角色執行對嘴。

* **場次級連續環境音與 J/L-Cut 混音**：同場戲 (`Scene`) 共享連續底噪軌 (`Ambiance Stem`)，切鏡處套用 `150ms Audio Crossfade` 消除聲音斷崖。

* **东亞 CJK 專業字幕與字卡引擎**：內建思源黑體、宋體與古典書法，支援直排/橫排、描邊陰影、中文避頭尾換行與滾動演職員表。

* **三軌分離、M&E 國際軌與 -14 LUFS 標準化**：分離為對白軌 (A1)、環境音軌 (A2) 與配樂軌 (A3，人聲出現時自動 Sidechain 閃避 -12dB)，由 FFmpeg 輸出主成片 `.mp4`、純音樂音效國際軌 (`_ME_Track.wav`) 與 `.srt / .ass` 字幕。

### 第 9 章：工作流執行引擎 (Workflow Runtime Engine)

* **設計目標**：畫布節點兼具資料流與實際任務調度能力，支援暫停、恢復、失敗重試、斷電續跑、Gate 攔截、DAG 循環死鎖檢測 (`Tarjan Cycle Detection`) 與上游變更髒資料傳播 (`Dirty Propagation`)。

* **狀態機定義**：

  * **Workflow 狀態 (6 態)**：`WAITING`、`RUNNING`、`PAUSED`、`FAILED`、`COMPLETED`、`CANCELLED`。

  * **Node 狀態 (8 態)**：`PENDING`、`READY`、`RUNNING`、`SUCCESS`、`FAILED`、`SKIPPED`、`BLOCKED`、`OUTDATED`。

### 第 10 章：畫布節點系統標準化 (Canvas Runtime Framework)

* **12 大標準節點類型 (`Node Definition`)**：

  * **業務節點 (7 類)**：`PROJECT`、`SCRIPT`、`ASSET`、`IMAGE`、`VIDEO`、`TTS`、`QA`。

  * **邏輯與控制節點 (5 類)**：`IF`、`LOOP`、`WAIT`、`MERGE`、`PUBLISH`。

### 第 11 章：任務佇列、GPU 調度與雲端非同步恢復

* **全面佇列化原則**：所有算圖任務一律進入 `Queue Manager` 依四級優先權（`HIGH`、`NORMAL`、`LOW`、`BACKGROUND`）排隊。

* **雲端非同步任務防重複扣款 (`Async Polling Recovery`)**：商用生影任務寫入 `remote_job_id`，斷網重連後優先憑單號向雲端取回已算完之成品，防止重複扣點。

### 第 12 章：專案版本控制與沙盒封裝匯出 (Project Version Control)

* 支援建立專案快照 (`Project_v1`, `Project_v2`) 與分支，記錄於 `project_versions` 表；支援一鍵打包匯出 `.omni_pack` 專案歸檔包與廢檔自動垃圾回收 (`Disk Pruner`)。

### 第 13 章：Agent 長期記憶系統 (Agent Long-Term Memory)

* 長篇劇集製作中自動檢索並注入 `agent_memories` 表中的全域創作鐵則，確保 Agent 絕對不會忘記核心設定。

### 第 14 章：Story Bible 強化架構：關係圖譜與狀態追蹤

* 透過 `character_relationships` 結構化儲存網狀人物關係，並藉由 `character_states` 按集數場次追蹤角色生理與服裝動態變化，徹底杜絕長篇連戲穿幫。

### 第 15 章：素材向量索引與毫秒級語意搜尋 (`Pass 8 強化`)

* 素材入庫時自動提取 `CLIP`、`SigLIP`、`DINOv2` 或 `InsightFace` 視覺特徵向量存入 `asset_embeddings` 表，並建立 `HNSW / Flat` 記憶體映射索引實現毫秒級餘弦相似度檢索。

### 第 16 章：Plugin Provider 抽象層與 ComfyUI 動態編譯器

* 核心引擎透過 `BaseLLMProvider`、`BaseImageProvider`、`BaseVideoProvider` 與 `BaseTTSProvider` 介面解耦。內建 **`ComfyUI Dynamic AST Graph Compiler`**，自動根據白名單動態增刪 AST 中的 IP-Adapter 與 ControlNet 節點。

### 第 17 章：預算管理與成本控制中心 (Budget & Cost Guard)

* 透過 `budget_rules` 表管控單鏡、單集與單專案總預算上限。觸及上限時 API 閘道器自動熔斷，100% 強制無縫切換回 `FREE_LOCAL` 地端免費模型。

### 第 18 章：多平台發布中心與 C2PA 合規標記

* 支援一鍵轉碼發布至 YouTube、TikTok、IG Reels、FB Video、Bilibili 與小紅書；匯出成片時選擇性寫入符合國際規範之 `C2PA Content Credentials` 溯源中繼資料。

### 第 19 章：Gate Checkpoint、自動 Migration 與災難恢復

* 完成 Gate1 \~ Gate5 時自動寫入持久化狀態快照至 `workflow_checkpoints` 表，支援崩潰後無縫接續；啟動時透過 `PRAGMA user_version` 自動執行無損 Schema Migration 並滾動備份最近 5 次之 `.db.bak`。

### 第 20 章：企業版與團隊協作預留架構

* 預留 `users`、`roles`、`permissions` 三張權限管理表，為未來升級至團隊或雲端協作奠定基礎。

### 第 21 章：v5.1 凍結後完整 SQLite 資料庫結構定義 (26 張正式資料表 DDL)

系統於本地維護 `data/omni_studio.db`，啟動時強制執行 WAL 模式與外鍵約束。以下為全部 **26 張正式資料表**之完整 DDL：

```sql
-- =========================================================================
-- 一、系統設定、模型商城與憑證管理 (Tables 1 ~ 4)
-- =========================================================================
CREATE TABLE IF NOT EXISTS system_settings (
    setting_key TEXT PRIMARY KEY,
    setting_value TEXT NOT NULL,
    schema_version INTEGER DEFAULT 51,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS commercial_providers (
    provider_id TEXT PRIMARY KEY,
    provider_name TEXT NOT NULL,
    api_base_url TEXT,
    keyring_service_key TEXT NOT NULL,
    key_status TEXT DEFAULT 'UNCONFIGURED',
    rate_limit_rpm INTEGER DEFAULT 60,
    total_points_consumed INTEGER DEFAULT 0,
    last_verified_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS models_catalog (
    model_id TEXT PRIMARY KEY,
    store_partition TEXT NOT NULL,
    category TEXT NOT NULL,
    display_name TEXT NOT NULL,
    provider_id TEXT,
    description TEXT,
    icon_name TEXT,
    cost_badge INTEGER DEFAULT 0,
    max_ref_images INTEGER DEFAULT 1,
    required_custom_nodes_json TEXT,
    is_enabled INTEGER DEFAULT 1,
    FOREIGN KEY(provider_id) REFERENCES commercial_providers(provider_id)
);

CREATE TABLE IF NOT EXISTS local_model_versions (
    version_id TEXT PRIMARY KEY,
    model_id TEXT NOT NULL,
    version_tag TEXT NOT NULL,
    download_url TEXT NOT NULL,
    mirror_download_url TEXT,
    sha256_hash TEXT,
    file_size_gb REAL NOT NULL,
    relative_file_path TEXT NOT NULL,
    header_verified INTEGER DEFAULT 0,
    is_downloaded INTEGER DEFAULT 0,
    is_active_version INTEGER DEFAULT 1,
    remote_updated_at TIMESTAMP,
    FOREIGN KEY(model_id) REFERENCES models_catalog(model_id)
);

-- =========================================================================
-- 二、專案、劇集、版本控制與預算熔斷 (Tables 5 ~ 8)
-- =========================================================================
CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    project_name TEXT NOT NULL,
    format_preset_id TEXT NOT NULL,
    aspect_ratio TEXT DEFAULT '21:9',
    target_resolution TEXT DEFAULT '1920x800',
    fps INTEGER DEFAULT 24,
    global_lut_path TEXT,
    default_cjk_font_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS episodes (
    episode_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    episode_index INTEGER NOT NULL,
    episode_title TEXT,
    execution_mode TEXT DEFAULT 'SEMI_AUTO',
    current_gate TEXT DEFAULT 'GATE_1_OUTLINE',
    gate_status TEXT DEFAULT 'IDLE',
    master_video_path TEXT,
    me_track_audio_path TEXT,
    master_srt_path TEXT,
    master_ass_path TEXT,
    otio_export_path TEXT,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS project_versions (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    version_name TEXT NOT NULL,
    parent_version_id TEXT,
    snapshot_path TEXT NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS budget_rules (
    project_id TEXT PRIMARY KEY,
    max_shot_cost INTEGER DEFAULT 500,
    max_episode_cost INTEGER DEFAULT 5000,
    max_project_cost INTEGER DEFAULT 50000,
    current_project_spent INTEGER DEFAULT 0,
    auto_fallback_to_local INTEGER DEFAULT 1,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

-- =========================================================================
-- 三、Story Bible 連戲設定集與 Agent 長期記憶 (Tables 9 ~ 12)
-- =========================================================================
CREATE TABLE IF NOT EXISTS story_bible (
    bible_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    episode_id TEXT,
    world_rules_json TEXT,
    episode_summary TEXT,
    unresolved_hooks_json TEXT,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS agent_memories (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    agent_name TEXT NOT NULL,
    memory_type TEXT DEFAULT 'RULE',
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS character_relationships (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    from_char_asset_id TEXT NOT NULL,
    to_char_asset_id TEXT NOT NULL,
    relation_type TEXT NOT NULL,
    description TEXT,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS character_states (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    episode_id TEXT NOT NULL,
    char_asset_id TEXT NOT NULL,
    health_and_mood_state TEXT NOT NULL,
    costume_override_desc TEXT,
    props_carried_json TEXT,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

-- =========================================================================
-- 四、素材資料庫、向量索引與重抽歷史 (Tables 13 ~ 15)
-- =========================================================================
CREATE TABLE IF NOT EXISTS project_assets (
    asset_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    category TEXT NOT NULL,
    source_type TEXT NOT NULL,
    asset_name TEXT NOT NULL,
    description TEXT,
    color_tag TEXT DEFAULT 'WHITE',
    sandbox_file_path TEXT NOT NULL,
    thumbnail_256_path TEXT,
    lora_or_voice_ref_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS asset_embeddings (
    asset_id TEXT PRIMARY KEY,
    model_name TEXT NOT NULL,
    vector_dim INTEGER DEFAULT 768,
    embedding_blob BLOB NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(asset_id) REFERENCES project_assets(asset_id)
);

CREATE TABLE IF NOT EXISTS prompt_generations (
    gen_id INTEGER PRIMARY KEY AUTOINCREMENT,
    target_type TEXT NOT NULL,
    target_id TEXT NOT NULL,
    version_num INTEGER NOT NULL,
    auto_generated_prompt TEXT,
    user_modified_prompt TEXT NOT NULL,
    negative_prompt TEXT,
    seed INTEGER DEFAULT -1,
    output_file_path TEXT,
    is_selected INTEGER DEFAULT 0
);

-- =========================================================================
-- 五、畫布節點系統與工作流 Runtime 引擎 (Tables 16 ~ 20)
-- =========================================================================
CREATE TABLE IF NOT EXISTS canvas_nodes (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    canvas_tab_id TEXT DEFAULT 'CANVAS_1',
    node_type TEXT NOT NULL,
    title TEXT NOT NULL,
    position_x REAL DEFAULT 0.0,
    position_y REAL DEFAULT 0.0,
    settings_json TEXT,
    node_status TEXT DEFAULT 'PENDING',
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS canvas_edges (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    canvas_tab_id TEXT DEFAULT 'CANVAS_1',
    from_node TEXT NOT NULL,
    to_node TEXT NOT NULL,
    edge_type TEXT DEFAULT 'DEFAULT',
    FOREIGN KEY(from_node) REFERENCES canvas_nodes(id),
    FOREIGN KEY(to_node) REFERENCES canvas_nodes(id)
);

CREATE TABLE IF NOT EXISTS workflow_runs (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    episode_id TEXT,
    run_type TEXT NOT NULL,
    status TEXT NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS node_executions (
    id TEXT PRIMARY KEY,
    workflow_id TEXT NOT NULL,
    node_id TEXT NOT NULL,
    input_json TEXT,
    output_json TEXT,
    status TEXT NOT NULL,
    retry_count INTEGER DEFAULT 0,
    execution_duration_ms INTEGER DEFAULT 0,
    error_message TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(workflow_id) REFERENCES workflow_runs(id),
    FOREIGN KEY(node_id) REFERENCES canvas_nodes(id)
);

CREATE TABLE IF NOT EXISTS workflow_checkpoints (
    checkpoint_id TEXT PRIMARY KEY,
    workflow_id TEXT NOT NULL,
    gate_name TEXT NOT NULL,
    state_dump_json TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(workflow_id) REFERENCES workflow_runs(id)
);

-- =========================================================================
-- 六、多體裁分段、成對分鏡節點、GPU 佇列與多平台發布 (Tables 21 ~ 25)
-- =========================================================================
CREATE TABLE IF NOT EXISTS video_segments (
    segment_id TEXT PRIMARY KEY,
    episode_id TEXT NOT NULL,
    tier_level TEXT DEFAULT 'SCENE',
    parent_segment_id TEXT,
    segment_index INTEGER NOT NULL,
    target_max_duration_sec REAL DEFAULT 180.0,
    actual_duration_sec REAL DEFAULT 0.0,
    shared_ambiance_audio_path TEXT,
    merged_segment_video_path TEXT,
    status TEXT DEFAULT 'PENDING',
    FOREIGN KEY(episode_id) REFERENCES episodes(episode_id)
);

CREATE TABLE IF NOT EXISTS video_shots (
    shot_id TEXT PRIMARY KEY,
    segment_id TEXT NOT NULL,
    shot_code TEXT NOT NULL,
    shot_index INTEGER NOT NULL,
    image_model_id TEXT,
    style_prompt TEXT,
    scene_prompt TEXT,
    gaze_direction TEXT DEFAULT 'NEUTRAL',
    lighting_id TEXT DEFAULT 'NONE',
    image_quality TEXT DEFAULT 'HIGH',
    image_status TEXT DEFAULT 'IDLE',
    keyframe_image_path TEXT,
    depth_map_path TEXT,
    video_model_id TEXT,
    action_prompt TEXT,
    camera_motion_id TEXT DEFAULT 'STATIC',
    camera_motion_prompt TEXT,
    ambiance_audio_prompt TEXT,
    frame_mode TEXT DEFAULT 'FIRST_FRAME',
    resolution TEXT DEFAULT '720p',
    duration_sec REAL DEFAULT 5.0,
    video_seed INTEGER DEFAULT -1,
    motion_strength REAL DEFAULT 1.0,
    generate_audio_flag INTEGER DEFAULT 1,
    inherit_prev_tail_mode TEXT DEFAULT 'AS_REFERENCE',
    first_frame_path TEXT,
    best_last_frame_path TEXT,
    speaker_asset_id TEXT,
    dialogue_text TEXT,
    emotion_tag TEXT DEFAULT 'NEUTRAL',
    tts_audio_path TEXT,
    phoneme_align_json TEXT,
    trim_in_sec REAL DEFAULT 0.0,
    trim_out_sec REAL DEFAULT 0.0,
    volume_keyframes_json TEXT,
    video_status TEXT DEFAULT 'IDLE',
    proxy_480p_video_path TEXT,
    normalized_shot_video_path TEXT,
    FOREIGN KEY(segment_id) REFERENCES video_segments(segment_id)
);

CREATE TABLE IF NOT EXISTS shot_asset_bindings (
    binding_id INTEGER PRIMARY KEY AUTOINCREMENT,
    shot_id TEXT NOT NULL,
    asset_id TEXT NOT NULL,
    slot_order INTEGER NOT NULL,
    regional_mask_coords TEXT,
    FOREIGN KEY(shot_id) REFERENCES video_shots(shot_id),
    FOREIGN KEY(asset_id) REFERENCES project_assets(asset_id)
);

CREATE TABLE IF NOT EXISTS task_queue (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    task_type TEXT NOT NULL,
    target_id TEXT NOT NULL,
    priority TEXT DEFAULT 'NORMAL',
    status TEXT DEFAULT 'QUEUED',
    worker_id TEXT DEFAULT 'GPU_0',
    remote_job_id TEXT,
    provider_status_url TEXT,
    retry_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS publish_tasks (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    episode_id TEXT,
    platform TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    tags_json TEXT,
    video_file_path TEXT NOT NULL,
    c2pa_watermark_embedded INTEGER DEFAULT 1,
    status TEXT DEFAULT 'DRAFT',
    published_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(project_id) REFERENCES projects(project_id)
);

-- =========================================================================
-- 七、企業版與團隊協作預留架構 (Table 26: Enterprise Auth Group)
-- =========================================================================
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    role_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS roles (
    role_id TEXT PRIMARY KEY,
    role_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS permissions (
    perm_id TEXT PRIMARY KEY,
    role_id TEXT NOT NULL,
    resource_action TEXT NOT NULL,
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
);
```

### 第 22 章：專案標準目錄結構與細粒度程式碼模組拆分架構
*(嚴格遵循「第 0 章準則 1：單一檔案不超過 400~500 行」之細粒度模組化拆分規範)*

```text
OmniAgent_Studio/
 ├── main.py                              # 應用程式輕量入口 (僅負責啟動 Pre-Flight 體檢與主視窗)
 ├── config/
 │    ├── app_constants.py                # 全域常數、預設路徑與檔案行數/緩衝區邊界定義
 │    ├── format_presets.py               # 六大影視體裁時間結構設定檔 (1分短片 ~ 90分電影)
 │    └── camera_lighting_dict.py         # 23種運鏡與12種布光之圖文及 Prompt 映射字典
 ├── schemas/                             # [準則 5] 跨層傳輸強型別資料契約 (Pydantic Models)
 │    ├── project_schemas.py              # 專案、劇集、預算與 Story Bible 資料模型
 │    ├── asset_schemas.py                # 素材、向量、白名單綁定與多視角設定資料模型
 │    └── shot_workflow_schemas.py        # 分鏡雙卡、運鏡參數、節點狀態與佇列任務資料模型
 ├── database/                            # [準則 4] 資料持久化層 (唯一允許執行 SQL 之目錄)
 │    ├── db_connection_pool.py           # SQLite WAL 連線管理、Single-Writer 寫入鎖與滾動備份
 │    ├── schema_migrator.py              # 26張表 DDL 初始化與 PRAGMA user_version 自動遷移
 │    ├── repositories/                   # 依業務特性拆分的資料存取物件 (DAO / Repositories)
 │    │    ├── model_store_repo.py        # 商城模型、版本與 API 金鑰狀態存取
 │    │    ├── asset_bible_repo.py        # 素材庫、重抽歷史、Story Bible 與 Agent 記憶存取
 │    │    └── workflow_shot_repo.py      # 畫布節點、分鏡雙卡、佇列與 Checkpoint 存取
 │    ├── vector_index_engine.py          # sqlite-vec / HNSW 毫秒級資產向量檢索器
 │    └── project_archiver.py             # 專案沙盒複製、廢檔回收 (GC) 與 .omni_pack 打包器
 ├── core/                                # [準則 1 & 3] 業務與硬體調度核心層 (依特性細分)
 │    ├── hardware/
 │    │    ├── gpu_auto_profiler.py       # 全系列 NVIDIA 顯卡偵測、NVML 溫控保護與精度適配
 │    │    ├── vram_ram_offloader.py      # 1GB VRAM 緩衝、Pinned Memory DMA 與系統 RAM 卸載
 │    │    └── process_watchdog.py        # [準則 8] Ollama/ComfyUI/FFmpeg 子行程守護與防殭屍回收
 │    ├── model_store/
 │    │    ├── hf_civitai_crawler.py      # 背景爬蟲、HTTP Range 斷點續傳與 safetensors 標頭自癒
 │    │    └── model_menu_router.py       # 雙分區動態選單供應器、預算熔斷與 Strict Local-First 路由
 │    ├── workflow/
 │    │    ├── dag_runtime_engine.py      # Tarjan 循環檢測、Dirty Propagation 與節點執行引擎
 │    │    ├── gate_state_machine.py      # 半自動/全自動 5大 Gate 攔截器與 Checkpoint 恢復
 │    │    └── gpu_task_dispatcher.py     # 4級優先權佇列、Token Bucket 限流與雲端單號輪詢恢復
 │    └── media_pipeline/
 │         ├── comfy_ast_compiler.py      # ComfyUI 動態 AST 節點注入編譯器與依賴節點自檢
 │         ├── tail_frame_selector.py     # 智慧尾幀清晰度篩選、LAB 直方圖色彩對齊與時域去閃爍
 │         ├── depth_rmbg_compositor.py   # RMBG 羽化去背、Depth 深度圖提取與多人分區遮罩生成
 │         ├── lipsync_audio_mixer.py     # 音素級指定臉孔對嘴、語音克隆、場次環境音與 J/L-Cut 混音
 │         └── master_ffmpeg_assembler.py # CJK ASS 特效字卡、-14 LUFS 響度標準化、M&E 軌與 OTIO 匯出
 ├── providers/                           # [準則 1] 外部工具與雲端 API 驅動抽象層
 │    ├── base_provider.py                # BaseLLM / BaseImage / BaseVideo / BaseTTS 抽象介面
 │    ├── mock_dryrun_provider.py         # [準則 10] 5秒極速無頭乾跑測試專用 Mock 驅動
 │    ├── local_ollama_provider.py        # 本地 Ollama GBNF 結構化推理實作
 │    ├── local_comfy_provider.py         # 本地 ComfyUI WebSocket/HTTP 算圖與顯存釋放實作
 │    ├── local_audio_provider.py         # 本地 XTTS / CosyVoice / WhisperX / Wav2Lip 實作
 │    └── cloud_commercial_provider.py    # Seedream / Seedance / Veo 3.1 / GPT Image / Wan 雲端實作
 ├── agents/                              # 多智能體協同層
 │    ├── director_script_agent.py        # 總導演與編劇 Agent (含台詞與動作時長自動平衡裁決)
 │    ├── asset_storyboard_agent.py       # 美術設定與分鏡映射 Agent (含 180度軸線與白名單引用)
 │    ├── qa_archivist_agent.py           # QA 審查重試與 Story Bible 長期記憶維護 Agent
 │    └── prompt_magic_expander.py        # ✨ 魔法棒 Prompt 擴寫與風格吸管 (Vision 反推) 輔助器
 └── ui/                                  # [準則 1 & 2] PySide6 純視圖層 (嚴禁夾帶業務與 SQL 邏輯)
      ├── main_window.py                  # 頂部三視圖切換、分頁管理與硬體/VRAM 遙測狀態列
      ├── workers/                        # [準則 2] 專責非同步執行緒與 Signal 轉發器
      │    └── qt_async_bridge.py         # 將 core/ 與 database/ 任務封裝為 QRunnable 之橋接器
      ├── canvas/                         # 畫布視圖模組群 (拆分為獨立元件檔防膨脹)
      │    ├── infinite_dot_view.py       # 無邊際點陣畫布、3段式 LOD 視角剔除與縮放平移控制
      │    ├── canvas_minimap_toolbar.py  # 左下角小地圖、Sugiyama 自動排版與分支建立工具列
      │    ├── asset_container_item.py    # 角色(藍)/場景(綠)/道具(黃) 資產容器與 PC 拖放沙盒上傳
      │    ├── shot_pair_card_item.py     # 左圖右影成對分鏡節點主體與紫色尾幀貝茲曲線
      │    ├── floating_prompt_panel.py   # 懸浮編輯器、白名單縮圖列、@膠囊標籤與 4秒四連抽草稿
      │    ├── camera_lighting_popups.py  # 23種運鏡、12種布光與生圖/生影細部參數彈窗
      │    └── sketch_voice_tools.py      # 30秒手繪火柴人構圖畫板與按住示範語氣麥克風元件
      ├── editor/                         # 影片編輯 (NLE) 視圖模組群
      │    ├── media_bin_panel.py         # 左側導航、7色圓點標籤過濾媒體櫃與字卡/字幕面板
      │    ├── proxy_video_player.py      # 480p Proxy 寬銀幕低延遲預覽器与 10秒動態毛片播放器
      │    └── multi_track_timeline.py    # 底部多軌時間軸、分割磁吸、音量包絡線與 [🖊️合成] 控制
      ├── exports/
      │    └── final_exports_view.py      # [🎞️成片] 視圖、渲染佇列監視器與多平台發布面板
      └── dialogs/
           ├── model_store_dialog.py      # 雙分區模型商城 QTableView 介面
           └── settings_budget_dialog.py  # 模型庫根目錄、API 金鑰驗證、預算上限與夜間掛機推播設定
```