from typing import Optional

class BudgetRule:
    """
    管理單專案預算規則的類別
    """

    def __init__(self, project_id: str, max_shot_cost: int, max_episode_cost: int, max_project_cost: int, current_project_spent: int, auto_fallback_to_local: int):
        """
        初始化 BudgetRule 類別

        :param project_id: 專案ID
        :param max_shot_cost: 最大單鏡預算
        :param max_episode_cost: 最大單集預算
        :param max_project_cost: 最大單專案預算
        :param current_project_spent: 目前專案已支出
        :param auto_fallback_to_local: 是否自動切換到本地免費模型
        """
        self.project_id = project_id
        self.max_shot_cost = max_shot_cost
        self.max_episode_cost = max_episode_cost
        self.max_project_cost = max_project_cost
        self.current_project_spent = current_project_spent
        self.auto_fallback_to_local = auto_fallback_to_local

    @classmethod
    def from_db(cls, project_id: str):
        """
        從資料庫讀取預算規則

        :param project_id: 專案ID
        :return: BudgetRule 實例
        """
        # 這裡需要實現從資料庫讀取預算規則的邏輯
        # 例如：使用 SQLAlchemy 或其他 ORM 工具
        # return cls(project_id, max_shot_cost, max_episode_cost, max_project_cost, current_project_spent, auto_fallback_to_local)
        pass

    def save_to_db(self):
        """
        將預算規則寫入資料庫
        """
        # 這裡需要實現將預算規則寫入資料庫的邏輯
        # 例如：使用 SQLAlchemy 或其他 ORM 工具
        pass
