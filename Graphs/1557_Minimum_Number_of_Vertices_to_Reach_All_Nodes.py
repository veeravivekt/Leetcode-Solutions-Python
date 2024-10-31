class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming_edges = set()
        for outgoing, incoming in edges:
            incoming_edges.add(incoming)
        return [i for i in range(n) if i not in incoming_edges]