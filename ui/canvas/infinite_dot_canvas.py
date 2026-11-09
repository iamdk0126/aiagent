from typing import List, Dict, Optional
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem
from PySide6.QtCore import Qt, QPointF

class Node:
    """
    節點類別，表示畫布上的節點
    """

    def __init__(self, id: int, position: QPointF):
        """
        初始化 Node 类
        :param id: 节点ID
        :param position: 节点位置
        """
        self.id = id
        self.position = position
        self.connections = []

    def add_connection(self, edge: 'Edge'):
        """
        添加連線
        :param edge: 連線
        """
        self.connections.append(edge)

    def remove_connection(self, edge: 'Edge'):
        """
        移除連線
        :param edge: 連線
        """
        self.connections.remove(edge)

class Edge:
    """
    連線類別，表示畫布上的連線
    """

    def __init__(self, source: Node, target: Node):
        """
        初始化 Edge 类
        :param source: 源節點
        :param target: 目標節點
        """
        self.source = source
        self.target = target

class InfiniteDotCanvas(QGraphicsScene):
    """
    無邊際點陣畫布類別，表示畫布上的畫布
    """

    def __init__(self):
        """
        初始化 InfiniteDotCanvas 类
        """
        super().__init__()
        self.nodes = []
        self.edges = []

    def add_node(self, node: Node):
        """
        添加節點
        :param node: 节点
        """
        self.nodes.append(node)
        self.addItem(self.create_node_item(node))

    def add_edge(self, edge: Edge):
        """
        添加連線
        :param edge: 連線
        """
        self.edges.append(edge)
        self.addItem(self.create_edge_item(edge))

    def create_node_item(self, node: Node) -> QGraphicsItem:
        """
        創建節點圖形項
        :param node: 节点
        :return: 节点圖形項
        """
        item = QGraphicsEllipseItem(node.position.x() - 10, node.position.y() - 10, 20, 20)
        item.setBrush(Qt.blue)
        return item

    def create_edge_item(self, edge: Edge) -> QGraphicsItem:
        """
        創建連線圖形項
        :param edge: 連線
        :return: 連線圖形項
        """
        item = QGraphicsLineItem(edge.source.position.x(), edge.source.position.y(), edge.target.position.x(), edge.target.position.y())
        item.setPen(Qt.black)
        return item
