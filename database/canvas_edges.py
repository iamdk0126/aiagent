from typing import Optional, List, Dict

class CanvasEdge:
    """
    CanvasEdge 類別，定義邊的屬性和方法。
    """

    def __init__(self, edge_id: str, source_node_id: str, target_node_id: str):
        """
        初始化 CanvasEdge 物件。

        :param edge_id: 边的唯一識別符
        :param source_node_id: 边的源節點識別符
        :param target_node_id: 边的目標節點識別符
        """
        self.edge_id: str = edge_id
        self.source_node_id: str = source_node_id
        self.target_node_id: str = target_node_id

    def get_edge_id(self) -> str:
        """
        取得邊的唯一識別符。

        :return: 边的唯一識別符
        """
        return self.edge_id

    def get_source_node_id(self) -> str:
        """
        取得邊的源節點識別符。

        :return: 边的源節點識別符
        """
        return self.source_node_id

    def get_target_node_id(self) -> str:
        """
        取得邊的目標節點識別符。

        :return: 边的目標節點識別符
        """
        return self.target_node_id

    def set_edge_id(self, edge_id: str) -> None:
        """
        設定邊的唯一識別符。

        :param edge_id: 边的唯一識別符
        """
        self.edge_id = edge_id

    def set_source_node_id(self, source_node_id: str) -> None:
        """
        設定邊的源節點識別符。

        :param source_node_id: 边的源節點識別符
        """
        self.source_node_id = source_node_id

    def set_target_node_id(self, target_node_id: str) -> None:
        """
        設定邊的目標節點識別符。

        :param target_node_id: 边的目標節點識別符
        """
        self.target_node_id = target_node_id

    def __repr__(self) -> str:
        """
        取得邊的字串表示。

        :return: 边的字串表示
        """
        return f"CanvasEdge(edge_id={self.edge_id}, source_node_id={self.source_node_id}, target_node_id={self.target_node_id})"
