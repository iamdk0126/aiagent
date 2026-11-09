# database/asset_embeddings.py

from typing import List, Dict, Optional
import sqlite3

class AssetEmbeddings:
    """
    類別 AssetEmbeddings 用於處理資產嵌入向量的資料庫操作。
    """

    def __init__(self, db_path: str):
        """
        初始化 AssetEmbeddings 類別。

        :param db_path: SQLite 資料庫路徑
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """
        創建 asset_embeddings 資料表。
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS asset_embeddings (
                asset_id TEXT PRIMARY KEY,
                embedding BLOB NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def create_embedding(self, asset_id: str, embedding: bytes):
        """
        創建一個新的資產嵌入向量。

        :param asset_id: 質產 ID
        :param embedding: 嵌入向量
        """
        self.cursor.execute('''
            INSERT INTO asset_embeddings (asset_id, embedding)
            VALUES (?, ?)
        ''', (asset_id, embedding))
        self.conn.commit()

    def get_embedding(self, asset_id: str) -> Optional[bytes]:
        """
        讀取一個資產的嵌入向量。

        :param asset_id: 質產 ID
        :return: 嵌入向量，如果不存在則返回 None
        """
        self.cursor.execute('''
            SELECT embedding FROM asset_embeddings WHERE asset_id = ?
        ''', (asset_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def update_embedding(self, asset_id: str, embedding: bytes):
        """
        更新一個資產的嵌入向量。

        :param asset_id: 質產 ID
        :param embedding: 新的嵌入向量
        """
        self.cursor.execute('''
            UPDATE asset_embeddings SET embedding = ? WHERE asset_id = ?
        ''', (embedding, asset_id))
        self.conn.commit()

    def delete_embedding(self, asset_id: str):
        """
        刪除一個資產的嵌入向量。

        :param asset_id: 質產 ID
        """
        self.cursor.execute('''
            DELETE FROM asset_embeddings WHERE asset_id = ?
        ''', (asset_id,))
        self.conn.commit()

    def close(self):
        """
        關閉資料庫連線。
        """
        self.conn.close()
