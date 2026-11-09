from typing import List, Dict
from database.db_manager import DBManager

class ModelMenuProvider:
    """
    ModelMenuProvider: 提供模型菜单和基础连接接口的类
    """

    def __init__(self, db_manager: DBManager):
        """
        初始化 ModelMenuProvider 类

        :param db_manager: 数据库管理器实例
        """
        self.db_manager = db_manager

    def fetch_free_local_models(self) -> List[Dict]:
        """
        获取本地免费模型

        :return: 本地免费模型列表
        """
        query = "SELECT * FROM model_store WHERE is_free = 1"
        return self.db_manager.execute_query(query)

    def fetch_commercial_api_models(self) -> List[Dict]:
        """
        获取商业API模型

        :return: 商业API模型列表
        """
        query = "SELECT * FROM model_store WHERE is_free = 0"
        return self.db_manager.execute_query(query)
