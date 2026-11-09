from typing import List, Optional

class AgentNode:
    """智能體節點類別骨架"""
    def __init__(self, node_id: str, node_type: str):
        self.node_id = node_id
        self.node_type = node_type

    def __repr__(self):
        return f"AgentNode(node_id={self.node_id}, node_type={self.node_type})"

class Edge:
    """邊類別骨架"""
    def __init__(self, edge_id: str, source_node_id: str, target_node_id: str):
        self.edge_id = edge_id
        self.source_node_id = source_node_id
        self.target_node_id = target_node_id

    def __repr__(self):
        return f"Edge(edge_id={self.edge_id}, source_node_id={self.source_node_id}, target_node_id={self.target_node_id})"

class MultiAgentGraph:
    """圖形數據結構類別骨架"""
    def __init__(self):
        self.nodes: List[AgentNode] = []
        self.edges: List[Edge] = []

    def add_node(self, node: AgentNode):
        """添加節點"""
        self.nodes.append(node)

    def add_edge(self, edge: Edge):
        """添加邊"""
        self.edges.append(edge)

    def get_nodes(self) -> List[AgentNode]:
        """獲取所有節點"""
        return self.nodes

    def get_edges(self) -> List[Edge]:
        """獲取所有邊"""
        return self.edges

    def get_node_by_id(self, node_id: str) -> Optional[AgentNode]:
        """通過節點ID獲取節點"""
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

    def get_edge_by_id(self, edge_id: str) -> Optional[Edge]:
        """通過邊ID獲取邊"""
        for edge in self.edges:
            if edge.edge_id == edge_id:
                return edge
        return None
