from typing import List, Optional
from database.db_manager import DBManager

class StoryBibleMemory:
    """智能體長期記憶檢索、角色關係圖與跨集狀態防穿幫注入"""
    def __init__(self, db_manager: DBManager):
        """
        初始化 StoryBibleMemory 類別

        :param db_manager: DBManager 實例，用於與資料庫進行連線
        """
        self.db_manager = db_manager

    def load_memory(self, project_id: str) -> None:
        """
        從資料庫中加載記憶

        :param project_id: 專案ID，用於識別特定的記憶
        """
        query = "SELECT memory_data FROM agent_nodes WHERE project_id = ?"
        result = self.db_manager.execute_query(query, (project_id,))
        if result:
            self.memory_data = result[0][0]
        else:
            self.memory_data = {}

    def save_memory(self, project_id: str, memory_data: dict) -> None:
        """
        將記憶保存到資料庫

        :param project_id: 專案ID，用於識別特定的記憶
        :param memory_data: 要保存的記憶數據
        """
        query = "INSERT OR REPLACE INTO agent_nodes (project_id, memory_data) VALUES (?, ?)"
        self.db_manager.execute_query(query, (project_id, memory_data))

    def retrieve_memory(self, project_id: str) -> dict:
        """
        從資料庫中检索記憶

        :param project_id: 專案ID，用於識別特定的記憶
        :return: 記憶數據
        """
        self.load_memory(project_id)
        return self.memory_data
