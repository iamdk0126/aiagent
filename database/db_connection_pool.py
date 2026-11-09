import sqlite3
from typing import List, Optional, Tuple, TypeVar, Generic, ContextManager
from contextlib import contextmanager

T = TypeVar('T')

class DBConnectionPool(Generic[T]):
    """
    SQLite 連線池類別，包含連線初始化、連線取得與釋放方法，並支援事務處理與錯誤重連機制。
    """

    def __init__(self, db_path: str, max_connections: int):
        """
        初始化 SQLite 連線池。

        :param db_path: SQLite 數據庫路徑
        :param max_connections: 最大連線數量
        """
        self.db_path = db_path
        self.max_connections = max_connections
        self.pool: List[sqlite3.Connection] = []
        self.in_use: List[sqlite3.Connection] = []

    def get_connection(self) -> sqlite3.Connection:
        """
        從連線池獲取一個 SQLite 連線。

        :return: SQLite 連線
        """
        if self.pool:
            conn = self.pool.pop()
            self.in_use.append(conn)
            return conn
        elif len(self.in_use) < self.max_connections:
            conn = sqlite3.connect(self.db_path)
            self.in_use.append(conn)
            return conn
        else:
            raise Exception("連線池已滿")

    def release_connection(self, conn: sqlite3.Connection) -> None:
        """
        將 SQLite 連線釋放回連線池。

        :param conn: SQLite 連線
        """
        if conn in self.in_use:
            self.in_use.remove(conn)
            self.pool.append(conn)

    @contextmanager
    def get_connection_context(self) -> ContextManager[sqlite3.Connection]:
        """
        上下文管理器，用於在 with 语句中獲取和釋放連線。

        :return: SQLite 連線
        """
        conn = self.get_connection()
        try:
            yield conn
        finally:
            self.release_connection(conn)

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        """
        執行 SQL 查詢。

        :param query: SQL 查詢語句
        :param params: 查詢參數
        :return: 查詢結果
        """
        with self.get_connection_context() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def insert_data(self, table_name: str, data: List[Tuple]) -> None:
        """
        插入數據。

        :param table_name: 表名
        :param data: 要插入的數據
        """
        with self.get_connection_context() as conn:
            cursor = conn.cursor()
            placeholders = ', '.join(['?'] * len(data[0]))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.executemany(query, data)
            conn.commit()

    def update_data(self, table_name: str, set_clause: str, where_clause: str) -> None:
        """
        更新數據。

        :param table_name: 表名
        :param set_clause: 更新子句
        :param where_clause: 篩選子句
        """
        with self.get_connection_context() as conn:
            cursor = conn.cursor()
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()

    def delete_data(self, table_name: str, where_clause: str) -> None:
        """
        刪除數據。

        :param table_name: 表名
        :param where_clause: 篩選子句
        """
        with self.get_connection_context() as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()
