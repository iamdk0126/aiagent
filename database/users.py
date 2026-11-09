import sqlite3
from typing import List, Dict, Optional

class Permission:
    """
    權限類別，用於處理權限資料庫操作。
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None

    def connect(self) -> None:
        """
        連接到 SQLite 資料庫。
        """
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row

    def disconnect(self) -> None:
        """
        斷開與 SQLite 資料庫的連線。
        """
        if self.connection:
            self.connection.close()
            self.connection = None

    def create_table(self) -> None:
        """
        創建 permissions 資料表。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS permissions (
                    permission_id TEXT PRIMARY KEY,
                    permission_name TEXT NOT NULL,
                    description TEXT
                )
            ''')
            self.connection.commit()

    def insert_permission(self, permission_id: str, permission_name: str, description: str) -> None:
        """
        插入一個新權限。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO permissions (permission_id, permission_name, description)
                VALUES (?, ?, ?)
            ''', (permission_id, permission_name, description))
            self.connection.commit()

    def get_permission(self, permission_id: str) -> Optional[Dict]:
        """
        查詢指定權限。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                SELECT * FROM permissions WHERE permission_id = ?
            ''', (permission_id,))
            return cursor.fetchone()

    def update_permission(self, permission_id: str, permission_name: str, description: str) -> None:
        """
        更新指定權限的資料。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                UPDATE permissions
                SET permission_name = ?, description = ?
                WHERE permission_id = ?
            ''', (permission_name, description, permission_id))
            self.connection.commit()

    def delete_permission(self, permission_id: str) -> None:
        """
        刪除指定權限。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                DELETE FROM permissions WHERE permission_id = ?
            ''', (permission_id,))
            self.connection.commit()

    def get_all_permissions(self) -> List[Dict]:
        """
        查詢所有權限。
        """
        with self.connection.cursor() as cursor:
            cursor.execute('''
                SELECT * FROM permissions
            ''')
            return cursor.fetchall()
