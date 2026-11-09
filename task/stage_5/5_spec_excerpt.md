# 主規格書 (`spec.md`) 針對階段 5 之相關章節摘錄

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
    execution_mode TEXT DEFAUL
...(章節截斷)...
