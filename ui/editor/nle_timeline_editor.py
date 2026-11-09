from typing import List, Optional
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsLineItem
from PySide6.QtCore import Qt, QPointF, QRectF

class Node(QGraphicsItem):
    """
    節點類別，表示畫布上的節點
    """
    def __init__(self, id: int, position: QPointF):
        super().__init__()
        self.id = id
        self.position = position
        self.connections = []

    def add_connection(self, edge: 'Edge') -> None:
        self.connections.append(edge)

    def remove_connection(self, edge: 'Edge') -> None:
        self.connections.remove(edge)

    def boundingRect(self) -> QRectF:
        return QRectF(-10, -10, 20, 20)

    def paint(self, painter, option, widget=None):
        painter.setBrush(Qt.blue)
        painter.drawEllipse(self.boundingRect())

class Edge(QGraphicsItem):
    """
    連線類別，表示畫布上的連線
    """
    def __init__(self, source: Node, target: Node):
        super().__init__()
        self.source = source
        self.target = target

    def boundingRect(self) -> QRectF:
        return QRectF()

    def paint(self, painter, option, widget=None):
        painter.setPen(Qt.black)
        painter.drawLine(self.source.position, self.target.position)

class NLETimelineEditor(QGraphicsScene):
    """
    NLE 時間軸編輯器類別，表示畫布上的編輯器
    """
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.edges = []

    def add_node(self, node: Node) -> None:
        self.addItem(node)
        self.nodes.append(node)

    def add_edge(self, edge: Edge) -> None:
        self.addItem(edge)
        self.edges.append(edge)

    def create_node_item(self, node: Node) -> QGraphicsItem:
        return node

    def create_edge_item(self, edge: Edge) -> QGraphicsItem:
        return edge

    def sort_nodes(self) -> None:
        """
        節點排序
        """
        pass

    def align_timeline(self) -> None:
        """
        時間軸對齊
        """
        pass

    def auto_connect_edges(self) -> None:
        """
        边的自動連接
        """
        pass
