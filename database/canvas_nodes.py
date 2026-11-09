# database/canvas_edges.py

from typing import Optional

class CanvasEdge:
    """
    CanvasEdge 類別，定義畫布邊的屬性和方法。
    """

    def __init__(self, edge_id: str, source_node_id: str, target_node_id: str, project_id: str):
        """
        初始化 CanvasEdge 物件。

        :param edge_id: 边ID
        :param source_node_id: 源節點ID
        :param target_node_id: 目標節點ID
        :param project_id: 專案ID
        """
        self.edge_id = edge_id
        self.source_node_id = source_node_id
        self.target_node_id = target_node_id
        self.project_id = project_id

    def get_edge_id(self) -> str:
        """
        取得邊ID。

        :return: 边ID
        """
        return self.edge_id

    def get_source_node_id(self) -> str:
        """
        取得源節點ID。

        :return: 源節點ID
        """
        return self.source_node_id

    def get_target_node_id(self) -> str:
        """
        取得目標節點ID。

        :return: 目標節點ID
        """
        return self.target_node_id

    def get_project_id(self) -> str:
        """
        取得專案ID。

        :return: 專案ID
        """
        return self.project_id

    def update_target_node_id(self, new_id: str) -> None:
        """
        更新目標節點ID。

        :param new_id: 新的目標節點ID
        """
        self.target_node_id = new_id

    def __repr__(self) -> str:
        """
        取得邊的字符串表示。

        :return: 边的字符串表示
        """
        return f"CanvasEdge(edge_id={self.edge_id}, source_node_id={self.source_node_id}, target_node_id={self.target_node_id}, project_id={self.project_id})"
