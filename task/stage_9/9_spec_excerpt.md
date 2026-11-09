# 主規格書 (`spec.md`) 針對階段 9 之相關章節摘錄

### 第 8 章：多體裁動態分段架構與廣播級終極合成引擎

* **六大市場主流體裁預設**：支援 `SHORT_1MIN` (1分短片)、`SHORT_3MIN` (3分微短劇)、`MINI_SERIES_10MIN` (10分小短劇)、`TV_DRAMA_60MIN` (60分電視劇) 與 `FEATURE_FILM_90MIN` (90分以上電影)。
* **音素級多語系指定角色對嘴 (`Phoneme-Aligned Target Speaker LipSync`)**：透過 `WhisperX` 與 `CosyVoice` 零樣本 3 秒情緒語音克隆，依 `speaker_asset_id` 臉部向量鎖定發話角色執行對嘴。
* **場次級連續環境音與 J/L-Cut 混音**：同場戲 (`Scene`) 共享連續底噪軌 (`Ambiance Stem`)，切鏡處套用 `150ms Audio Crossfade` 消除聲音斷崖。
* **东亞 CJK 專業字幕與字卡引擎**：內建思源黑體、宋體與古典書法，支援直排/橫排、描邊陰影、中文避頭尾換行與滾動演職員表。
* **三軌分離、M&E 國際軌與 -14 LUFS 標準化**：分離為對白軌 (A1)、環境音軌 (A2) 與配樂軌 (A3，人聲出現時自動 Sidechain 閃避 -12dB)，由 FFmpeg 輸出主成片 `.mp4`、純音樂音效國際軌 (`_ME_Track.wav`) 與 `.srt / .ass` 字幕。

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
    bible_id TEXT PRI
...(章節截斷)...
