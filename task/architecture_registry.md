# 🗺️ 專案全域程式碼、Function 與資料表關聯註冊表 (Architecture Registry)
> 最後自動更新時間：2026-11-09 11:07:29
> **核心規範**：推理與編程模型在實作任何階段時，必須查閱本註冊表的『資料表欄位』、『跨階段模組介面』與『Function 簽章』，確保命名與參數型別 100% 吻合。

## 1. 🗄️ 資料表結構與存取關聯 (Database Tables & CRUD Mapping)
### 資料表 `archive_log`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表存儲項目存档和恢復的日誌，包括存档ID、項目ID、存档時間、恢復時間等。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `project_info`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 此資料表存儲項目的基本信息，包括項目ID、項目名稱、項目描述等。
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
### 📄 `database/db_manager.py` (所屬階段: `1.1.1`)
- **模組職責註記**: 此檔案實現了 SQLite WAL 連線池、26 張表的初始化、Auto-Migration 與滾動備份功能，並提供了對外介面進行資料庫操作。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional), contextlib:(contextmanager)`
  - **Class `DBManager`**: SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
    - `def __init__(self, db_path: str)` ➔ 初始化 SQLite WAL 連線池
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取 SQLite 連線，並在使用後將連線放回池中。 | 🔗 呼叫: `pop, connect, append`
    - `def init_tables(self)` ➔ 初始化 26 張表，如果表不存在則創建。 | 🔗 呼叫: `get_connection, cursor, commit, execute`
    - `def auto_migration(self)` ➔ 自動升級資料庫結構，添加新欄位並更新用戶版本。 | 🗄️ 資料表: `table_1` | 🔗 呼叫: `get_connection, cursor, execute, fetchone, commit`
    - `def rolling_backup(self)` ➔ 進行資料庫滾動備份，將當前資料庫備份到 'backup.db'。 | 🔗 呼叫: `get_connection, cursor, execute, commit`

### 📄 `database/project_archiver.py` (所屬階段: `1.1.3`)
- **模組職責註記**: 此檔案的核心職責是實現數據庫項目存档功能，提供對外介面進行存档操作。

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
- **階段 `1.1.3` 關聯總結**: 本階段實現了數據庫項目存档功能，與父階段和相關模組進行了交互，並與資料表進行了關聯。
