# 🗺️ 專案全域程式碼、Function 與資料表關聯註冊表 (Architecture Registry)
> 最後自動更新時間：2026-11-09 11:23:44
> **核心規範**：推理與編程模型在實作任何階段時，必須查閱本註冊表的『資料表欄位』、『跨階段模組介面』與『Function 簽章』，確保命名與參數型別 100% 吻合。

## 1. 🗄️ 資料表結構與存取關聯 (Database Tables & CRUD Mapping)
### 資料表 `archive_log`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 存儲專案版本快照的資料表，包含 project_id 和 snapshot_data 字段。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_archive(), database/project_archiver.py::ProjectArchiver.restore_archive(), database/project_assets.py::ProjectArchiver.restore_archive()`

### 資料表 `asset_embeddings`
- **定義檔案**: `database/asset_embeddings.py` | **用途註記**: 此資料表存儲資產嵌入向量的相關信息，包括資產 ID、嵌入向量、創建和更新時間等。
- **欄位結構**: `asset_id (TEXT), embedding (BLOB), created_at (TIMESTAMP)`
- **關聯存取函數 (Read/Write)**: `database/asset_embeddings.py::AssetEmbeddings.create_embedding(), database/asset_embeddings.py::AssetEmbeddings.get_embedding(), database/asset_embeddings.py::AssetEmbeddings.update_embedding(), database/asset_embeddings.py::AssetEmbeddings.delete_embedding()`

### 資料表 `frames`
- **定義檔案**: `Stage 5.1.1` | **用途註記**: 此資料表用於存儲影像處理任務的各幀影像數據，與 FrameContinuityEngine 類中的方法進行互動。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `model_store`
- **定義檔案**: `未知` | **用途註記**: 此資料表的業務用途是存儲模型信息，包括模型的免費狀態，關聯的函數為fetch_free_local_models和fetch_commercial_api_models。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `core/model_menu_provider.py::ModelMenuProvider.fetch_free_local_models(), core/model_menu_provider.py::ModelMenuProvider.fetch_commercial_api_models()`

### 資料表 `project_assets`
- **定義檔案**: `Stage 4.1.1` | **用途註記**: 此資料表存儲項目資產的相關信息，包括項目 ID、資產類型、路徑、創建和更新時間等。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `project_info`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 存儲 .omni_pack 打包的資料表，包含 project_id 和 pack_data 字段。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_project_pack(), database/project_archiver.py::ProjectArchiver.restore_project_pack()`

### 資料表 `projects`
- **定義檔案**: `Stage 4.1.1` | **用途註記**: 此資料表存儲項目的基本信息，包括項目 ID、項目名稱、格式預設 ID、寬高比、目標解析度、帧率、全局 LUT 路徑、默認 CJK 字體路徑、創建和更新時間等。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `settings`
- **定義檔案**: `Stage 1.1.1` | **用途註記**: 設置表，存儲系統設置，關聯於數據庫連線初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_1`
- **定義檔案**: `未知` | **用途註記**: 此資料表用於示例，包含 'id' 和 'name' 欄位，並在 Auto-Migration 中添加了 'new_column' 欄位。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/db_manager.py::DBManager.auto_migration()`

### 資料表 `users`
- **定義檔案**: `Stage 1.1.1` | **用途註記**: 用戶表，存儲用戶信息，關聯於數據庫連線初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `vector_index_table`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 此資料表用於存儲向量及其ID，用於向量索引引擎的數據庫操作。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/vector_index_engine.py::VectorIndexEngine.load_index(), database/vector_index_engine.py::VectorIndexEngine.insert_vector(), database/vector_index_engine.py::VectorIndexEngine.delete_vector()`

## 2. 📦 程式模組、類別與 Function 關聯索引 (Modules & Symbol Map)
### 📄 `core/frame_continuity_engine.py` (所屬階段: `5.1.2`)
- **模組職責註記**: 此檔案實現了核心業務演算法，包括智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), database.db_manager:(DBManager)`
  - **Class `FrameContinuityEngine`**: 智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背
    - `def __init__(self, db_manager: DBManager)` ➔ 初始化 FrameContinuityEngine 类
    - `def select_best_last_frame(self, frames: List[Dict]) -> Optional[Dict]` ➔ 選擇最佳尾幀，輸入為帧列表，輸出為最佳尾幀。
    - `def match_histograms(self, frame1: Dict, frame2: Dict) -> float` ➔ 進行 LAB 色彩校正，輸入為兩帧，輸出為色彩匹配度。
    - `def temporal_deflicker(self, frames: List[Dict]) -> List[Dict]` ➔ 進行時域去閃爍與羽化去背，輸入為帧列表，輸出為處理後的帧列表。

### 📄 `core/gpu_auto_profiler.py` (所屬階段: `2.1.2`)
- **模組職責註記**: 此檔案的核心職責是實現 GPU 自適應引擎的基礎架構，包括初始化 GPU 資訊、獲取 GPU 資訊、配置運算精度和記憶體管理。
- **依賴引用 (Imports)**: `torch, pynvml, typing:(Dict, Optional)`
  - **Class `NvidiaProfiler`**: NvidiaProfiler: GPU 自適應引擎的基礎架構
    - `def __init__(self)` ➔ 初始化 GPU 資訊
    - `def initialize(self) -> None` ➔ 初始化 GPU 資訊，使用 pynvml 初始化並獲取 GPU 數量和屬性。 | 🔗 呼叫: `nvmlInit, nvmlDeviceGetCount, nvmlDeviceGetProperties`
    - `def get_device_info(self) -> Dict` ➔ 獲取 GPU 資訊，如果尚未初始化則調用 initialize 方法。 | 🔗 呼叫: `initialize`
    - `def configure_precision(self) -> None` ➔ 根據 GPU 的計算能力配置運算精度，以利於高效計算。 | 🔗 呼叫: `get_device_info, set_default_tensor_type`
    - `def configure_memory_management(self) -> None` ➔ 根據 GPU 的記憶體容量配置記憶體管理策略，以利於高效記憶體使用。 | 🔗 呼叫: `get_device_info, set_device, empty_cache`

### 📄 `core/model_menu_provider.py` (所屬階段: `3.2.2`)
- **模組職責註記**: 此檔案的核心職責是提供模型菜單和基礎連接接口，通過DBManager與數據庫進行交互，獲取本地免費和商業API模型。
- **依賴引用 (Imports)**: `typing:(List, Dict), database.db_manager:(DBManager)`
  - **Class `ModelMenuProvider`**: ModelMenuProvider: 提供模型菜单和基础连接接口的类
    - `def __init__(self, db_manager: DBManager)` ➔ 初始化 ModelMenuProvider 类
    - `def fetch_free_local_models(self) -> List[Dict]` ➔ 此函數的功能是獲取本地免費模型，輸入無，輸出為本地免費模型列表，操作的資料表為model_store。 | 🗄️ 資料表: `model_store` | 🔗 呼叫: `execute_query`
    - `def fetch_commercial_api_models(self) -> List[Dict]` ➔ 此函數的功能是獲取商業API模型，輸入無，輸出為商業API模型列表，操作的資料表為model_store。 | 🗄️ 資料表: `model_store` | 🔗 呼叫: `execute_query`

### 📄 `core/model_store_crawler.py` (所屬階段: `3.1.2`)
- **模組職責註記**: 此檔案的核心職責是從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息，並提供對外介面來獲取和保存模型數據。
- **依賴引用 (Imports)**: `requests, typing:(List, Dict, Optional)`
  - **Class `ModelStoreCrawler`**: ModelStoreCrawler: 用于从 Hugging Face Hub 和 Civitai v1 API 获取模型信息的类
    - `def __init__(self, hf_token: Optional[str], civitai_token: Optional[str])` ➔ 初始化 ModelStoreCrawler 类
    - `def fetch_models(self, hf_repo: str, civitai_category: str) -> List[Dict]` ➔ 從 Hugging Face Hub 和 Civitai v1 API 获取模型信息，並返回模型信息列表。 | 🔗 呼叫: `_fetch_hf_models, _fetch_civitai_models`
    - `def parse_model_info(self, model_info: Dict) -> Dict` ➔ 解析模型信息，返回解析後的模型信息字典。
    - `def save_models(self, models: List[Dict], save_path: str) -> None` ➔ 將模型信息保存到文件中。 | 🔗 呼叫: `write`
    - `def _fetch_hf_models(self, repo: str) -> List[Dict]` ➔ 從 Hugging Face Hub 获取模型信息，返回模型信息列表。 | 🔗 呼叫: `get, raise_for_status, json`
    - `def _fetch_civitai_models(self, category: str) -> List[Dict]` ➔ 從 Civitai v1 获取模型信息，返回模型信息列表。 | 🔗 呼叫: `get, raise_for_status, json`

### 📄 `core/multi_agent_graph.py` (所屬階段: `7.1.1`)
- **模組職責註記**: 此檔案定義了多智能體協同圖形數據庫的基礎結構，包括智能體節點和邊的類別，以及對圖形數據庫的增刪改查操作。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional)`
  - **Class `AgentNode`**: 智能體節點類別
    - `def __init__(self, node_id: str, node_type: str)` ➔ 待推理模型或開發者補充註記
  - **Class `Edge`**: 边類別
    - `def __init__(self, edge_id: str, source_node: AgentNode, target_node: AgentNode)` ➔ 待推理模型或開發者補充註記
  - **Class `MultiAgentGraph`**: 多智能體協同圖形數據庫類別
    - `def __init__(self)` ➔ 待推理模型或開發者補充註記
    - `def add_node(self, node: AgentNode)` ➔ 添加智能體節點 | 🔗 呼叫: `append`
    - `def add_edge(self, edge: Edge)` ➔ 添加邊 | 🔗 呼叫: `append`
    - `def get_node(self, node_id: str) -> Optional[AgentNode]` ➔ 根據節點ID獲取智能體節點
    - `def get_edges(self, node_id: str) -> List[Edge]` ➔ 根據節點ID獲取所有連接的邊
    - `def remove_node(self, node_id: str)` ➔ 根據節點ID移除智能體節點
    - `def remove_edge(self, edge_id: str)` ➔ 根據邊ID移除邊

### 📄 `core/vram_ram_hybrid_manager.py` (所屬階段: `2.2.2`)
- **模組職責註記**: 此檔案實現了VRAM和RAM的協同管理，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **依賴引用 (Imports)**: `sqlite3, typing:(Dict, Optional)`
  - **Class `VRAMRAMHybridManager`**: VRAM 和 RAM 協同管理器
    - `def __init__(self, vram_buffer_size: int, pinned_memory_pool: int)` ➔ 初始化VRAM和RAM協同管理器，設置VRAM緩衝區大小和固定內存池大小。
    - `def initialize(self)` ➔ 初始化VRAM和RAM協同管理器的邏輯。
    - `def upload_to_vram(self, data: bytes)` ➔ 將數據上傳到VRAM，如果VRAM緩衝區已滿則拋出異常。 | 🔗 呼叫: `ValueError`
    - `def release_from_vram(self, data: bytes)` ➔ 從VRAM釋放數據，減少VRAM使用情況。
    - `def get_vram_usage(self) -> int` ➔ 獲取當前VRAM的使用情況。

### 📄 `database/asset_embeddings.py` (所屬階段: `4.1.2`)
- **模組職責註記**: 此檔案定義了資產嵌入向量的數據庫操作，包括創建、讀取、更新和刪除嵌入向量。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional), sqlite3`
  - **Class `AssetEmbeddings`**: 類別 AssetEmbeddings 用於處理資產嵌入向量的資料庫操作。
    - `def __init__(self, db_path: str)` ➔ 初始化 AssetEmbeddings 類別。 | 🔗 呼叫: `connect, cursor, _create_table`
    - `def _create_table(self)` ➔ 創建 asset_embeddings 資料表。 | 🔗 呼叫: `execute, commit`
    - `def create_embedding(self, asset_id: str, embedding: bytes)` ➔ 創建一個新的資產嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def get_embedding(self, asset_id: str) -> Optional[bytes]` ➔ 讀取一個資產的嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, fetchone`
    - `def update_embedding(self, asset_id: str, embedding: bytes)` ➔ 更新一個資產的嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def delete_embedding(self, asset_id: str)` ➔ 刪除一個資產的嵌入向量。 | 🗄️ 資料表: `asset_embeddings` | 🔗 呼叫: `execute, commit`
    - `def close(self)` ➔ 關閉資料庫連線。 | 🔗 呼叫: `close`

### 📄 `database/db_manager.py` (所屬階段: `1.1.1`)
- **模組職責註記**: 此檔案管理數據庫連接，包括創建數據庫引擎和獲取數據庫會話。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional), contextlib:(contextmanager)`
  - **Class `DBManager`**: SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
    - `def __init__(self, db_path: str)` ➔ 初始化 SQLite WAL 連線池
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取 SQLite 連線，並在使用後將連線放回池中。 | 🔗 呼叫: `pop, connect, append`
    - `def init_tables(self)` ➔ 初始化 26 張表，如果表不存在則創建。 | 🔗 呼叫: `get_connection, cursor, commit, execute`
    - `def auto_migration(self)` ➔ 自動升級資料庫結構，添加新欄位並更新用戶版本。 | 🗄️ 資料表: `table_1` | 🔗 呼叫: `get_connection, cursor, execute, fetchone, commit`
    - `def rolling_backup(self)` ➔ 進行資料庫滾動備份，將當前資料庫備份到 'backup.db'。 | 🔗 呼叫: `get_connection, cursor, execute, commit`

### 📄 `database/project_archiver.py` (所屬階段: `1.1.3`)
- **模組職責註記**: 此檔案實現了項目存档和恢復的功能，包括創建和恢復存档。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple), contextlib:(contextmanager)`
  - **Class `ProjectArchiver`**: 專案版本快照與 .omni_pack 打包匯出/還原器
    - `def __init__(self, db_path: str)` ➔ 初始化 ProjectArchiver | 🔗 呼叫: `DBManager`
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取連線 | 🔗 呼叫: `get_connection`
    - `def create_archive(self, project_id: int, snapshot_data: dict)` ➔ 創建專案版本快照，將快照數據插入到 archive_log 資料表中。 | 🗄️ 資料表: `archive_log` | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def restore_archive(self, archive_id: int)` ➔ 復原專案版本快照，從 archive_log 資料表中讀取快照數據。 | 🗄️ 資料表: `archive_log` | 🔗 呼叫: `get_connection, cursor, execute, commit, fetchone`
    - `def create_project_pack(self, project_id: int, pack_data: dict)` ➔ 創建 .omni_pack 打包，將打包數據插入到 project_info 資料表中。 | 🗄️ 資料表: `project_info` | 🔗 呼叫: `get_connection, cursor, execute, commit`
    - `def restore_project_pack(self, project_id: int)` ➔ 復原 .omni_pack 打包，從 project_info 資料表中讀取打包數據。 | 🗄️ 資料表: `project_info` | 🔗 呼叫: `get_connection, cursor, execute, commit, fetchone`

### 📄 `database/project_assets.py` (所屬階段: `4.1.2`)
- **模組職責註記**: 此檔案定義了項目資產的數據庫模型，包括項目資產和項目之間的關聯。
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

### 📄 `database/vector_index_engine.py` (所屬階段: `1.1.2`)
- **模組職責註記**: 此檔案實現了一個向量索引引擎，主要功能包括初始化、加載索引、插入向量、查詢向量和刪除向量。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional, Tuple), hnswlib:(HierarchicalNSW), numpy`
  - **Class `VectorIndexEngine`**: sqlite-vec / HNSW 毫秒級資產向量檢索器
    - `def __init__(self, db_path: str, index_path: str)` ➔ 初始化向量索引引擎，設置資料庫和索引路徑，加載索引。 | 🔗 呼叫: `load_index`
    - `def load_index(self)` ➔ 加載HNSW索引，從SQLite資料庫中讀取向量數據並添加到索引中。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `HierarchicalNSW, load_index, get_connection, cursor, execute, fetchall, append, add_item`
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取SQLite連線。 | 🔗 呼叫: `DBManager, get_connection`
    - `def insert_vector(self, vector: np.ndarray, vector_id: int)` ➔ 插入向量到SQLite資料庫和HNSW索引中。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `add_item, append, get_connection, cursor, execute, commit, tobytes`
    - `def search_vector(self, vector: np.ndarray, k: int) -> List[Tuple[int, float]]` ➔ 查詢最接近的向量及其距離。 | 🔗 呼叫: `search_knn`
    - `def delete_vector(self, vector_id: int)` ➔ 從SQLite資料庫和HNSW索引中刪除向量。 | 🗄️ 資料表: `vector_index_table` | 🔗 呼叫: `delete_item, remove, get_connection, cursor, execute, commit`

## 3. 📝 各階段完成後之推理模型語意與關聯總結 (Stage Post-Coding Semantic Notes)
- **階段 `1.1.1` 關聯總結**: 本階段實現了 SQLite WAL 連線池、26 張表的初始化、Auto-Migration 與滾動備份功能，與父階段和其他模組進行了資料庫連線和初始化的協調。
- **階段 `1.1.2` 關聯總結**: 本階段實現了一個向量索引引擎，與SQLite資料庫和HNSW索引庫互動，進行向量的插入、查詢和刪除操作。
- **階段 `1.1.3` 關聯總結**: 本階段實現了專案版本快照與打包的相關功能，通過 ProjectArchiver 類與 DBManager 類進行資料庫操作，與父階段和其他模組進行互動，並與資料表 archive_log 和 project_info 進行關聯。
- **階段 `2.1.1` 關聯總結**: 本階段實現了 GPU 自適應引擎的基础架构，包括初始化 GPU 信息、获取 GPU 信息、配置运算精度和配置内存管理，并与父阶段和相关模块进行交互。
- **階段 `2.1.2` 關聯總結**: 本階段實現了 GPU 自適應引擎的核心功能，包括初始化 GPU 資訊、獲取 GPU 資訊、配置運算精度和記憶體管理，這些功能與父階段和其他模組互動，以實現高效的 GPU 計算資源管理。
- **階段 `2.2.1` 關聯總結**: 本階段實現了VRAM和RAM協同管理器，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **階段 `2.2.2` 關聯總結**: 本階段實現了VRAM和RAM的協同管理，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **階段 `3.1.1` 關聯總結**: 本階段實現了 ModelStoreCrawler 類，用於從 Hugging Face Hub 和 Civitai v1 API 獲取模型信息，並進行解析和保存。
- **階段 `3.1.2` 關聯總結**: 本階段實現了從 Hugging Face Hub 和 Civitai v1 API 爬取模型信息的模組，並提供了對外介面來獲取和保存模型數據。
- **階段 `3.2.1` 關聯總結**: 本階段實現了 ModelMenuProvider 類，用於提供模型菜單和基礎連線介面，與數據庫管理器進行交互以獲取本地免費模型和商業API模型。
- **階段 `3.2.2` 關聯總結**: 本階段實現了ModelMenuProvider類，用於從model_store資料表中獲取本地免費和商業API模型，並通過DBManager與數據庫進行交互。
- **階段 `4.1.1` 關聯總結**: 本階段實現了資料庫連線管理、資產和嵌入向量的數據模型定義，以及基本的數據庫操作功能。
- **階段 `4.1.2` 關聯總結**: 本階段實現了數據庫連接管理、項目資產和嵌入向量的數據庫操作，並與父階段的數據庫設計和核心業務邏輯進行了整合。
- **階段 `5.1.1` 關聯總結**: 本階段實現了 FrameContinuityEngine 類，用於智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背，並通過 DBManager 類與數據庫進行交互。
- **階段 `5.1.2` 關聯總結**: 本階段實現了核心業務演算法，包括智慧最佳尾幀挑選、LAB 色彩校正、時域去閃爍與羽化去背，並通過 DBManager 与資料庫互動。
- **階段 `7.1.1` 關聯總結**: 本階段實現了多智能體協同圖形數據庫的基礎結構，包括智能體節點和邊的類別，以及對圖形數據庫的增刪改查操作。
