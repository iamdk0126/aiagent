# 主規格書 (`spec.md`) 針對階段 1 之相關章節摘錄

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
-- ====================================================
...(章節截斷)...
