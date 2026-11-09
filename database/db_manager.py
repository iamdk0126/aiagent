import sqlite3
from typing import List, Optional, Tuple
from contextlib import contextmanager

class DBManager:
    """
    SQLite WAL 連線池、26張表初始化、Auto-Migration 與滾動備份
    """

    def __init__(self, db_path: str):
        """
        初始化 SQLite WAL 連線池
        :param db_path: 資料庫路徑
        """
        self.db_path = db_path
        self.pool = []

    @contextmanager
    def get_connection(self) -> sqlite3.Connection:
        """
        從連線池獲取連線
        :return: SQLite 連線
        """
        if self.pool:
            conn = self.pool.pop()
        else:
            conn = sqlite3.connect(self.db_path, isolation_level="WAL")
        try:
            yield conn
        finally:
            self.pool.append(conn)

    def init_tables(self):
        """
        初始化 26 張表
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            for i in range(1, 27):
                table_name = f"table_{i}"
                cursor.execute(f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    )
                """)
            conn.commit()

    def auto_migration(self):
        """
        Auto-Migration 功能
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA user_version")
            version = cursor.fetchone()[0]
            if version < 2:
                cursor.execute("ALTER TABLE table_1 ADD COLUMN new_column TEXT")
                conn.commit()
                cursor.execute("PRAGMA user_version = 2")

    def rolling_backup(self):
        """
        滚動備份功能
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA backup = 'backup.db'")
            conn.commit()
            cursor.execute("PRAGMA backup = 'backup.db'")

    def connect(self) -> None:
        """
        連接到 SQLite 數據庫
        """
        self.connection = sqlite3.connect(self.db_path, isolation_level="WAL")

    def disconnect(self) -> None:
        """
        斷開與 SQLite 數據庫的連線
        """
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, params: Optional[Tuple] = None) -> List[Tuple]:
        """
        執行 SQL 查詢
        :param query: SQL 查詢語句
        :param params: 查詢參數
        :return: 查詢結果
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def insert_data(self, table_name: str, data: List[Tuple]):
        """
        插入數據
        :param table_name: 表名
        :param data: 要插入的數據
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            placeholders = ', '.join(['?'] * len(data[0]))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.executemany(query, data)
            conn.commit()

    def update_data(self, table_name: str, set_clause: str, where_clause: str):
        """
        更新數據
        :param table_name: 表名
        :param set_clause: 更新子句
        :param where_clause: 篩選子句
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()

    def delete_data(self, table_name: str, where_clause: str):
        """
        刪除數據
        :param table_name: 表名
        :param where_clause: 篩選子句
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            query = f"DELETE FROM {table_name} WHERE {where_clause}"
            cursor.execute(query)
            conn.commit()
