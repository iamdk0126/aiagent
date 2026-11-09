import sqlite3
from typing import List, Optional, Tuple
from contextlib import contextmanager

class ProjectArchiver:
    """
    專案版本快照與 .omni_pack 打包匯出/還原器
    """

    def __init__(self, db_path: str):
        """
        初始化 ProjectArchiver
        :param db_path: 資料庫路徑
        """
        self.db_path = db_path
        self.db_manager = DBManager(db_path)

    @contextmanager
    def get_connection(self) -> sqlite3.Connection:
        """
        從連線池獲取連線
        :return: SQLite 連線
        """
        with self.db_manager.get_connection() as conn:
            yield conn

    def create_archive(self, project_id: int, snapshot_data: dict):
        """
        創建專案版本快照
        :param project_id: 專案ID
        :param snapshot_data: 快照數據
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO archive_log (project_id, snapshot_data) VALUES (?, ?)", (project_id, snapshot_data))
            conn.commit()

    def restore_archive(self, archive_id: int):
        """
        復原專案版本快照
        :param archive_id: 存档ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT snapshot_data FROM archive_log WHERE id = ?", (archive_id,))
            snapshot_data = cursor.fetchone()[0]
            conn.commit()
            return snapshot_data

    def create_project_pack(self, project_id: int, pack_data: dict):
        """
        創建 .omni_pack 打包
        :param project_id: 專案ID
        :param pack_data: 打包數據
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO project_info (project_id, pack_data) VALUES (?, ?)", (project_id, pack_data))
            conn.commit()

    def restore_project_pack(self, project_id: int):
        """
        復原 .omni_pack 打包
        :param project_id: 專案ID
        """
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT pack_data FROM project_info WHERE project_id = ?", (project_id,))
            pack_data = cursor.fetchone()[0]
            conn.commit()
            return pack_data

# 示例使用
if __name__ == "__main__":
    db_path = "example.db"
    project_archiver = ProjectArchiver(db_path)
    project_id = 1
    snapshot_data = {"version": "1.0", "data": "example_data"}
    pack_data = {"files": ["file1", "file2"], "metadata": "example_metadata"}

    project_archiver.create_archive(project_id, snapshot_data)
    restored_snapshot = project_archiver.restore_archive(1)
    print("Restored Snapshot:", restored_snapshot)

    project_archiver.create_project_pack(project_id, pack_data)
    restored_pack = project_archiver.restore_project_pack(project_id)
    print("Restored Pack:", restored_pack)
