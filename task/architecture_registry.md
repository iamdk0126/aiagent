# 🗺️ 專案全域程式碼、Function 與資料表關聯註冊表 (Architecture Registry)
> 最後自動更新時間：2026-11-09 12:55:03
> **核心規範**：推理與編程模型在實作任何階段時，必須查閱本註冊表的『資料表欄位』、『跨階段模組介面』與『Function 簽章』，確保命名與參數型別 100% 吻合。

## 1. 🗄️ 資料表結構與存取關聯 (Database Tables & CRUD Mapping)
### 資料表 `N/A`
- **定義檔案**: `Stage 2.3.3` | **用途註記**: 本階段的程式碼未涉及任何資料表。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `agent_nodes`
- **定義檔案**: `Stage 7.1.2` | **用途註記**: 此資料表存儲智能體節點的資訊，包括節點ID和節點類型。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `archive_log`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 存儲專案版本快照的資料表，包含 project_id 和 snapshot_data 欄位。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_archive(), database/project_archiver.py::ProjectArchiver.restore_archive(), database/project_assets.py::ProjectArchiver.restore_archive()`

### 資料表 `asset_embeddings`
- **定義檔案**: `database/asset_embeddings.py` | **用途註記**: 此資料表用於存儲資產的嵌入向量，包含 asset_id、embedding 和 created_at 字段。
- **欄位結構**: `asset_id (TEXT), embedding (BLOB), created_at (TIMESTAMP)`
- **關聯存取函數 (Read/Write)**: `database/asset_embeddings.py::AssetEmbeddings.create_embedding(), database/asset_embeddings.py::AssetEmbeddings.get_embedding(), database/asset_embeddings.py::AssetEmbeddings.update_embedding(), database/asset_embeddings.py::AssetEmbeddings.delete_embedding()`

### 資料表 `budget_rules`
- **定義檔案**: `Stage 13.1.1` | **用途註記**: 此資料表用於存儲各專案的預算規則，包括最大單鏡預算、最大單集預算、最大單專案預算、目前專案已支出和是否自動切換到本地免費模型等信息。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `canvas_edges`
- **定義檔案**: `Stage 10.1.1` | **用途註記**: 此資料表用於存儲畫布上的邊，包含邊的唯一識別符、源節點識別符和目標節點識別符。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `edges`
- **定義檔案**: `Stage 7.1.2` | **用途註記**: 此資料表用於存儲畫布邊的數據，包括邊的唯一識別符、源節點識別符和目標節點識別符。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `frame_table`
- **定義檔案**: `Stage 5.2.1` | **用途註記**: 此資料表用於存儲フレーム的相關信息，包括帧的時間戳、圖像數據等，與 FrameContinuityEngine 中的函數進行交互。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `frames`
- **定義檔案**: `Stage 5.1.1` | **用途註記**: 此資料表用於存儲影像處理任務的各幀影像數據，與 FrameContinuityEngine 類中的方法進行互動。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `histogram_table`
- **定義檔案**: `Stage 5.2.1` | **用途註記**: 此資料表用於存儲色彩直方圖的相關信息，包括色彩直方圖的數據等。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `model_store`
- **定義檔案**: `未知` | **用途註記**: 此資料表的業務用途是存儲模型信息，包括模型的免費狀態，關聯說明為ModelMenuProvider類通過調用數據庫管理器獲取本地免費模型和商業API模型。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `core/model_menu_provider.py::ModelMenuProvider.fetch_free_local_models(), core/model_menu_provider.py::ModelMenuProvider.fetch_commercial_api_models()`

### 資料表 `permissions`
- **定義檔案**: `database/permissions.py` | **用途註記**: 此資料表用於存儲權限相關的數據，包括權限ID、權限名稱和描述。
- **欄位結構**: `permission_id (TEXT), permission_name (TEXT), description (TEXT)`
- **關聯存取函數 (Read/Write)**: `database/users.py::Permission.insert_permission(), database/users.py::Permission.get_permission(), database/users.py::Permission.update_permission(), database/users.py::Permission.delete_permission(), database/users.py::Permission.get_all_permissions(), database/roles.py::Permission.insert_permission(), database/roles.py::Permission.get_permission(), database/roles.py::Permission.update_permission(), database/roles.py::Permission.delete_permission(), database/roles.py::Permission.get_all_permissions(), database/permissions.py::Permission.insert_permission(), database/permissions.py::Permission.get_permission(), database/permissions.py::Permission.update_permission(), database/permissions.py::Permission.delete_permission(), database/permissions.py::Permission.get_all_permissions()`

### 資料表 `project_assets`
- **定義檔案**: `Stage 4.1.1` | **用途註記**: 存儲項目資產的數據，包括項目ID、資產類型、路徑、創建和更新時間等字段。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `project_info`
- **定義檔案**: `Stage 1.1.3` | **用途註記**: 存儲 .omni_pack 打包的資料表，包含 project_id 和 pack_data 欄位。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/project_archiver.py::ProjectArchiver.create_project_pack(), database/project_archiver.py::ProjectArchiver.restore_project_pack()`

### 資料表 `projects`
- **定義檔案**: `Stage 4.1.1` | **用途註記**: 存儲項目的基本信息，包括項目ID、項目名稱、格式預設ID、寬高比、目標解析度、帧率、全局LUT路徑、默認CJK字體路徑、創建和更新時間等字段。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `settings`
- **定義檔案**: `Stage 1.1.1` | **用途註記**: 設置表，存儲系統設置，關聯於數據庫連線初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_1`
- **定義檔案**: `未知` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化和自動升級。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `database/db_manager.py::DBManager.auto_migration()`

### 資料表 `table_10`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_11`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_12`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_13`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_14`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_15`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_16`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_17`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_18`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_19`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_2`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_20`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_21`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_22`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_23`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_24`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_25`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_26`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_3`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_4`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_5`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_6`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_7`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_8`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
- **關聯存取函數 (Read/Write)**: `尚無函數直接存取`

### 資料表 `table_9`
- **定義檔案**: `Stage 1.1.2` | **用途註記**: 包含id和name字段，用於示例數據庫表的初始化。
- **欄位結構**: `(欄位待補充)`
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

### 📄 `core/vram_ram_hybrid_manager.py` (所屬階段: `2.2.2`)
- **模組職責註記**: 此檔案實現了VRAM和RAM的協同管理，通過初始化、上傳和釋放數據來管理VRAM的使用情況。
- **依賴引用 (Imports)**: `sqlite3, typing:(Dict, Optional)`
  - **Class `VRAMRAMHybridManager`**: VRAM 和 RAM 協同管理器
    - `def __init__(self, vram_buffer_size: int, pinned_memory_pool: int)` ➔ 初始化VRAM和RAM協同管理器，設置VRAM緩衝區大小和固定內存池大小。
    - `def initialize(self)` ➔ 初始化VRAM和RAM協同管理器的邏輯。
    - `def upload_to_vram(self, data: bytes)` ➔ 將數據上傳到VRAM，如果VRAM緩衝區已滿則拋出異常。 | 🔗 呼叫: `ValueError`
    - `def release_from_vram(self, data: bytes)` ➔ 從VRAM釋放數據。
    - `def get_vram_usage(self) -> int` ➔ 獲取VRAM的使用情況。

### 📄 `core/workflow_runtime.py` (所屬階段: `9.1.2`)
- **模組職責註記**: 此檔案的核心職責是管理工作流任務的註冊、執行和狀態查詢，提供對外介面進行任務管理。
- **依賴引用 (Imports)**: `typing:(List, Dict, Optional)`
  - **Class `WorkflowRuntime`**: WorkflowRuntime: 管理工作流任务的类
    - `def __init__(self)` ➔ 初始化 WorkflowRuntime 类
    - `def register_task(self, task_id: str, task_function)` ➔ 註冊任務，將任務ID和任務函數存儲在 tasks 字典中。
    - `def execute_task(self, task_id: str)` ➔ 執行指定ID的任務，返回任務執行結果，如果任務不存在則拋出 ValueError。 | 🔗 呼叫: `ValueError`
    - `def get_task_status(self, task_id: str) -> Optional[str]` ➔ 查詢指定ID的任務狀態，如果任務存在則返回 'Running'，否則返回 None。

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

### 📄 `database/db_manager.py` (所屬階段: `1.1.2`)
- **模組職責註記**: 此檔案實現了數據庫管理器，用於創建數據庫連接和獲取數據庫會話。
- **依賴引用 (Imports)**: `sqlite3, typing:(List, Optional), contextlib:(contextmanager)`
  - **Class `DBManager`**: SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
    - `def __init__(self, db_path: str)` ➔ 初始化數據庫管理器，創建數據庫連接和元數據。
    - `def get_connection(self) -> sqlite3.Connection` ➔ 從連線池獲取SQLite連線，並在使用後返回連線池。 | 🔗 呼叫: `pop, connect, append`
    - `def init_tables(self)` ➔ 初始化26張表，每張表包含id和name字段。 | 🔗 呼叫: `get_connection, cursor, commit, execute`
    - `def auto_migration(self)` ➔ 自動升級數據庫結構，添加新列new_column到table_1。 | 🗄️ 資料表: `table_1` | 🔗 呼叫: `get_connection, cursor, execute, fetchone, commit`
    - `def rolling_backup(self)` ➔ 進行數據庫滾動備份，將當前數據庫備份到backup.db | 🔗 呼叫: `get_connection, cursor, execute, commit`

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

### 📄 `ui/canvas/asset_container_node.py` (所屬階段: `5.5.1`)
- **模組職責註記**: 此檔案定義了AssetContainerNode類，用於管理資產容器，並提供添加、移除和獲取資產的方法。
- **依賴引用 (Imports)**: `typing:(List, Optional)`
  - **Class `AssetContainerNode`**: 角色(藍)/場景(綠)/道具(黃) 資產容器與 PC 拖放沙盒上傳
    - `def __init__(self, asset_type: str, asset_name: str, asset_path: str)` ➔ 初始化AssetContainerNode類，設置資產類型、名稱和路徑，並初始化資產列表。
    - `def add_asset(self, asset: str) -> None` ➔ 向資產列表中添加一個資產。 | 🔗 呼叫: `append`
    - `def remove_asset(self, asset: str) -> None` ➔ 從資產列表中移除一個資產。 | 🔗 呼叫: `remove`
    - `def get_assets(self) -> List[str]` ➔ 返回所有資產的列表。
    - `def get_asset_info(self, asset_name: str) -> Optional[str]` ➔ 獲取指定資產的資訊。

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
- **階段 `1.1.1` 關聯總結**: 本階段實現了 SQLite WAL 連線池、26 張表初始化、Auto-Migration 與滾動備份功能，與父階段和其他模組進行了資料庫連線和操作的互動。
- **階段 `1.1.2` 關聯總結**: 本階段實現了數據庫管理模組，包括連線池、表初始化、自動升級和滾動備份功能，與父階段和其他模組進行了數據庫連接和操作的互動。
- **階段 `1.1.3` 關聯總結**: 本階段實現了專案版本快照與打包的相關功能，通過 ProjectArchiver 類與 DBManager 類進行資料庫操作，與父階段和其他模組進行互動，並與資料表 archive_log 和 project_info 進行關聯。
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
- **階段 `7.1.1` 關聯總結**: 本階段實現了多智能體協同圖形數據庫的基礎結構，包括智能體節點和邊的類別，以及對圖形數據庫的增刪改查操作。
- **階段 `7.1.2` 關聯總結**: 本階段實現了多智能體協同圖形數據庫的模組，與父階段和其他模組進行了互動，並與資料表進行了關聯。
- **階段 `9.1.1` 關聯總結**: 本階段實現了 WorkflowRuntime 類，用於管理工作流任務的註冊、執行和狀態查詢，與父階段和其他模組無直接關聯，主要與資料表無直接互動。
- **階段 `9.1.2` 關聯總結**: 本階段實現了 WorkflowRuntime 類，用於管理工作流任務的註冊、執行和狀態查詢，與父階段和其他模組無直接關聯，主要與資料表無關聯。
- **階段 `10.1.1` 關聯總結**: 本階段實現了 CanvasEdge 類別，用於定義畫布邊的屬性和方法，並提供了對邊的增刪改查操作。
- **階段 `10.1.2` 關聯總結**: 本階段實現了CanvasEdge類別，用於定義畫布邊的屬性和方法，並提供了對邊的增刪改查操作。
- **階段 `13.1.1` 關聯總結**: 本階段實現了 BudgetRule 類別，用於管理單專案預算規則，並提供了從資料庫讀取和寫入預算規則的功能。
- **階段 `13.1.2` 關聯總結**: 本階段實現了預算規則的管理類別，與資料庫進行互動，進行預算規則的讀取和寫入。
- **階段 `14.1.1` 關聯總結**: 本階段實現了 WorkflowCheckpoint 類別，用於管理工作流程的檢查點，包括保存和加載檢查點，並與 SQLite 數據庫進行交互。
- **階段 `14.1.2` 關聯總結**: 本階段實現了 WorkflowCheckpoint 類別，用於管理工作流程的檢查點，包括保存和加載檢查點，並與 SQLite 數據庫進行交互。
- **階段 `15.1.1` 關聯總結**: 本階段實現了三個模組（users.py, roles.py, permissions.py）來處理權限資料庫操作，每個模組都包含連接、斷開連接、創建表、插入、查詢、更新和刪除權限的功能，並與 permissions 資料表進行互動。
- **階段 `15.1.2` 關聯總結**: 本階段實現了權限管理功能，通過三個模組（users.py, roles.py, permissions.py）與SQLite資料庫進行互動，實現了權限的創建、查詢、更新和刪除。
