import sqlite3
from typing import List, Optional
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

# 示例使用
if __name__ == "__main__":
    db_manager = DBManager("example.db")
    db_manager.init_tables()
    db_manager.auto_migration()
    db_manager.rolling_backup()
