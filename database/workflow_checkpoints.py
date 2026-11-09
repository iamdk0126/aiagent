import sqlite3
from typing import Optional

class WorkflowCheckpoint:
    """
    WorkflowCheckpoint 類別用於管理工作流程的檢查點，包括保存和加載檢查點。
    """

    def __init__(self, db_path: str):
        """
        初始化 WorkflowCheckpoint 類別。

        :param db_path: SQLite 數據庫的路徑。
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        創建 workflow_checkpoints 表。
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS workflow_checkpoints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                checkpoint_data BLOB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save_checkpoint(self, checkpoint_data: bytes):
        """
        保存檢查點數據。

        :param checkpoint_data: 檢查點數據，以 bytes 格式傳遞。
        """
        self.cursor.execute('''
            INSERT INTO workflow_checkpoints (checkpoint_data) VALUES (?)
        ''', (checkpoint_data,))
        self.conn.commit()

    def load_checkpoint(self) -> Optional[bytes]:
        """
        加載最新的檢查點數據。

        :return: 檢查點數據，如果沒有檢查點則返回 None。
        """
        self.cursor.execute('''
            SELECT checkpoint_data FROM workflow_checkpoints ORDER BY created_at DESC LIMIT 1
        ''')
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def __del__(self):
        """
        類別析構函數，關閉數據庫連接。
        """
        self.conn.close()
