from typing import List, Dict, Optional

class AgentNode:
    """
    智能體節點類別
    """
    def __init__(self, node_id: str, node_type: str):
        self.node_id = node_id
        self.node_type = node_type

class Edge:
    """
    边類別
    """
    def __init__(self, edge_id: str, source_node: AgentNode, target_node: AgentNode):
        self.edge_id = edge_id
        self.source_node = source_node
        self.target_node = target_node

class MultiAgentGraph:
    """
    多智能體協同圖形數據庫類別
    """
    def __init__(self):
        self.nodes: List[AgentNode] = []
        self.edges: List[Edge] = []

    def add_node(self, node: AgentNode):
        """
        添加智能體節點
        """
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        """
        添加邊
        """
        self.edges.append(edge)

    def get_node(self, node_id: str) -> Optional[AgentNode]:
        """
        根據節點ID獲取智能體節點
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_edges(self, node_id: str) -> List[Edge]:
        """
        根據節點ID獲取所有連接的邊
        """
        return [edge for edge in self.edges if edge.source_node.node_id == node_id or edge.target_node.node_id == node_id]

    def remove_node(self, node_id: str):
        """
        根據節點ID移除智能體節點
        """
        self.nodes = [node for node in self.nodes if node.node_id != node_id]
        self.edges = [edge for edge in self.edges if edge.source_node.node_id != node_id and edge.target_node.node_id != node_id]

    def remove_edge(self, edge_id: str):
        """
        根據邊ID移除邊
        """
        self.edges = [edge for edge in self.edges if edge.edge_id != edge_id]
