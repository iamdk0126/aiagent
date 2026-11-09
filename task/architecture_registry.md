# 🗺️ 專案全域程式碼、Function 與資料表關聯註冊表 (Architecture Registry)
> 最後自動更新時間：2026-11-09 22:29:18
> **核心規範**：推理與編程模型在實作任何階段時，必須查閱本註冊表的『資料表欄位』、『跨階段模組介面』與『Function 簽章』，確保命名與參數型別 100% 吻合。

## 1. 🗄️ 資料表結構與存取關聯 (Database Tables & CRUD Mapping)
### 資料表 `N/A`
- **定義檔案**: `Stage 2.3.3` | **用途註記**: 本階段的程式碼未涉及任何資料表。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `agent_edges`
- **定義檔案**: `Stage 7.1.1` | **用途註記**: 此資料表存儲智能體邊的資訊，包括邊ID、源節點ID和目標節點ID
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `agent_nodes`
- **定義檔案**: `Stage 7.1.2` | **用途註記**: 此資料表用於持久化智能體的長期記憶數據，包含專案ID和記憶數據字段。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `agents/story_bible_memory.py::StoryBibleMemory.load_memory(), agents/story_bible_memory.py::StoryBibleMemory.save_memory()`

### 資料表 `archive_log`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 用於存檔系統操作日誌，包含操作項目 ID、項目 ID、操作資料與時間戳。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_archive(), database/project_archiver.py::ProjectArchiver.restore_archive(), database/project_assets.py::ProjectArchiver.restore_archive()`

### 資料表 `asset_embedding_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲資產的嵌入向量數據，包括嵌入向量ID、素材ID、嵌入向量和更新時間等，業務用途是支持資產的向量查詢和相似度計算，關聯到 asset_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `asset_embeddings`
- **定義檔案**: `database/asset_embeddings.py` | **用途註記**: 此資料表用於存儲資產的嵌入向量，包含 asset_id、embedding 和 created_at 字段。
- **欄位結構**: `asset_id (TEXT), embedding (BLOB), created_at (TIMESTAMP)`
- **關聯存取函數 (Read/Write)**: `database/asset_embeddings.py::AssetEmbeddings.create_embedding(), database/asset_embeddings.py::AssetEmbeddings.get_embedding(), database/asset_embeddings.py::AssetEmbeddings.update_embedding(), database/asset_embeddings.py::AssetEmbeddings.delete_embedding()`

### 資料表 `asset_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲素材的資訊，包括素材ID、名稱、類型、劇集ID、描述和更新時間等，業務用途是管理素材實體，關聯到 episode_table 和 shot_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `budget_rules`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 記錄預算規則資訊，包含規則 ID、專案 ID、各類預算限制與自動降級標誌。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `budget_settings`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲預算設置信息，包括預算上限等。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `canvas_edges`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲畫布上的邊，包含邊的唯一識別符、源節點識別符和目標節點識別符。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `checkpoint_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲檢查點的資訊，包括檢查點ID、分鏡ID、檢查點數據和更新時間等，業務用途是管理檢查點實體，關聯到 shot_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `edges`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲畫布邊的數據，包括邊的唯一識別符、源節點識別符和目標節點識別符。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `episode_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲劇集的資訊，包括劇集ID、名稱、專案ID、描述和更新時間等，業務用途是管理劇集實體，關聯到 project_table 和 asset_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `frame_table`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲フレーム的相關信息，包括帧的時間戳、圖像數據等，與 FrameContinuityEngine 中的函數進行交互。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `frames`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲影像處理任務的各幀影像數據，與 FrameContinuityEngine 類中的方法進行互動。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `histogram_table`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲色彩直方圖的相關信息，包括色彩直方圖的數據等。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `model_store`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲模型信息，包括模型名稱、描述等，ModelStoreDialog 類別通過 DBManager 和 ModelStore 模組與此資料表互動。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `core/model_menu_provider.py::ModelMenuProvider.fetch_free_local_models(), core/model_menu_provider.py::ModelMenuProvider.fetch_commercial_api_models()`

### 資料表 `permissions`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於存儲權限相關的數據，包括權限ID、權限名稱和描述。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `database/users.py::Permission.insert_permission(), database/users.py::Permission.get_permission(), database/users.py::Permission.update_permission(), database/users.py::Permission.delete_permission(), database/users.py::Permission.get_all_permissions(), database/roles.py::Permission.insert_permission(), database/roles.py::Permission.get_permission(), database/roles.py::Permission.update_permission(), database/roles.py::Permission.delete_permission(), database/roles.py::Permission.get_all_permissions(), database/permissions.py::Permission.insert_permission(), database/permissions.py::Permission.get_permission(), database/permissions.py::Permission.update_permission(), database/permissions.py::Permission.delete_permission(), database/permissions.py::Permission.get_all_permissions()`

### 資料表 `project_assets`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 記錄專案的資產資訊，包含資產 ID、專案 ID、資產類型、路徑與創建、更新時間。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `project_info`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 存儲 .omni_pack 打包的資料表，包含 project_id 和 pack_data 欄位。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_project_pack(), database/project_archiver.py::ProjectArchiver.restore_project_pack()`

### 資料表 `project_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲專案的基本資訊，包括專案ID、名稱、描述和更新時間等，業務用途是管理專案實體，關聯到 episode_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `project_versions`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 記錄專案的版本資訊，包含版本 ID、專案 ID、版本號與時間戳。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `projects`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 存儲項目的基本信息，包括項目ID、項目名稱、格式預設ID、寬高比、目標解析度、帧率、全局LUT路徑、默認CJK字體路徑、創建和更新時間等字段。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `settings`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 設置表，存儲系統設置，關聯於數據庫連線初始化。
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `shot_table`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表用於存儲分鏡的資訊，包括分鏡ID、名稱、劇集ID、素材ID、起始帧、結束帧、描述和更新時間等，業務用途是管理分鏡實體，關聯到 episode_table、asset_table 和 checkpoint_table。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_1`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `database/db_manager.py::DBManager.auto_migration()`

### 資料表 `table_10`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_100`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_101`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_102`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_103`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_104`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_105`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_106`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_107`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_108`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_109`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_11`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_110`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_111`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_112`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_113`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_114`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_115`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_116`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_117`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_118`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_119`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_12`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_120`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_121`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_122`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_123`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_124`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_125`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_126`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_127`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_128`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_129`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_13`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_130`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_131`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_132`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_133`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_134`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_135`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_136`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_137`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_138`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_139`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_14`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_140`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_141`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_142`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_143`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_144`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_145`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_146`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_147`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_148`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_149`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_15`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_150`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_151`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_152`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_153`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_154`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_155`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_156`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_157`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_158`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_159`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_16`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_160`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_161`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_162`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_163`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_164`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_165`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_166`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_167`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_168`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_169`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_17`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_170`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_171`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_172`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_173`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_174`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_175`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_176`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_177`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_178`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_179`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_18`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_180`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_181`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_182`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_183`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_184`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_185`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_186`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_187`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_188`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_189`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_19`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_190`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_191`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_192`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_193`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_194`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_195`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_196`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_197`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_198`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_199`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_2`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_20`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_200`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_201`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_202`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_203`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_204`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_205`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_206`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_207`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_208`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_209`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_21`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_210`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_211`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_212`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_213`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_214`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_215`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_216`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_217`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_218`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_219`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_22`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_220`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_221`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_222`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_223`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_224`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_225`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_226`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_227`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_228`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_229`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_23`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_230`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_231`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_232`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_233`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_234`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_235`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_236`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_237`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_238`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_239`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_24`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_240`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_241`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_242`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_243`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_244`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_245`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_246`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_247`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_248`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_249`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_25`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_250`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_251`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_252`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_253`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_254`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_255`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_256`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_257`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_258`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_259`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_26`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_260`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_261`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_262`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_263`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_264`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_265`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_266`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_267`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_268`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_269`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_27`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_270`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_271`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_272`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_273`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_274`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_275`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_276`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_277`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_278`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_279`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_28`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_280`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_281`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_282`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_283`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_284`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_285`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_286`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_29`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_3`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_30`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_31`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_32`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_33`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_34`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_35`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_36`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_37`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_38`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_39`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_4`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_40`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_41`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_42`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_43`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_44`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_45`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_46`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_47`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_48`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_49`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_5`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_50`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_51`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_52`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_53`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_54`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_55`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_56`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_57`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_58`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_59`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_6`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_60`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_61`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_62`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_63`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_64`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_65`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_66`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_67`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_68`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_69`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_7`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_70`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_71`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_72`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_73`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_74`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_75`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_76`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_77`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_78`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_79`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_8`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_80`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_81`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_82`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_83`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_84`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_85`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_86`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_87`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_88`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_89`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_9`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 此資料表用於示例，具體業務用途需根據實際需求定義
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_90`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_91`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_92`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_93`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_94`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_95`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_96`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_97`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_98`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_99`
- **定義檔案**: `database/schema_migrator.py` | **用途註記**: 由 database/schema_migrator.py 建立維護
- **欄位結構**: `id (INTEGER)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `users`
- **定義檔案**: `Stage 1.1.1` | **用途註記**: 用戶表，存儲用戶信息，關聯於數據庫連線初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `vector_index_table`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 此資料表用於存儲向量及其對應的 ID，用於向量的查詢和刪除操作。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/vector_index_engine.py::VectorIndexEngine.load_index(), database/vector_index_engine.py::VectorIndexEngine.insert_vector(), database/vector_index_engine.py::VectorIndexEngine.delete_vector()`

### 資料表 `vram_usage_table`
- **定義檔案**: `Stage 2.2.1` | **用途註記**: 此資料表用於持久化 VRAM 使用情況，包含 VRAM 使用量等相關信息。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `workflow_checkpoints`
- **定義檔案**: `database/workflow_checkpoints.py` | **用途註記**: 此資料表用於保存工作流程的檢查點數據，包括檢查點數據和創建時間。
- **欄位結構**: `id (INTEGER), created_at (TIMESTAMP)`
- **關聯存取函數 (Read/Write)**: `database/workflow_checkpoints.py::WorkflowCheckpoint.save_checkpoint(), database/workflow_checkpoints.py::WorkflowCheckpoint.load_checkpoint()`

### 資料表 `影視體裁時間結構表`
- **定義檔案**: `Stage 9.1.3` | **用途註記**: 此資料表用於持久化影視體裁的時間結構設定，包括影視體裁名稱和對應的時長。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `未見`
- **定義檔案**: `Stage 5.2.3` | **用途註記**: 未見明確提及資料表
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `無`
- **定義檔案**: `Stage 2.3.1` | **用途註記**: 本模組中未涉及資料表。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `資料表名稱`
- **定義檔案**: `Stage 5.3.2` | **用途註記**: 此資料表的業務用途與關聯說明
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

## 2. 📦 程式模組、類別與 Function 關聯索引 (Modules & Symbol Map)
### 📄 `agents/multi_agent_graph.py` (所屬階段: `7.1.2`)
- **模組職責註記**: 此檔案定義了一個多智能體圖形數據結構，用於管理智能體節點和邊，並提供了添加、獲取和查詢節點和邊的功能。
- **依賴引用 (Imports)**: `typing:(List, Optional)`
  - **Class `AgentNode`**: 智能體節點類別骨架
    - `def __init__(self, node_id: str, node_type: str)` ➔ 待推理模型或開發者補充註記
    - `def __repr__(self)` ➔ 待推理模型或開發者補充註記
  - **Class `Edge`**: 邊類別骨架
    - `def __init__(self, edge_id: str, source_node_id: str, target_node_id: str)` ➔ 待推理模型或開發者補充註記
    - `def __repr__(self)` ➔ 待推理模型或開發者補充註記
  - **Class `MultiAgentGraph`**: 圖形數據結構類別骨架
    - `def __init__(self)` ➔ 待推理模型或開發者補充註記
    - `def add_node(self, node: AgentNode)` ➔ 添加一個智能體節點到圖形中。 | 🔗 呼叫: `append`
    - `def add_edge(self, edge: Edge)` ➔ 添加一個邊到圖形中，連接兩個智能體節點。 | 🔗 呼叫: `append`
    - `def get_nodes(self) -> List[AgentNode]` ➔ 獲取圖形中的所有智能體節點。
    - `def get_edges(self) -> List[Edge]` ➔ 獲取圖形中的所有邊。
    - `def get_node_by_id(self, node_id: str) -> Optional[AgentNode]` ➔ 通過節點ID獲取特定的智能體節點。
    - `def get_edge_by_id(self, edge_id: str) -> Optional[Edge]` ➔ 通過邊ID獲取特定的邊

### 📄 `agents/story_bible_memory.py` (所屬階段: `7.2.2`)
- **模組職責註記**: 此檔案實現了智能體長期記憶的相關功能，包括記憶的加載、保存和检索。
- **依賴引用 (Imports)**: `typing:(List, Optional), database.db_manager:(DBManager)`
  - **Class `StoryBibleMemory`**: 智能體長期記憶檢索、角色關係圖與跨集狀態防穿幫注入
    - `def __init__(self, db_manager: DBManager)` ➔ 初始化 StoryBibleMemory 類別
    - `def load_memory(self, project_id: str) -> None` ➔ 從資料庫中加載特定專案的記憶數據。 | 🗄️ 資料表: `agent_nodes` | 🔗 呼叫: `execute_query`
    - `def save_memory(self, project_id: str, memory_data: dict) -> None` ➔ 將記憶數據保存到資料庫中，如果記憶已存在則進行更新。 | 🗄️ 資料表: `agent_nodes` | 🔗 呼叫: `execute_query`
    - `def retrieve_memory(self, project_id: str) -> dict` ➔ 從資料庫中检索特定專案的記憶數據並返回。 | 🔗 呼叫: `load_memory`

### 📄 `config/format_presets.py` (所屬階段: `9.1.3`)
- **模組職責註記**: 此檔案定義了影視體裁時間結構的配置類和管理類，並提供了獲取特定影視體裁和所有影視體裁的時間結構設定的方法。
- **依賴引用 (Imports)**: `typing:(Dict, List)`
  - **Class `FormatPreset`**: 影視體裁時間結構設定
    - `def __init__(self, name: str, duration: int)` ➔ 初始化影視體裁時間結構設定的預設值。
    - `def __repr__(self) -> str` ➔ 返回影視體裁時間結構的字符串表示。
  - **Class `FormatPresets`**: 六大影視體裁的時間結構設定
    - `def __init__(self)` ➔ 初始化影視體裁時間結構設定的預設值。 | 🔗 呼叫: `FormatPreset`
    - `def get_preset(self, name: str) -> FormatPreset` ➔ 獲取指定影視體裁的時間結構設定。 | 🔗 呼叫: `get`
    - `def get_all_presets(self) -> List[FormatPreset]` ➔ 獲取所有影視體裁的時間結構設定。 | 🔗 呼叫: `values`

### 📄 `core/frame_continuity_engine.py` (所屬階段: `5.2.3`)
- **模組職責註記**: 此檔案實現了FrameContinuityEngine類，用於智慧最佳尾幀挑選、LAB色彩校正、時域去閃爍與羽化去背，並通過DBManager與數據庫進行交互。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), database.db_manager:(DBManager)`
  - **Class `FrameContinuityEngine`**: 智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背
    - `def __init__(self, db_manager: DBManager)` ➔ 初始化 FrameContinuityEngine 类
    - `def select_best_last_frame(self, frames: List[Dict]) -> Optional[Dict]` ➔ 此函數的功能是選擇最佳尾幀，輸入為帧列表，輸出為最佳尾幀。
    - `def match_histograms(self, frame1: Dict, frame2: Dict) -> float` ➔ 此函數的功能是進行LAB色彩校正，輸入為兩帧，輸出為色彩匹配度。
    - `def temporal_deflicker(self, frames: List[Dict]) -> List[Dict]` ➔ 此函數的功能是進行時域去閃爍與羽化去背，輸入為帧列表，輸出為去閃爍與羽化去背的帧列表。

### 📄 `core/gpu_auto_profiler.py` (所屬階段: `2.1.2`)
- **模組職責註記**: 此檔案實現了 GPU 自適應引擎的核心功能，包括初始化 GPU 資訊、獲取 GPU 資訊、配置運算精度和記憶體管理。
- **依賴引用 (Imports)**: `torch, pynvml, typing:(Dict, Optional)`
  - **Class `NvidiaProfiler`**: NvidiaProfiler: GPU 自適應引擎的基礎架構
    - `def __init__(self)` ➔ 初始化 GPU 資訊
    - `def initialize(self) -> None` ➔ 初始化 GPU 資訊 | 🔗 呼叫: `nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetProperties`
    - `def get_device_info(self) -> Dict` ➔ 獲取 GPU 資訊 | 🔗 呼叫: `initialize`
    - `def configure_precision(self) -> None` ➔ 配置運算精度 | 🔗 呼叫: `get_device_info, set_default_tensor_type`
    - `def configure_memory_management(self) -> None` ➔ 配置記憶體管理 | 🔗 呼叫: `get_device_info, set_device, empty_cache`

### 📄 `core/master_video_assembler.py` (所屬階段: `2.3.3`)
- **模組職責註記**: 此檔案實現了 GPU 自適應引擎和 VRAM 記憶體管理，並整合了音素級指定臉孔對嘴、J/L-Cut 混音和視頻組裝功能。
- **依賴引用 (Imports)**: `torch, pynvml, typing:(Dict, Optional)`
  - **Class `NvidiaProfiler`**: NvidiaProfiler: GPU 自適應引擎的基礎架構
    - `def __init__(self)` ➔ 初始化 GPU 資訊
    - `def initialize(self) -> None` ➔ 初始化 GPU 資訊 | 🔗 呼叫: `nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetProperties`
    - `def get_device_info(self) -> Dict` ➔ 獲取 GPU 資訊 | 🔗 呼叫: `initialize`
    - `def configure_precision(self) -> None` ➔ 配置運算精度 | 🔗 呼叫: `get_device_info, set_default_tensor_type`
    - `def configure_memory_management(self) -> None` ➔ 配置記憶體管理 | 🔗 呼叫: `get_device_info, set_device, empty_cache`
  - **Class `VRAMRAMHybridManager`**: VRAM 和 RAM 協同管理器
    - `def __init__(self, vram_buffer_size: int, pinned_memory_pool: int)` ➔ 初始化 VRAM 和 RAM 協同管理器
    - `def initialize(self)` ➔ 初始化 VRAM 和 RAM 协同管理器
    - `def upload_to_vram(self, data: bytes)` ➔ 将数据上传到 VRAM | 🔗 呼叫: `ValueError`
    - `def release_from_vram(self, data: bytes)` ➔ 从 VRAM 释放数据
    - `def get_vram_usage(self) -> int` ➔ 获取 VRAM 使用情况
  - **Class `MasterVideoAssembler`**: MasterVideoAssembler: 音素級指定臉孔對嘴、J/L-Cut 混音、CJK 字卡、M&E 軌與 OTIO 匯出
    - `def __init__(self)` ➔ 初始化 MasterVideoAssembler | 🔗 呼叫: `NvidiaProfiler, VRAMRAMHybridManager`
    - `def initialize(self)` ➔ 初始化 MasterVideoAssembler | 🔗 呼叫: `initialize`
    - `def phoneme_aligned_lip_sync(self, speaker_asset_id: str, audio_clip: bytes) -> bytes` ➔ 音素級指定臉孔對嘴
    - `def j_l_cut_mix(self, audio_clip: bytes, next_audio_clip: bytes) -> bytes` ➔ J/L-Cut 混音
    - `def assemble_video(self, video_clips: list, audio_clips: list) -> bytes` ➔ 組裝視頻

### 📄 `core/model_menu_provider.py` (所屬階段: `3.2.2`)
- **模組職責註記**: 此檔案的核心職責是提供模型菜單和基礎連接接口，通過調用數據庫管理器獲取本地免費模型和商業API模型。
- **依賴引用 (Imports)**: `typing:(List, Dict), database.db_manager:(DBManager)`
  - **Class `ModelMenuProvider`**: ModelMenuProvider: 提供模型菜单和基础连接接口的类
    - `def __init__(self, db_manager: DBManager)` ➔ 初始化 ModelMenuProvider 类
    - `def fetch_free_local_models(self) -> List[Dict]` ➔ 此函數的功能是獲取本地免費模型，輸入為無，輸出為本地免費模型列表，操作的資料表為model_store。 | 🗄️ 資料表: `model_store` | 🔗 呼叫: `execute_query`
    - `def fetch_commercial_api_models(self) -> List[Dict]` ➔ 此函數的功能是獲取商業API模型，輸入為無，輸出為商業API模型列表，操作的資料表為model_store。 | 🗄️ 資料表: `model_store` | 🔗 呼叫: `execute_query`

### 📄 `core/model_store_crawler.py` (所屬階段: `3.1.2`)
- **模組職責註記**: 此檔案的核心職責是從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息，並保存到文件中。
- **依賴引用 (Imports)**: `requests, typing:(List, Dict, Optional)`
  - **Class `ModelStoreCrawler`**: ModelStoreCrawler: 用于从 Hugging Face Hub 和 Civitai v1 API 获取模型信息的类
    - `def __init__(self, hf_token: Optional[str], civitai_token: Optional[str])` ➔ 初始化 ModelStoreCrawler 类
    - `def fetch_models(self, hf_repo: str, civitai_category: str) -> List[Dict]` ➔ 從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息，並返回模型信息列表。 | 🔗 呼叫: `_fetch_hf_models, _fetch_civitai_models`
    - `def parse_model_info(self, model_info: Dict) -> Dict` ➔ 解析模型信息，返回解析後的模型信息字典。
    - `def save_models(self, models: List[Dict], save_path: str) -> None` ➔ 將模型信息保存到文件中。 | 🔗 呼叫: `write`
    - `def _fetch_hf_models(self, repo: str) -> List[Dict]` ➔ 從 Hugging Face Hub 爬取模型信息，返回模型信息列表。 | 🔗 呼叫: `get, raise_for_status, json`
    - `def _fetch_civitai_models(self, category: str) -> List[Dict]` ➔ 從 Civitai v1 爬取模型信息，返回模型信息列表。 | 🔗 呼叫: `get, raise_for_status, json`

### 📄 `core/multi_agent_graph.py` (所屬階段: `7.1.2`)
- **模組職責註記**: 此檔案定義了多智能體協同圖形數據庫的類別和相關操作，包括添加、獲取和移除節點和邊。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional)`
  - **Class `AgentNode`**: 智能體節點類別
    - `def __init__(self, node_id: str, node_type: str)` ➔ 待推理模型或開發者補充註記
  - **Class `Edge`**: 边類別
    - `def __init__(self, edge_id: str, source_node: AgentNode, target_node: AgentNode)` ➔ 待推理模型或開發者補充註記
  - **Class `MultiAgentGraph`**: 多智能體協同圖形數據庫類別
    - `def __init__(self)` ➔ 待推理模型或開發者補充註記
    - `def add_node(self, node: AgentNode)` ➔ 添加一個智能體節點到圖形數據庫中。 | 🔗 呼叫: `append`
    - `def add_edge(self, edge: Edge)` ➔ 添加一個邊到圖形數據庫中，連接兩個節點。 | 🔗 呼叫: `append`
    - `def get_node(self, node_id: str) -> Optional[AgentNode]` ➔ 根據節點ID獲取智能體節點。
    - `def get_edges(self, node_id: str) -> List[Edge]` ➔ 根據節點ID獲取所有連接的邊。
    - `def remove_node(self, node_id: str)` ➔ 根據節點ID移除智能體節點及其相關的邊。
    - `def remove_edge(self, edge_id: str)` ➔ 根據邊ID移除邊

### 📄 `core/task_queue_dispatcher.py` (所屬階段: `8.2.3`)
- **模組職責註記**: 此檔案實現了任務隊列的管理功能，包括任務的添加、執行和移除。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional, Any)`
  - **Class `TaskStatus`**: TaskStatus: 任务状态枚举
  - **Class `Task`**: Task: 任务类
    - `def __init__(self, task_id: str, task_function)` ➔ 初始化 Task 类
    - `def execute(self)` ➔ 执行任务 | 🔗 呼叫: `task_function`
  - **Class `TaskQueue`**: TaskQueue: 任务队列类
    - `def __init__(self)` ➔ 初始化 TaskQueue 类
    - `def add_task(self, task: Task)` ➔ 添加任务 | 🔗 呼叫: `append`
    - `def remove_task(self, task_id: str)` ➔ 移除任务
    - `def process_tasks(self)` ➔ 处理任务 | 🔗 呼叫: `execute, remove_task`
  - **Function `def example_task()`** ➔ 待推理模型或開發者補充註記

### 📄 `core/vram_ram_hybrid_manager.py` (所屬階段: `2.2.2`)
- **模組職責註記**: 此檔案實現了VRAM和RAM的協同管理，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **依賴引用 (Imports)**: `sqlite3, typing:(Dict, Optional)`
  - **Class `VRAMRAMHybridManager`**: VRAM 和 RAM 協同管理器
    - `def __init__(self, vram_buffer_size: int, pinned_memory_pool: int)` ➔ 初始化VRAM和RAM協同管理器，設置VRAM緩衝區大小和固定內存池大小。
    - `def initialize(self)` ➔ 初始化VRAM和RAM協同管理器的邏輯。
    - `def upload_to_vram(self, data: bytes)` ➔ 將數據上傳到VRAM，如果VRAM緩衝區已滿則拋出異常。 | 🔗 呼叫: `ValueError`
    - `def release_from_vram(self, data: bytes)` ➔ 從VRAM釋放數據。
    - `def get_vram_usage(self) -> int` ➔ 獲取VRAM的使用情況。

### 📄 `core/workflow_runtime.py` (所屬階段: `8.1.2`)
- **模組職責註記**: 此檔案實現了工作流任務管理的核心功能，包括任務註冊、執行和狀態查詢。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional)`
  - **Class `WorkflowRuntime`**: WorkflowRuntime: 管理工作流任务的类
    - `def __init__(self)` ➔ 初始化 WorkflowRuntime 类
    - `def register_task(self, task_id: str, task_function)` ➔ 註冊任務，將任務ID和任務函數存儲在tasks字典中。
    - `def execute_task(self, task_id: str)` ➔ 執行指定ID的任務，返回任務執行結果，如果任務不存在則拋出異常。 | 🔗 呼叫: `ValueError`
    - `def get_task_status(self, task_id: str) -> Optional[str]` ➔ 查詢指定ID的任務狀態，如果任務存在則返回'Running'，否則返回None。

### 📄 `database/asset_embeddings.py` (所屬階段: `4.2.2`)
- **模組職責註記**: 此檔案定義了 AssetEmbeddings 類別，用於處理資產嵌入向量的資料庫操作，包括創建、讀取、更新和刪除嵌入向量。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), sqlite3`
  - **Class `AssetEmbeddings`**: 類別 AssetEmbeddings 用於處理資產嵌入向量的資料庫操作。
    - `def __init__(self, db_path: str)` ➔ 初始化 AssetEmbeddings 類別。 | 🔗 呼叫: `connect, cursor, _create_table`
    - `def _create_table(self)` ➔ 創建 asset_embeddings 資料表，如果該表不存在。 | 🔗 呼叫: `execute, commit`
    - `def create_embedding(self, asset_id: str, embedding: bytes)` ➔ 創建一個新的資產嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def get_embedding(self, asset_id: str) -> Optional[bytes]` ➔ 讀取一個資產的嵌入向量，如果不存在則返回 None。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, fetchone`
    - `def update_embedding(self, asset_id: str, embedding: bytes)` ➔ 更新一個資產的嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def delete_embedding(self, asset_id: str)` ➔ 刪除一個資產的嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def close(self)` ➔ 關閉資料庫連線。 | 🔗 呼叫: `close`

### 📄 `database/budget_rules.py` (所屬階段: `13.1.2`)
- **模組職責註記**: 此檔案定義了管理單專案預算規則的類別，包括初始化、從資料庫讀取和寫入預算規則的功能。
- **依賴引用 (Imports)**: `typing:(Optional)`
  - **Class `BudgetRule`**: 管理單專案預算規則的類別
    - `def __init__(self, project_id: str, max_shot_cost: int, max_episode_cost: int, max_project_cost: int, current_project_spent: int, auto_fallback_to_local: int)` ➔ 初始化 BudgetRule 類別，設置預算規則的各個屬性。
    - `def from_db(cls, project_id: str)` ➔ 從資料庫讀取預算規則，返回一個 BudgetRule 實例。
    - `def save_to_db(self)` ➔ 將預算規則寫入資料庫。

### 📄 `database/canvas_edges.py` (所屬階段: `10.1.2`)
- **模組職責註記**: 此檔案定義了CanvasEdge類別，用於管理畫布邊的數據。
- **依賴引用 (Imports)**: `typing:(Optional, List, Dict)`
  - **Class `CanvasEdge`**: CanvasEdge 類別，定義邊的屬性和方法。
    - `def __init__(self, edge_id: str, source_node_id: str, target_node_id: str)` ➔ 初始化CanvasEdge物件，設置邊的屬性。
    - `def get_edge_id(self) -> str` ➔ 取得邊的唯一識別符。
    - `def get_source_node_id(self) -> str` ➔ 取得邊的源節點識別符。
    - `def get_target_node_id(self) -> str` ➔ 取得邊的目標節點識別符。
    - `def set_edge_id(self, edge_id: str) -> None` ➔ 設定邊的唯一識別符。
    - `def set_source_node_id(self, source_node_id: str) -> None` ➔ 設定邊的源節點識別符。
    - `def set_target_node_id(self, target_node_id: str) -> None` ➔ 設定邊的目標節點識別符。
    - `def __repr__(self) -> str` ➔ 取得邊的字串表示。

### 📄 `database/canvas_nodes.py` (所屬階段: `10.1.2`)
- **模組職責註記**: 此檔案定義了 CanvasEdge 類別，用於表示畫布上的邊，並提供了對邊的屬性訪問和更新方法。
- **依賴引用 (Imports)**: `typing:(Optional)`
  - **Class `CanvasEdge`**: CanvasEdge 類別，定義畫布邊的屬性和方法。
    - `def __init__(self, edge_id: str, source_node_id: str, target_node_id: str, project_id: str)` ➔ 初始化 CanvasEdge 物件。
    - `def get_edge_id(self) -> str` ➔ 取得邊ID。
    - `def get_source_node_id(self) -> str` ➔ 取得源節點ID。
    - `def get_target_node_id(self) -> str` ➔ 取得目標節點ID。
    - `def get_project_id(self) -> str` ➔ 取得專案ID。
    - `def update_target_node_id(self, new_id: str) -> None` ➔ 更新目標節點ID。
    - `def __repr__(self) -> str` ➔ 取得邊的字符串表示。

### 📄 `database/db_connection_pool.py` (所屬階段: `1.1.1`)
- **模組職責註記**: 此模組的核心職責是管理 SQLite 連線池，提供連線取得、釋放、事務處理以及基礎的 CRUD 操作介面，支援錯誤重連機制，並通過上下文管理器簡化連線使用。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple, TypeVar, Generic, ContextManager), contextlib:(contextmanager)`
  - **Class `DBConnectionPool(Generic[T])`**: SQLite 連線池類別，包含連線初始化、連線取得與釋放方法，並支援事務處理與錯誤重連機制。
    - `def __init__(self, db_path: str, max_connections: int)` ➔ 初始化 SQLite 連線池。
    - `def get_connection(self) -> sqlite3.Connection` ➔ 此函數從連線池中獲取一個 SQLite 連線，如果連線池已滿則拋出異常。輸入為無，輸出為 sqlite3.Connection 物件，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `pop, append, connect, Exception`
    - `def release_connection(self, conn: sqlite3.Connection) -> None` ➔ 此函數將已使用的 SQLite 連線釋放回連線池。輸入為 sqlite3.Connection 物件，輸出為無，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `remove, append`
    - `def get_connection_context(self) -> ContextManager[sqlite3.Connection]` ➔ 此函數是一個上下文管理器，用於在 with 語句中自動處理連線的取得以及釋放，支援事務處理。輸入為無，輸出為 ContextManager 物件，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `get_connection, release_connection`
    - `def execute_query(self, query: str, params: Optional[Tuple]) -> List[Tuple]` ➔ 此函數執行 SQL 查詢，並返回查詢結果。輸入為 SQL 查詢字串和可選的參數元組，輸出為查詢結果的列表（List[Tuple]），操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `get_connection_context, cursor, execute, fetchall`
    - `def insert_data(self, table_name: str, data: List[Tuple]) -> None` ➔ 此函數插入數據到指定的資料表。輸入為表名和數據列表，輸出為無，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `get_connection_context, cursor, join, executemany, commit`
    - `def update_data(self, table_name: str, set_clause: str, where_clause: str) -> None` ➔ 此函數更新指定資料表中的數據。輸入為表名、更新子句和篩選子句，輸出為無，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `get_connection_context, cursor, execute, commit`
    - `def delete_data(self, table_name: str, where_clause: str) -> None` ➔ 此函數刪除指定資料表中的數據。輸入為表名和篩選子句，輸出為無，操作對象為後端 SQL 資料表，但未指定表名。 | 🔗 呼叫: `get_connection_context, cursor, execute, commit`

### 📄 `database/db_manager.py` (所屬階段: `1.1.1`)
- **模組職責註記**: 此檔案實現了 SQLite 數據庫的連線管理、表初始化、自動升級、滾動備份及基本的 CRUD 操作，提供了一個完整的數據庫管理介面。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple), contextlib:(contextmanager)`
  - **Class `DBManager`**: SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
    - `def __init__(self, db_path: str)` ➔ 初始化 SQLite WAL 連線池
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取 SQLite 連線 | 🔗 呼叫: `pop, connect, append`
    - `def init_tables(self)` ➔ 初始化 26 張表 | 🔗 呼叫: `get_connection, cursor, commit, execute`
    - `def auto_migration(self)` ➔ 自動升級數據庫結構 | 🗄️ 資料表: `table_1` | 🔗 呼叫: `get_connection, cursor, execute, fetchone, commit`
    - `def rolling_backup(self)` ➔ 進行數據庫滾動備份 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def connect(self) -> None` ➔ 連接到 SQLite 數據庫 | 🔗 呼叫: `connect`
    - `def disconnect(self) -> None` ➔ 斷開與 SQLite 數據庫的連線 | 🔗 呼叫: `close`
    - `def execute_query(self, query: str, params: Optional[Tuple]) -> List[Tuple]` ➔ 執行 SQL 查詢 | 🔗 呼叫: `get_connection, cursor, fetchall, execute`
    - `def insert_data(self, table_name: str, data: List[Tuple])` ➔ 插入數據 | 🔗 呼叫: `get_connection, cursor, join, executemany, commit`
    - `def update_data(self, table_name: str, set_clause: str, where_clause: str)` ➔ 更新數據 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def delete_data(self, table_name: str, where_clause: str)` ➔ 刪除數據 | 🔗 呼叫: `get_connection, cursor, execute, commit`

### 📄 `database/permissions.py` (所屬階段: `15.1.2`)
- **模組職責註記**: 此檔案定義了權限管理功能，通過SQLite資料庫進行權限的創建、查詢、更新和刪除。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Dict, Optional)`
  - **Class `Permission`**: 權限類別，用於處理權限資料庫操作。
    - `def __init__(self, db_path: str)` ➔ 待推理模型或開發者補充註記
    - `def connect(self) -> None` ➔ 連接到SQLite資料庫。 | 🔗 呼叫: `connect`
    - `def disconnect(self) -> None` ➔ 斷開與SQLite資料庫的連線。 | 🔗 呼叫: `close`
    - `def create_table(self) -> None` ➔ 創建permissions資料表。 | 🔗 呼叫: `cursor, execute, commit`
    - `def insert_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 插入一個新權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_permission(self, permission_id: str) -> Optional[Dict]` ➔ 查詢指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchone`
    - `def update_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 更新指定權限的資料。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def delete_permission(self, permission_id: str) -> None` ➔ 刪除指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_all_permissions(self) -> List[Dict]` ➔ 查詢所有權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchall`

### 📄 `database/project_archiver.py` (所屬階段: `1.3.2`)
- **模組職責註記**: 此檔案實現了存档管理器，用於創建和恢復項目存档。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple), contextlib:(contextmanager)`
  - **Class `ProjectArchiver`**: 專案版本快照與 .omni_pack 打包匯出/還原器
    - `def __init__(self, db_path: str)` ➔ 初始化存档管理器，創建數據庫管理器實例。 | 🔗 呼叫: `DBManager`
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取連線 | 🔗 呼叫: `get_connection`
    - `def create_archive(self, project_id: int, snapshot_data: dict)` ➔ 創建項目存档，將項目、資產和嵌入數據保存到存档日誌中。 | 🗄️ 資料表: `archive_log` | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def restore_archive(self, archive_id: int)` ➔ 恢復項目存档，從存档日誌中恢復項目、資產和嵌入數據。 | 🗄️ 資料表: `archive_log` | 🔗 呼叫: `get_connection, cursor, execute, commit, fetchone`
    - `def create_project_pack(self, project_id: int, pack_data: dict)` ➔ 創建 .omni_pack 打包，將打包數據插入到 project_info 資料表中。 | 🗄️ 資料表: `project_info` | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def restore_project_pack(self, project_id: int)` ➔ 復原 .omni_pack 打包，從 project_info 資料表中讀取打包數據。 | 🗄️ 資料表: `project_info` | 🔗 呼叫: `get_connection, cursor, execute, commit, fetchone`

### 📄 `database/project_assets.py` (所屬階段: `4.1.2`)
- **模組職責註記**: 此檔案定義了項目資產的數據庫模型，包括項目資產和項目兩個表，並設置了關聯關係。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), sqlalchemy:(create_engine, Column, Integer, String, ForeignKey), sqlalchemy.ext.declarative:(declarative_base), sqlalchemy.orm:(relationship, sessionmaker), typing:(List, Dict, Optional), sqlalchemy:(create_engine, Column, Integer, String, ForeignKey), sqlalchemy.ext.declarative:(declarative_base), sqlalchemy.orm:(relationship, sessionmaker), sqlalchemy:(create_engine), sqlalchemy.orm:(sessionmaker), project_assets:(Base, ProjectAssets, Project), asset_embeddings:(AssetEmbeddings)`
  - **Class `ProjectAssets(Base)`**: 
  - **Class `Project(Base)`**: 
  - **Class `AssetEmbeddings(Base)`**: 
  - **Class `DBManager`**: 
    - `def __init__(self, db_url: str)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `create_engine, create_all, sessionmaker`
    - `def get_session(self)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `Session`
  - **Class `ProjectArchiver`**: 
    - `def __init__(self, db_url: str)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `DBManager`
    - `def create_archive(self, project_id: str, snapshot_data: str)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `get_session, first, all, filter_by, query`
    - `def restore_archive(self, project_id: str, snapshot_data: str)` ➔ 待推理模型或開發者補充註記 | 🗄️ 資料表: `archive_log` | 🔗 呼叫: `get_session`

### 📄 `database/roles.py` (所屬階段: `15.1.2`)
- **模組職責註記**: 此檔案定義了角色管理功能，但未直接使用，主要功能與權限管理相關。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Dict, Optional)`
  - **Class `Permission`**: 權限類別，用於處理權限資料庫操作。
    - `def __init__(self, db_path: str)` ➔ 待推理模型或開發者補充註記
    - `def connect(self) -> None` ➔ 連接到SQLite資料庫。 | 🔗 呼叫: `connect`
    - `def disconnect(self) -> None` ➔ 斷開與SQLite資料庫的連線。 | 🔗 呼叫: `close`
    - `def create_table(self) -> None` ➔ 創建permissions資料表。 | 🔗 呼叫: `cursor, execute, commit`
    - `def insert_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 插入一個新權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_permission(self, permission_id: str) -> Optional[Dict]` ➔ 查詢指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchone`
    - `def update_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 更新指定權限的資料。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def delete_permission(self, permission_id: str) -> None` ➔ 刪除指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_all_permissions(self) -> List[Dict]` ➔ 查詢所有權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchall`

### 📄 `database/schema_migrator.py` (所屬階段: `1.1.2`)
- **模組職責註記**: 此模組定義了資料庫版本遷移與表結構初始化的框架，包含版本管理、表創建及遷移方法，並使用上下文管理器確保資料庫連線安全釋放。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple, TypeVar, Generic, ContextManager), contextlib:(contextmanager)`
  - **Class `TableSchema`**: TableSchema: 表結構類別
    - `def __init__(self, name: str, columns: List[str], primary_key: str)` ➔ 待推理模型或開發者補充註記
  - **Class `SchemaMigrator(Generic[T])`**: SchemaMigrator: Schema 迁移器類別
    - `def __init__(self, db_path: str)` ➔ 初始化 SchemaMigrator 類別 | 🔗 呼叫: `get_current_version`
    - `def get_current_version(self) -> int` ➔ 獲取當前資料庫版本，若連線異常則回傳 0。 | 🔗 呼叫: `get_connection, cursor, execute, fetchone`
    - `def upgrade_database(self, target_version: int) -> None` ➔ 將資料庫升級到指定版本，若目標版本低於當前版本則不執行，並執行所有中間版本的升級步驟。 | 🔗 呼叫: `set_current_version, hasattr, Exception, getattr`
    - `def set_current_version(self, version: int) -> None` ➔ 設定資料庫的當前版本。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def get_connection(self) -> ContextManager[sqlite3.Connection]` ➔ 上下文管理器，用於安全獲取與釋放 SQLite 資料庫連線。 | 🔗 呼叫: `connect, close`
    - `def create_tables_from_schemas(self, schemas: List[TableSchema]) -> None` ➔ 根據 TableSchema 列表創建表結構，並支援 IF NOT EXISTS。 | 🔗 呼叫: `get_connection, cursor, commit, join, execute`
    - `def _upgrade_to_v2(self) -> None` ➔ 升級到版本 2，新增 archive_log 表。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v3(self) -> None` ➔ 升級到版本 3，新增 project_assets 表。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v4(self) -> None` ➔ 升級到版本 4，新增 project_versions 表。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v5(self) -> None` ➔ 升級到版本 5，新增 budget_rules 表。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v6(self) -> None` ➔ 升級到版本 6，尚未完成。 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v7(self) -> None` ➔ 升級到版本 7 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v8(self) -> None` ➔ 升級到版本 8 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v9(self) -> None` ➔ 升級到版本 9 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v10(self) -> None` ➔ 升級到版本 10 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v11(self) -> None` ➔ 升級到版本 11 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v12(self) -> None` ➔ 升級到版本 12 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v13(self) -> None` ➔ 升級到版本 13 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v14(self) -> None` ➔ 升級到版本 14 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v15(self) -> None` ➔ 升級到版本 15 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v16(self) -> None` ➔ 升級到版本 16 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v17(self) -> None` ➔ 升級到版本 17 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v18(self) -> None` ➔ 升級到版本 18 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v19(self) -> None` ➔ 升級到版本 19 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v20(self) -> None` ➔ 升級到版本 20 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v21(self) -> None` ➔ 升級到版本 21 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v22(self) -> None` ➔ 升級到版本 22 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v23(self) -> None` ➔ 升級到版本 23 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v24(self) -> None` ➔ 升級到版本 24 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v25(self) -> None` ➔ 升級到版本 25 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v26(self) -> None` ➔ 升級到版本 26 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v27(self) -> None` ➔ 升級到版本 27 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v28(self) -> None` ➔ 升級到版本 28 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v29(self) -> None` ➔ 升級到版本 29 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v30(self) -> None` ➔ 升級到版本 30 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v31(self) -> None` ➔ 升級到版本 31 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v32(self) -> None` ➔ 升級到版本 32 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v33(self) -> None` ➔ 升級到版本 33 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v34(self) -> None` ➔ 升級到版本 34 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v35(self) -> None` ➔ 升級到版本 35 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v36(self) -> None` ➔ 升級到版本 36 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v37(self) -> None` ➔ 升級到版本 37 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v38(self) -> None` ➔ 升級到版本 38 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v39(self) -> None` ➔ 升級到版本 39 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v40(self) -> None` ➔ 升級到版本 40 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v41(self) -> None` ➔ 升級到版本 41 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v42(self) -> None` ➔ 升級到版本 42 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v43(self) -> None` ➔ 升級到版本 43 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v44(self) -> None` ➔ 升級到版本 44 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v45(self) -> None` ➔ 升級到版本 45 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v46(self) -> None` ➔ 升級到版本 46 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v47(self) -> None` ➔ 升級到版本 47 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v48(self) -> None` ➔ 升級到版本 48 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v49(self) -> None` ➔ 升級到版本 49 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v50(self) -> None` ➔ 升級到版本 50 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v51(self) -> None` ➔ 升級到版本 51 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v52(self) -> None` ➔ 升級到版本 52 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v53(self) -> None` ➔ 升級到版本 53 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v54(self) -> None` ➔ 升級到版本 54 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v55(self) -> None` ➔ 升級到版本 55 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v56(self) -> None` ➔ 升級到版本 56 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v57(self) -> None` ➔ 升級到版本 57 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v58(self) -> None` ➔ 升級到版本 58 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v59(self) -> None` ➔ 升級到版本 59 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v60(self) -> None` ➔ 升級到版本 60 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v61(self) -> None` ➔ 升級到版本 61 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v62(self) -> None` ➔ 升級到版本 62 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v63(self) -> None` ➔ 升級到版本 63 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v64(self) -> None` ➔ 升級到版本 64 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v65(self) -> None` ➔ 升級到版本 65 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v66(self) -> None` ➔ 升級到版本 66 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v67(self) -> None` ➔ 升級到版本 67 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v68(self) -> None` ➔ 升級到版本 68 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v69(self) -> None` ➔ 升級到版本 69 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v70(self) -> None` ➔ 升級到版本 70 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v71(self) -> None` ➔ 升級到版本 71 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v72(self) -> None` ➔ 升級到版本 72 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v73(self) -> None` ➔ 升級到版本 73 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v74(self) -> None` ➔ 升級到版本 74 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v75(self) -> None` ➔ 升級到版本 75 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v76(self) -> None` ➔ 升級到版本 76 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v77(self) -> None` ➔ 升級到版本 77 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v78(self) -> None` ➔ 升級到版本 78 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v79(self) -> None` ➔ 升級到版本 79 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v80(self) -> None` ➔ 升級到版本 80 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v81(self) -> None` ➔ 升級到版本 81 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v82(self) -> None` ➔ 升級到版本 82 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v83(self) -> None` ➔ 升級到版本 83 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v84(self) -> None` ➔ 升級到版本 84 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v85(self) -> None` ➔ 升級到版本 85 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v86(self) -> None` ➔ 升級到版本 86 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v87(self) -> None` ➔ 升級到版本 87 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v88(self) -> None` ➔ 升級到版本 88 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v89(self) -> None` ➔ 升級到版本 89 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v90(self) -> None` ➔ 升級到版本 90 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v91(self) -> None` ➔ 升級到版本 91 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v92(self) -> None` ➔ 升級到版本 92 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v93(self) -> None` ➔ 升級到版本 93 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v94(self) -> None` ➔ 升級到版本 94 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v95(self) -> None` ➔ 升級到版本 95 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v96(self) -> None` ➔ 升級到版本 96 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v97(self) -> None` ➔ 升級到版本 97 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v98(self) -> None` ➔ 升級到版本 98 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v99(self) -> None` ➔ 升級到版本 99 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v100(self) -> None` ➔ 升級到版本 100 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v101(self) -> None` ➔ 升級到版本 101 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v102(self) -> None` ➔ 升級到版本 102 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v103(self) -> None` ➔ 升級到版本 103 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v104(self) -> None` ➔ 升級到版本 104 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v105(self) -> None` ➔ 升級到版本 105 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v106(self) -> None` ➔ 升級到版本 106 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v107(self) -> None` ➔ 升級到版本 107 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v108(self) -> None` ➔ 升級到版本 108 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v109(self) -> None` ➔ 升級到版本 109 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v110(self) -> None` ➔ 升級到版本 110 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v111(self) -> None` ➔ 升級到版本 111 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v112(self) -> None` ➔ 升級到版本 112 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v113(self) -> None` ➔ 升級到版本 113 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v114(self) -> None` ➔ 升級到版本 114 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v115(self) -> None` ➔ 升級到版本 115 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v116(self) -> None` ➔ 升級到版本 116 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v117(self) -> None` ➔ 升級到版本 117 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v118(self) -> None` ➔ 升級到版本 118 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v119(self) -> None` ➔ 升級到版本 119 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v120(self) -> None` ➔ 升級到版本 120 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v121(self) -> None` ➔ 升級到版本 121 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v122(self) -> None` ➔ 升級到版本 122 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v123(self) -> None` ➔ 升級到版本 123 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v124(self) -> None` ➔ 升級到版本 124 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v125(self) -> None` ➔ 升級到版本 125 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v126(self) -> None` ➔ 升級到版本 126 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v127(self) -> None` ➔ 升級到版本 127 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v128(self) -> None` ➔ 升級到版本 128 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v129(self) -> None` ➔ 升級到版本 129 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v130(self) -> None` ➔ 升級到版本 130 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v131(self) -> None` ➔ 升級到版本 131 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v132(self) -> None` ➔ 升級到版本 132 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v133(self) -> None` ➔ 升級到版本 133 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v134(self) -> None` ➔ 升級到版本 134 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v135(self) -> None` ➔ 升級到版本 135 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v136(self) -> None` ➔ 升級到版本 136 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v137(self) -> None` ➔ 升級到版本 137 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v138(self) -> None` ➔ 升級到版本 138 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v139(self) -> None` ➔ 升級到版本 139 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v140(self) -> None` ➔ 升級到版本 140 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v141(self) -> None` ➔ 升級到版本 141 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v142(self) -> None` ➔ 升級到版本 142 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v143(self) -> None` ➔ 升級到版本 143 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v144(self) -> None` ➔ 升級到版本 144 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v145(self) -> None` ➔ 升級到版本 145 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v146(self) -> None` ➔ 升級到版本 146 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v147(self) -> None` ➔ 升級到版本 147 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v148(self) -> None` ➔ 升級到版本 148 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v149(self) -> None` ➔ 升級到版本 149 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v150(self) -> None` ➔ 升級到版本 150 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v151(self) -> None` ➔ 升級到版本 151 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v152(self) -> None` ➔ 升級到版本 152 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v153(self) -> None` ➔ 升級到版本 153 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v154(self) -> None` ➔ 升級到版本 154 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v155(self) -> None` ➔ 升級到版本 155 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v156(self) -> None` ➔ 升級到版本 156 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v157(self) -> None` ➔ 升級到版本 157 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v158(self) -> None` ➔ 升級到版本 158 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v159(self) -> None` ➔ 升級到版本 159 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v160(self) -> None` ➔ 升級到版本 160 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v161(self) -> None` ➔ 升級到版本 161 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v162(self) -> None` ➔ 升級到版本 162 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v163(self) -> None` ➔ 升級到版本 163 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v164(self) -> None` ➔ 升級到版本 164 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v165(self) -> None` ➔ 升級到版本 165 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v166(self) -> None` ➔ 升級到版本 166 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v167(self) -> None` ➔ 升級到版本 167 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v168(self) -> None` ➔ 升級到版本 168 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v169(self) -> None` ➔ 升級到版本 169 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v170(self) -> None` ➔ 升級到版本 170 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v171(self) -> None` ➔ 升級到版本 171 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v172(self) -> None` ➔ 升級到版本 172 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v173(self) -> None` ➔ 升級到版本 173 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v174(self) -> None` ➔ 升級到版本 174 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v175(self) -> None` ➔ 升級到版本 175 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v176(self) -> None` ➔ 升級到版本 176 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v177(self) -> None` ➔ 升級到版本 177 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v178(self) -> None` ➔ 升級到版本 178 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v179(self) -> None` ➔ 升級到版本 179 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v180(self) -> None` ➔ 升級到版本 180 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v181(self) -> None` ➔ 升級到版本 181 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v182(self) -> None` ➔ 升級到版本 182 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v183(self) -> None` ➔ 升級到版本 183 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v184(self) -> None` ➔ 升級到版本 184 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v185(self) -> None` ➔ 升級到版本 185 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v186(self) -> None` ➔ 升級到版本 186 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v187(self) -> None` ➔ 升級到版本 187 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v188(self) -> None` ➔ 升級到版本 188 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v189(self) -> None` ➔ 升級到版本 189 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v190(self) -> None` ➔ 升級到版本 190 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v191(self) -> None` ➔ 升級到版本 191 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v192(self) -> None` ➔ 升級到版本 192 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v193(self) -> None` ➔ 升級到版本 193 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v194(self) -> None` ➔ 升級到版本 194 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v195(self) -> None` ➔ 升級到版本 195 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v196(self) -> None` ➔ 升級到版本 196 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v197(self) -> None` ➔ 升級到版本 197 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v198(self) -> None` ➔ 升級到版本 198 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v199(self) -> None` ➔ 升級到版本 199 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v200(self) -> None` ➔ 升級到版本 200 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v201(self) -> None` ➔ 升級到版本 201 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v202(self) -> None` ➔ 升級到版本 202 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v203(self) -> None` ➔ 升級到版本 203 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v204(self) -> None` ➔ 升級到版本 204 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v205(self) -> None` ➔ 升級到版本 205 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v206(self) -> None` ➔ 升級到版本 206 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v207(self) -> None` ➔ 升級到版本 207 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v208(self) -> None` ➔ 升級到版本 208 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v209(self) -> None` ➔ 升級到版本 209 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v210(self) -> None` ➔ 升級到版本 210 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v211(self) -> None` ➔ 升級到版本 211 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v212(self) -> None` ➔ 升級到版本 212 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v213(self) -> None` ➔ 升級到版本 213 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v214(self) -> None` ➔ 升級到版本 214 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v215(self) -> None` ➔ 升級到版本 215 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v216(self) -> None` ➔ 升級到版本 216 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v217(self) -> None` ➔ 升級到版本 217 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v218(self) -> None` ➔ 升級到版本 218 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v219(self) -> None` ➔ 升級到版本 219 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v220(self) -> None` ➔ 升級到版本 220 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v221(self) -> None` ➔ 升級到版本 221 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v222(self) -> None` ➔ 升級到版本 222 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v223(self) -> None` ➔ 升級到版本 223 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v224(self) -> None` ➔ 升級到版本 224 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v225(self) -> None` ➔ 升級到版本 225 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v226(self) -> None` ➔ 升級到版本 226 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v227(self) -> None` ➔ 升級到版本 227 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v228(self) -> None` ➔ 升級到版本 228 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v229(self) -> None` ➔ 升級到版本 229 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v230(self) -> None` ➔ 升級到版本 230 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v231(self) -> None` ➔ 升級到版本 231 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v232(self) -> None` ➔ 升級到版本 232 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v233(self) -> None` ➔ 升級到版本 233 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v234(self) -> None` ➔ 升級到版本 234 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v235(self) -> None` ➔ 升級到版本 235 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v236(self) -> None` ➔ 升級到版本 236 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v237(self) -> None` ➔ 升級到版本 237 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v238(self) -> None` ➔ 升級到版本 238 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v239(self) -> None` ➔ 升級到版本 239 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v240(self) -> None` ➔ 升級到版本 240 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v241(self) -> None` ➔ 升級到版本 241 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v242(self) -> None` ➔ 升級到版本 242 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v243(self) -> None` ➔ 升級到版本 243 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v244(self) -> None` ➔ 升級到版本 244 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v245(self) -> None` ➔ 升級到版本 245 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v246(self) -> None` ➔ 升級到版本 246 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v247(self) -> None` ➔ 升級到版本 247 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v248(self) -> None` ➔ 升級到版本 248 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v249(self) -> None` ➔ 升級到版本 249 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v250(self) -> None` ➔ 升級到版本 250 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v251(self) -> None` ➔ 升級到版本 251 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v252(self) -> None` ➔ 升級到版本 252 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v253(self) -> None` ➔ 升級到版本 253 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v254(self) -> None` ➔ 升級到版本 254 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v255(self) -> None` ➔ 升級到版本 255 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v256(self) -> None` ➔ 升級到版本 256 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v257(self) -> None` ➔ 升級到版本 257 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v258(self) -> None` ➔ 升級到版本 258 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v259(self) -> None` ➔ 升級到版本 259 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v260(self) -> None` ➔ 升級到版本 260 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v261(self) -> None` ➔ 升級到版本 261 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v262(self) -> None` ➔ 升級到版本 262 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v263(self) -> None` ➔ 升級到版本 263 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v264(self) -> None` ➔ 升級到版本 264 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v265(self) -> None` ➔ 升級到版本 265 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v266(self) -> None` ➔ 升級到版本 266 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v267(self) -> None` ➔ 升級到版本 267 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v268(self) -> None` ➔ 升級到版本 268 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v269(self) -> None` ➔ 升級到版本 269 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v270(self) -> None` ➔ 升級到版本 270 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v271(self) -> None` ➔ 升級到版本 271 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v272(self) -> None` ➔ 升級到版本 272 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v273(self) -> None` ➔ 升級到版本 273 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v274(self) -> None` ➔ 升級到版本 274 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v275(self) -> None` ➔ 升級到版本 275 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v276(self) -> None` ➔ 升級到版本 276 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v277(self) -> None` ➔ 升級到版本 277 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v278(self) -> None` ➔ 升級到版本 278 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v279(self) -> None` ➔ 升級到版本 279 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v280(self) -> None` ➔ 升級到版本 280 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v281(self) -> None` ➔ 升級到版本 281 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v282(self) -> None` ➔ 升級到版本 282 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v283(self) -> None` ➔ 升級到版本 283 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v284(self) -> None` ➔ 升級到版本 284 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v285(self) -> None` ➔ 升級到版本 285 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v286(self) -> None` ➔ 升級到版本 286 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v287(self) -> None` ➔ 升級到版本 287 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v288(self) -> None` ➔ 升級到版本 288 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v289(self) -> None` ➔ 升級到版本 289 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v290(self) -> None` ➔ 升級到版本 290 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v291(self) -> None` ➔ 升級到版本 291 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v292(self) -> None` ➔ 升級到版本 292 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v293(self) -> None` ➔ 升級到版本 293 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v294(self) -> None` ➔ 升級到版本 294 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v295(self) -> None` ➔ 升級到版本 295 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v296(self) -> None` ➔ 升級到版本 296 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v297(self) -> None` ➔ 升級到版本 297 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v298(self) -> None` ➔ 升級到版本 298 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v299(self) -> None` ➔ 升級到版本 299 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v300(self) -> None` ➔ 升級到版本 300 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v301(self) -> None` ➔ 升級到版本 301 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v302(self) -> None` ➔ 升級到版本 302 | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def _upgrade_to_v303(self) -> None` ➔ 升級到版本 303 | 🔗 呼叫: `get_connection, cursor, execute`

### 📄 `database/users.py` (所屬階段: `15.1.2`)
- **模組職責註記**: 此檔案定義了用戶管理功能，但未直接使用，主要功能與權限管理相關。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Dict, Optional)`
  - **Class `Permission`**: 權限類別，用於處理權限資料庫操作。
    - `def __init__(self, db_path: str)` ➔ 待推理模型或開發者補充註記
    - `def connect(self) -> None` ➔ 連接到SQLite資料庫。 | 🔗 呼叫: `connect`
    - `def disconnect(self) -> None` ➔ 斷開與SQLite資料庫的連線。 | 🔗 呼叫: `close`
    - `def create_table(self) -> None` ➔ 創建permissions資料表。 | 🔗 呼叫: `cursor, execute, commit`
    - `def insert_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 插入一個新權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_permission(self, permission_id: str) -> Optional[Dict]` ➔ 查詢指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchone`
    - `def update_permission(self, permission_id: str, permission_name: str, description: str) -> None` ➔ 更新指定權限的資料。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def delete_permission(self, permission_id: str) -> None` ➔ 刪除指定權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, commit`
    - `def get_all_permissions(self) -> List[Dict]` ➔ 查詢所有權限。 | 🗄️ 資料表: `permissions` | 🔗 呼叫: `cursor, execute, fetchall`

### 📄 `database/vector_index_engine.py` (所屬階段: `1.2.2`)
- **模組職責註記**: 此檔案實現了一個向量索引引擎，使用 HNSW 算法和 SQLite 數據庫來存儲和查詢向量。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple), hnswlib:(HierarchicalNSW), numpy`
  - **Class `VectorIndexEngine`**: sqlite-vec / HNSW 毫秒級資產向量檢索器
    - `def __init__(self, db_path: str, index_path: str)` ➔ 初始化向量索引引擎，設置資料庫和索引路徑，並加載索引。 | 🔗 呼叫: `load_index`
    - `def load_index(self)` ➔ 加載 HNSW 索引和向量數據到記憶體中。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `HierarchicalNSW, load_index, get_connection, cursor, execute, fetchall, append, add_item`
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取 SQLite 連線。 | 🔗 呼叫: `DBManager, get_connection`
    - `def insert_vector(self, vector: np.ndarray, vector_id: int)` ➔ 插入向量到數據庫和索引中。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `add_item, append, get_connection, cursor, execute, commit, tobytes`
    - `def search_vector(self, vector: np.ndarray, k: int) -> List[Tuple[int, float]]` ➔ 查詢最接近的向量及其距離。 | 🔗 呼叫: `search_knn`
    - `def delete_vector(self, vector_id: int)` ➔ 從數據庫和索引中刪除向量。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `delete_item, remove, get_connection, cursor, execute, commit`

### 📄 `database/workflow_checkpoints.py` (所屬階段: `14.1.2`)
- **模組職責註記**: 此檔案定義了 WorkflowCheckpoint 類別，用於管理工作流程的檢查點，包括保存和加載檢查點。
- **依賴引用 (Imports)**: `sqlite3, typing:(Optional)`
  - **Class `WorkflowCheckpoint`**: WorkflowCheckpoint 類別用於管理工作流程的檢查點，包括保存和加載檢查點。
    - `def __init__(self, db_path: str)` ➔ 初始化 WorkflowCheckpoint 類別。 | 🔗 呼叫: `connect, cursor, _create_table`
    - `def _create_table(self)` ➔ 創建 workflow_checkpoints 表，如果表不存在。 | 🔗 呼叫: `execute, commit`
    - `def save_checkpoint(self, checkpoint_data: bytes)` ➔ 保存檢查點數據到 workflow_checkpoints 表中。 | 🗄️ 資料表: `workflow_checkpoints` | 🔗 呼叫: `execute, commit`
    - `def load_checkpoint(self) -> Optional[bytes]` ➔ 從 workflow_checkpoints 表中加載最新的檢查點數據。 | 🗄️ 資料表: `workflow_checkpoints` | 🔗 呼叫: `execute, fetchone`
    - `def __del__(self)` ➔ 類別析構函數，關閉數據庫連接。 | 🔗 呼叫: `close`

### 📄 `schemas/shot_workflow_schemas.py` (所屬階段: `1.1.3`)
- **模組職責註記**: 此檔案的核心職責是定義 Pydantic 資料模型，用於表示系統中的核心實體，包括專案、劇集、素材、分鏡、檢查點和資產嵌入向量。這些模型將用於 API 的請求/回應、資料庫操作或前端展示，確保資料的一致性和結構化。
- **依賴引用 (Imports)**: `pydantic:(BaseModel, Field), typing:(List, Optional, Dict, Any)`
  - **Class `Project(BaseModel)`**: Project: 專案資料模型
  - **Class `Episode(BaseModel)`**: Episode: 剧集資料模型
  - **Class `Asset(BaseModel)`**: Asset: 素材資料模型
  - **Class `Shot(BaseModel)`**: Shot: 分鏡資料模型
  - **Class `Checkpoint(BaseModel)`**: Checkpoint: 檢查點資料模型
  - **Class `AssetEmbedding(BaseModel)`**: AssetEmbedding: 資產嵌入向量資料模型

### 📄 `ui/canvas/asset_container_node.py` (所屬階段: `5.5.2`)
- **模組職責註記**: 此檔案定義了AssetContainerNode類，用於管理角色、場景和道具的資產容器，並提供了相關的資產管理功能。
- **依賴引用 (Imports)**: `typing:(List, Optional)`
  - **Class `AssetContainerNode`**: 角色(藍)/場景(綠)/道具(黃) 資產容器與 PC 拖放沙盒上傳
    - `def __init__(self, asset_type: str, asset_name: str, asset_path: str)` ➔ 初始化AssetContainerNode類，設置資產類型、名稱和路徑，並初始化資產列表。
    - `def add_asset(self, asset: str) -> None` ➔ 向資產列表中添加一個資產。 | 🔗 呼叫: `append`
    - `def remove_asset(self, asset: str) -> None` ➔ 從資產列表中移除一個資產。 | 🔗 呼叫: `remove`
    - `def get_assets(self) -> List[str]` ➔ 獲取所有資產的列表。
    - `def get_asset_info(self, asset_name: str) -> Optional[str]` ➔ 獲取指定資產的資訊。
    - `def sort_assets(self) -> None` ➔ 對資產列表進行排序。 | 🔗 呼叫: `sort`
    - `def classify_assets(self, category: str) -> List[str]` ➔ 根據指定分類對資產進行分類。
    - `def search_assets(self, keyword: str) -> List[str]` ➔ 根據指定關鍵字搜索資產。

### 📄 `ui/canvas/infinite_dot_canvas.py` (所屬階段: `5.4.2`)
- **模組職責註記**: 此檔案實現了無邊際點陣畫布的邏輯，包括節點和連線的管理以及圖形項的創建。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), PySide6.QtWidgets:(QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem), PySide6.QtCore:(Qt, QPointF)`
  - **Class `Node`**: 節點類別，表示畫布上的節點
    - `def __init__(self, id: int, position: QPointF)` ➔ 初始化 Node 类
    - `def add_connection(self, edge: 'Edge')` ➔ 添加連線 | 🔗 呼叫: `append`
    - `def remove_connection(self, edge: 'Edge')` ➔ 移除連線 | 🔗 呼叫: `remove`
  - **Class `Edge`**: 連線類別，表示畫布上的連線
    - `def __init__(self, source: Node, target: Node)` ➔ 初始化 Edge 类
  - **Class `InfiniteDotCanvas(QGraphicsScene)`**: 無邊際點陣畫布類別，表示畫布上的畫布
    - `def __init__(self)` ➔ 初始化 InfiniteDotCanvas 类 | 🔗 呼叫: `__init__`
    - `def add_node(self, node: Node)` ➔ 添加節點 | 🔗 呼叫: `append, addItem, create_node_item`
    - `def add_edge(self, edge: Edge)` ➔ 添加連線 | 🔗 呼叫: `append, addItem, create_edge_item`
    - `def create_node_item(self, node: Node) -> QGraphicsItem` ➔ 創建節點圖形項 | 🔗 呼叫: `QGraphicsEllipseItem, setBrush, x, y`
    - `def create_edge_item(self, edge: Edge) -> QGraphicsItem` ➔ 創建連線圖形項 | 🔗 呼叫: `QGraphicsLineItem, setPen, x, y`

### 📄 `ui/canvas/shot_pair_node_widget.py` (所屬階段: `5.1.2`)
- **模組職責註記**: 此檔案的核心職責是實現圖形用戶界面的模組，包括左圖右影成對分鏡卡、白名單縮圖列、運鏡/布光/參數懸浮框。
- **依賴引用 (Imports)**: `PySide6.QtWidgets:(QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QComboBox, QLineEdit, QPushButton), PySide6.QtCore:(Qt)`
  - **Class `ShotPairNodeWidget(QWidget)`**: 左圖右影成對分鏡卡、白名單縮圖列、運鏡/布光/參數懸浮框
    - `def __init__(self, parent)` ➔ 初始化 ShotPairNodeWidget 类，設置父窗口。 | 🔗 呼叫: `__init__, initUI`
    - `def initUI(self)` ➔ 初始化 UI 元素，包括左圖右影成對分鏡卡、白名單縮圖列、運鏡/布光/參數懸浮框。 | 🔗 呼叫: `QVBoxLayout, QLabel, QHBoxLayout, addWidget, addLayout, QListWidget, QComboBox, QLineEdit`
    - `def add_frame(self, left_frame, right_frame)` ➔ 添加左圖右影成對分鏡卡。 | 🔗 呼叫: `setText`
    - `def add_to_white_list(self, item)` ➔ 將項目添加到白名單。 | 🔗 呼叫: `addItem`
    - `def set_camera(self, camera)` ➔ 設置運鏡。 | 🔗 呼叫: `setCurrentText`
    - `def set_lighting(self, lighting)` ➔ 設置布光。 | 🔗 呼叫: `setCurrentText`
    - `def set_parameters(self, parameters)` ➔ 設置參數。 | 🔗 呼叫: `setText`

### 📄 `ui/dialogs/model_store_dialog.py` (所屬階段: `5.6.2`)
- **模組職責註記**: 此檔案的核心職責是提供一個對話框用於顯示和管理 model_store 資料表中的模型信息，包括初始化 UI 元素、刷新模型列表等。
- **依賴引用 (Imports)**: `PySide6.QtWidgets:(QDialog, QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QLabel), PySide6.QtCore:(Qt), database.db_manager:(DBManager), database.model_store:(ModelStore)`
  - **Class `ModelStoreDialog(QDialog)`**: ModelStoreDialog 類別用於顯示和管理 model_store 資料表中的模型信息。
    - `def __init__(self, parent)` ➔ 初始化 ModelStoreDialog 类，設置父窗口並初始化 UI 元素。 | 🔗 呼叫: `__init__, initUI`
    - `def initUI(self)` ➔ 初始化 UI 元素，包括模型列表顯示和按鈕布局。 | 🔗 呼叫: `QVBoxLayout, QTableView, setSelectionBehavior, setSelectionMode, addWidget, QHBoxLayout, QPushButton, connect`
    - `def refresh_model_list(self)` ➔ 刷新模型列表，從 model_store 資料表中獲取模型信息並顯示在 QTableView 中。 | 🔗 呼叫: `get_all_models, setModel, resizeColumnsToContents`

### 📄 `ui/dialogs/settings_budget_dialog.py` (所屬階段: `6.2.2`)
- **模組職責註記**: 此檔案實現了預算設置對話框的 UI 界面和基本功能，包括顯示和更新預算設置。
- **依賴引用 (Imports)**: `PySide6.QtWidgets:(QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton), PySide6.QtCore:(Qt), typing:(Optional)`
  - **Class `SettingsBudgetDialog(QDialog)`**: 設置預算設置對話框
    - `def __init__(self, parent)` ➔ 初始化方法，設置對話框標題和初始化 UI 元素。 | 🔗 呼叫: `__init__, setWindowTitle, initUI`
    - `def initUI(self)` ➔ 初始化 UI 元素，包括標籤、輸入框和按鈕。 | 🔗 呼叫: `QVBoxLayout, QLabel, addWidget, QLineEdit, setPlaceholderText, QPushButton, connect, setLayout`
    - `def show_budget_settings(self, budget: float)` ➔ 顯示預算設置，將預算值顯示在輸入框中。 | 🔗 呼叫: `setText`
    - `def update_budget_settings(self)` ➔ 更新預算設置，從輸入框中獲取預算值並進行驗證，如果驗證通過則更新預算設置。 | 🔗 呼叫: `text`

### 📄 `ui/editor/nle_timeline_editor.py` (所屬階段: `6.1.2`)
- **模組職責註記**: 此檔案實現了NLE時間軸編輯器的核心邏輯，包括節點和連線的管理，以及編輯器的排序和自動連接功能。
- **依賴引用 (Imports)**: `typing:(List, Optional), PySide6.QtWidgets:(QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem), PySide6.QtCore:(Qt, QPointF, QRectF)`
  - **Class `Node(QGraphicsItem)`**: 節點類別，表示畫布上的節點
    - `def __init__(self, id: int, position: QPointF)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `__init__`
    - `def add_connection(self, edge: 'Edge') -> None` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `append`
    - `def remove_connection(self, edge: 'Edge') -> None` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `remove`
    - `def boundingRect(self) -> QRectF` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `QRectF`
    - `def paint(self, painter, option, widget)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `setBrush, drawEllipse, boundingRect`
  - **Class `Edge(QGraphicsItem)`**: 連線類別，表示畫布上的連線
    - `def __init__(self, source: Node, target: Node)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `__init__`
    - `def boundingRect(self) -> QRectF` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `QRectF`
    - `def paint(self, painter, option, widget)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `setPen, drawLine`
  - **Class `NLETimelineEditor(QGraphicsScene)`**: NLE 時間軸編輯器類別，表示畫布上的編輯器
    - `def __init__(self)` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `__init__`
    - `def add_node(self, node: Node) -> None` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `addItem, append`
    - `def add_edge(self, edge: Edge) -> None` ➔ 待推理模型或開發者補充註記 | 🔗 呼叫: `addItem, append`
    - `def create_node_item(self, node: Node) -> QGraphicsItem` ➔ 待推理模型或開發者補充註記
    - `def create_edge_item(self, edge: Edge) -> QGraphicsItem` ➔ 待推理模型或開發者補充註記
    - `def sort_nodes(self) -> None` ➔ 節點排序
    - `def align_timeline(self) -> None` ➔ 時間軸對齊
    - `def auto_connect_edges(self) -> None` ➔ 边的自動連接

### 📄 `ui/main_window.py` (所屬階段: `5.3.2`)
- **模組職責註記**: 此檔案實現了主視窗類別，包含頂部三視圖切換介面，包括畫布視圖、影片編輯視圖、成片視圖和硬體遙測狀態視圖。
- **依賴引用 (Imports)**: `PySide6.QtWidgets:(QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QLabel), PySide6.QtCore:(Qt, QTimer), psutil`
  - **Class `MainWindow(QMainWindow)`**: 主視窗類別，包含頂部三視圖切換介面
    - `def __init__(self)` ➔ 初始化 MainWindow 类 | 🔗 呼叫: `__init__, initUI`
    - `def initUI(self)` ➔ 初始化 UI 元素 | 🔗 呼叫: `setWindowTitle, setGeometry, QTabWidget, setCentralWidget, QWidget, addTab, initCanvasTab, initEditorTab`
    - `def initCanvasTab(self)` ➔ 初始化畫布視圖 | 🔗 呼叫: `QVBoxLayout, QLabel, setAlignment, addWidget, setLayout`
    - `def initEditorTab(self)` ➔ 初始化影片編輯視圖 | 🔗 呼叫: `QVBoxLayout, QLabel, setAlignment, addWidget, setLayout`
    - `def initOutputTab(self)` ➔ 初始化成片視圖 | 🔗 呼叫: `QVBoxLayout, QLabel, setAlignment, addWidget, setLayout`
    - `def initHardwareMonitorTab(self)` ➔ 初始化硬體遙測狀態視圖 | 🔗 呼叫: `QVBoxLayout, QFrame, setFrameShape, setLineWidth, QLabelText, addWidget, setLayout, QTimer`
    - `def updateHardwareMonitor(self)` ➔ 更新硬體遙測狀態 | 🔗 呼叫: `Process, sensors_temperatures, setText, memory_info, virtual_memory`

## 3. 📝 各階段完成後之推理模型語意與關聯總結 (Stage Post-Coding Semantic Notes)
- **階段 `1.1.1` 關聯總結**: 本階段實作資料庫連線池管理，提供基礎 CRUD 功能的支援，這些操作會與後端 SQL 資料表互動，但程式碼中未明確定義資料表，因此 CRUD 函數的具體操作對象需由其他模組或業務邏輯指定。
- **階段 `1.1.2` 關聯總結**: 階段 1.1.2 實作的 SchemaMigrator 模組與資料庫版本管理及表結構初始化相關，主要通過 Generic 泛型類別定義資料庫遷移框架，並提供版本獲取、升級及表創建功能，與後端資料庫操作模組（如 project_data_access）及資料庫版本控制文件（如 database_schema_versions.txt）互動，確保表結構與版本需求一致。
- **階段 `1.1.3` 關聯總結**: 階段 1.1.3 定義了多個 Pydantic 資料模型，這些模型將用於 API 的資料交換、資料庫 ORM 映射或其他服務的資料結構定義，並與父階段的規範保持一致，通過明確的資料結構支持系統的其他功能模組。
- **階段 `1.2.1` 關聯總結**: 本階段實現了向量索引引擎，與SQLite資料庫和HNSW索引庫互動，進行向量的插入、查詢和刪除操作。
- **階段 `1.2.2` 關聯總結**: 本階段實現了向量索引引擎，與父階段和資料表互動，進行向量的插入、查詢和刪除操作。
- **階段 `1.3.1` 關聯總結**: 本階段實現了 ProjectArchiver 類別，用於管理專案版本快照和 .omni_pack 打包的創建與復原，與資料庫進行互動。
- **階段 `1.3.2` 關聯總結**: 本階段實現了專案版本快照和 .omni_pack 打包的創建與復原功能，與父階段和資料表進行了互動。
- **階段 `2.1.1` 關聯總結**: 本階段實現了 GPU 自適應引擎的基础框架，包括初始化 GPU 信息、获取 GPU 信息、配置运算精度和配置内存管理，并与父阶段和相关模块进行交互。
- **階段 `2.1.2` 關聯總結**: 本階段實現了 GPU 自適應引擎的核心功能，包括初始化 GPU 資訊、獲取 GPU 資訊、配置運算精度和記憶體管理。
- **階段 `2.2.1` 關聯總結**: 本階段實現了 VRAM 和 RAM 協同管理器，該管理器通過初始化、上傳和釋放數據來管理 VRAM 和 RAM 的使用情況，並與資料庫進行互動以持久化管理狀態。
- **階段 `2.2.2` 關聯總結**: 本階段實現了VRAM和RAM的協同管理，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **階段 `2.3.1` 關聯總結**: 本階段實現了 GPU 自適應引擎和 VRAM/RAM 協同管理器，用於音素級指定臉孔對嘴和 J/L-Cut 混音。
- **階段 `2.3.2` 關聯總結**: 本階段實現了 GPU 自適應引擎和 VRAM 與 RAM 協同管理器，用於提高視頻合成的效率和性能。
- **階段 `2.3.3` 關聯總結**: 本階段實現了 GPU 自適應引擎和 VRAM 記憶體管理，並在 MasterVideoAssembler 中整合了音素級指定臉孔對嘴、J/L-Cut 混音和視頻組裝功能，與父階段和其他模組進行了互動。
- **階段 `3.1.1` 關聯總結**: 本階段實現了從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息的類和方法，並保存到文件中。
- **階段 `3.1.2` 關聯總結**: 本階段實現了從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息的功能，並保存到文件中。
- **階段 `3.2.1` 關聯總結**: 本階段實現了 ModelMenuProvider 類，用於提供模型菜單和基礎連線介面，與數據庫管理器進行交互以獲取本地免費模型和商業API模型。
- **階段 `3.2.2` 關聯總結**: 本階段實現了模型菜單和基礎連接接口的類，通過調用數據庫管理器獲取本地免費模型和商業API模型。
- **階段 `4.1.1` 關聯總結**: 本階段實現了資料庫連線管理、項目資產與嵌入式數據的 ORM 模型，並定義了項目存档與恢復的介面。
- **階段 `4.1.2` 關聯總結**: 本階段實現了數據庫模型和管理器，用於存儲和操作項目資產及其嵌入數據，並提供了數據庫管理器和存档管理器的實現。
- **階段 `4.2.1` 關聯總結**: 本階段實現了 AssetEmbeddings 類別，用於處理資產嵌入向量的資料庫操作，包括創建、讀取、更新和刪除嵌入向量，並與 SQLite 資料庫進行互動。
- **階段 `4.2.2` 關聯總結**: 本階段實現了資產嵌入向量的資料庫操作，包括創建、讀取、更新和刪除嵌入向量，並與 SQLite 資料庫進行交互。
- **階段 `5.1.1` 關聯總結**: ShotPairNodeWidget 模組實現了圖形用戶介面的元素和功能，與父階段的 UI 設計和資料結構相連，並與其他模組進行互動以實現圖形化操作。
- **階段 `5.1.2` 關聯總結**: 本階段實現了圖形用戶界面的模組，與父階段和其他模組進行了互動，並與資料表無直接關聯。
- **階段 `5.2.1` 關聯總結**: 本階段實現了FrameContinuityEngine類，用於智慧最佳尾幀挑選、LAB色彩校正、時域去閃爍與羽化去背，並通過DBManager與數據庫進行交互。
- **階段 `5.2.2` 關聯總結**: 本階段實現了核心業務演算法，包括智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背，並通過 DBManager 類與數據庫進行交互。
- **階段 `5.2.3` 關聯總結**: 本階段實現了FrameContinuityEngine類，用於智慧最佳尾幀挑選、LAB色彩校正、時域去閃爍與羽化去背，並通過DBManager與數據庫進行交互。
- **階段 `5.3.1` 關聯總結**: 本階段實現了主視窗類別，包含頂部三視圖切換介面，與父階段和其他模組無直接互動，主要操作資料表為無
- **階段 `5.3.2` 關聯總結**: 本階段實現了硬體遙測狀態顯示功能，通過 `ui/main_window.py` 檔案中的 `MainWindow` 類和 `initHardwareMonitorTab` 方法，與父階段和其他模組互動，並通過 SQL 資料表進行數據存取。
- **階段 `5.4.1` 關聯總結**: 本階段實現了無邊際點陣畫布的模組，與父階段和其他模組進行了互動，並與資料表進行了關聯。
- **階段 `5.4.2` 關聯總結**: 本階段實現了無邊際點陣畫布的模組，與父階段和其他模組無直接關聯，主要與 UI 層互動。
- **階段 `5.5.1` 關聯總結**: 本階段實現了AssetContainerNode類，用於管理角色、場景和道具的資產容器，並與PC拖放沙盒上傳功能互動。
- **階段 `5.5.2` 關聯總結**: 本階段實現了AssetContainerNode類，用於管理角色、場景和道具的資產容器，並提供了添加、移除、獲取、排序、分類和搜索資產的功能。
- **階段 `5.6.1` 關聯總結**: 本階段實現了 ModelStoreDialog 類別，用於顯示和管理 model_store 資料表中的模型信息，並通過 DBManager 和 ModelStore 類與資料庫進行連接和數據交互。
- **階段 `5.6.2` 關聯總結**: ModelStoreDialog 類別用於顯示和管理 model_store 資料表中的模型信息，與 DBManager 和 ModelStore 模組互動，並通過 QTableView 顯示模型列表。
- **階段 `6.1.1` 關聯總結**: 本階段實現了NLE時間軸編輯器的UI組件，包括節點和連線的類別，以及編輯器的類別，這些組件與父階段的圖形處理和數據結構相關，並與其他模組進行互動以實現時間軸的編輯和顯示。
- **階段 `6.1.2` 關聯總結**: 本階段實現了NLE時間軸編輯器的核心邏輯，包括節點和連線的管理，以及編輯器的排序和自動連接功能。
- **階段 `6.2.1` 關聯總結**: 本階段實現了預算設置對話框的 UI 界面，與父階段和其他模組無直接關聯，主要操作資料表為 `budget_settings`。
- **階段 `6.2.2` 關聯總結**: 本階段實現了預算設置對話框的 UI 界面和基本功能，與父階段和其他模組無直接關聯，主要操作資料表為 `budget_settings`。
- **階段 `7.1.1` 關聯總結**: 本階段實現了智能體圖形數據結構的骨架，包括節點和邊的類別，以及圖形數據結構的管理方法，這些類別和方法將在後續的階段中與資料庫進行互動，實現智能體網絡的建模和管理。
- **階段 `7.1.2` 關聯總結**: 本階段實現了一個多智能體圖形數據結構，用於管理智能體節點和邊，並提供了添加、獲取和查詢節點和邊的功能。
- **階段 `7.2.1` 關聯總結**: 本階段實現了智能體長期記憶的管理功能，包括從資料庫加載、保存和检索記憶，與資料庫進行連線。
- **階段 `7.2.2` 關聯總結**: 本階段實現了智能體長期記憶的檢索、保存和检索功能，與資料庫進行交互以持久化記憶數據。
- **階段 `8.1.1` 關聯總結**: 本階段實現了 WorkflowRuntime 類，用於管理工作流任務的註冊、執行和狀態查詢，與父階段和其他模組無直接關聯，主要與資料表無直接互動。
- **階段 `8.1.2` 關聯總結**: 本階段實現了工作流任務管理的核心功能，包括任務註冊、執行和狀態查詢，與父階段和其他模組進行了互動。
- **階段 `8.2.1` 關聯總結**: 本階段實現了任務隊列的基礎結構，包括任務狀態枚舉、任務類和任務隊列類，用於管理任務的添加、移除和處理。
- **階段 `8.2.2` 關聯總結**: 本階段實現了任務處理與優先級管理的模組，與父階段和其他模組無直接互動，主要操作任務隊列和任務狀態。
- **階段 `8.2.3` 關聯總結**: 本階段實現了任務隊列的管理功能，包括任務的添加、執行和移除，與父階段和其他模組進行了互動。
- **階段 `9.1.1` 關聯總結**: 本階段實現了影視體裁時間結構設定的資料結構與類別骨架，與父階段和其他模組無直接互動，主要用於管理影視作品的時間配置。
- **階段 `9.1.2` 關聯總結**: 本階段實現了影視體裁時間結構設定的配置，與父階段和其他模組無直接互動，主要與資料表無關聯。
- **階段 `9.1.3` 關聯總結**: 本階段實現了影視體裁時間結構設定的配置，與父階段和相關模組進行了互動，並通過SQL資料表進行數據持久化。
- **階段 `10.1.1` 關聯總結**: 本階段實現了 CanvasEdge 類別，用於定義畫布邊的屬性和方法，並提供了對邊的增刪改查操作。
- **階段 `10.1.2` 關聯總結**: 本階段實現了CanvasEdge類別，用於定義畫布邊的屬性和方法，並提供了對邊的增刪改查操作。
- **階段 `13.1.1` 關聯總結**: 本階段實現了 BudgetRule 類別，用於管理單專案預算規則，並提供了從資料庫讀取和寫入預算規則的功能。
- **階段 `13.1.2` 關聯總結**: 本階段實現了預算規則的管理類別，與資料庫進行互動，進行預算規則的讀取和寫入。
- **階段 `14.1.1` 關聯總結**: 本階段實現了 WorkflowCheckpoint 類別，用於管理工作流程的檢查點，包括保存和加載檢查點，並與 SQLite 數據庫進行交互。
- **階段 `14.1.2` 關聯總結**: 本階段實現了 WorkflowCheckpoint 類別，用於管理工作流程的檢查點，包括保存和加載檢查點，並與 SQLite 數據庫進行交互。
- **階段 `15.1.1` 關聯總結**: 本階段實現了三個模組（users.py, roles.py, permissions.py）來處理權限資料庫操作，每個模組都包含連接、斷開連接、創建表、插入、查詢、更新和刪除權限的功能，並與 permissions 資料表進行互動。
- **階段 `15.1.2` 關聯總結**: 本階段實現了權限管理功能，通過三個模組（users.py, roles.py, permissions.py）與SQLite資料庫進行互動，實現了權限的創建、查詢、更新和刪除。
