import sqlite3
from typing import List, Optional, Tuple
from hnswlib import HierarchicalNSW
import numpy as np

class VectorIndexEngine:
    """
    sqlite-vec / HNSW 毫秒級資產向量檢索器
    """

    def __init__(self, db_path: str, index_path: str):
        """
        初始化向量索引引擎
        :param db_path: 資料庫路徑
        :param index_path: HNSW 索引路徑
        """
        self.db_path = db_path
        self.index_path = index_path
        self.index = None
        self.vector_ids = []
        self.load_index()

    def load_index(self):
        """
        加載 HNSW 索引
        """
        if not self.index:
            try:
                self.index = HierarchicalNSW(dim=128, max_elements=100000, M=16, ef_construction=200)
                self.index.load_index(self.index_path)
                with self.get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("SELECT id, vector FROM vector_index_table")
                    rows = cursor.fetchall()
                    for row in rows:
                        self.vector_ids.append(row[0])
                        self.index.add_item(np.frombuffer(row[1], dtype=np.float32), row[0])
            except FileNotFoundError:
                self.index = HierarchicalNSW(dim=128, max_elements=100000, M=16, ef_construction=200)

    @contextmanager
    def get_connection(self) -> sqlite3.Connection:
        """
        從連線池獲取連線
        :return: SQLite 連線
        """
        db_manager = DBManager(self.db_path, None)
        with db_manager.get_connection() as conn:
            yield conn

    def insert_vector(self, vector: np.ndarray, vector_id: int):
        """
        插入向量
        :param vector: 向量
        :param vector_id: 向量ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vector_index_table (id, vector) VALUES (?, ?)", (vector_id, vector.tobytes()))
            conn.commit()
        self.index.add_item(vector, vector_id)
        self.vector_ids.append(vector_id)

    def search_vector(self, vector: np.ndarray, k: int = 10) -> List[Tuple[int, float]]:
        """
        查詢向量
        :param vector: 向量
        :param k: 返回的最接近向量數量
        :return: 最接近向量及其距離
        """
        return self.index.search_knn(vector, k)

    def delete_vector(self, vector_id: int):
        """
        刪除向量
        :param vector_id: 向量ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vector_index_table WHERE id = ?", (vector_id,))
            conn.commit()
        self.index.delete_item(vector_id)
        self.vector_ids.remove(vector_id)

# 示例使用
if __name__ == "__main__":
    db_path = "example.db"
    index_path = "example_index.hnsw"
    vector_index_engine = VectorIndexEngine(db_path, index_path)
    vector = np.random.rand(128).astype(np.float32)
    vector_id = 1
    vector_index_engine.insert_vector(vector, vector_id)
    results = vector_index_engine.search_vector(vector)
    print(results)
    vector_index_engine.delete_vector(vector_id)
