# 主規格書 (`spec.md`) 針對階段 8 之相關章節摘錄

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


### 第 9 章：工作流執行引擎 (Workflow Runtime Engine)
* **設計目標**：畫布節點兼具資料流與實際任務調度能力，支援暫停、恢復、失敗重試、斷電續跑、Gate 攔截、DAG 循環死鎖檢測 (`Tarjan Cycle Detection`) 與上游變更髒資料傳播 (`Dirty Propagation`)。
* **狀態機定義**：
  * **Workflow 狀態 (6 態)**：`WAITING`、`RUNNING`、`PAUSED`、`FAILED`、`COMPLETED`、`CANCELLED`。
  * **Node 狀態 (8 態)**：`PENDING`、`READY`、`RUNNING`、`SUCCESS`、`FAILED`、`SKIPPED`、`BLOCKED`、`OUTDATED`。

---


### 第 21 章：v5.0 凍結後完整 SQLite 資料庫結構定義 (26 張正式資料表 DDL)

系統於本地維護 `data/omni_studio.db`，啟動時強制執行 WAL 模式與外鍵約束。以下為全部 **26 張正式資料表**之完整 DDL：

```sql
-- =========================================================================
-- 一、系統設定、模型商城與憑證管理 (Tables 1 ~ 4)
-- =========================================================================
CREATE TABLE IF NOT EXISTS system_settings (
    setting_key TEXT PRIMARY KEY,
    setting_value TEXT NOT NULL,
    schema_version INTEGER DEFAULT 50,
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
    gate_stat
...(章節截斷)...
