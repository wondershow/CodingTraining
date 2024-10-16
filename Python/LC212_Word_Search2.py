class TrieNode:
    def __init__(self):
        self.flag = False
        self.kids = {}

'''
A Trie + DFS problem

The mistakes I made:
1. for each dfs, we need a "visited" set
2. for each backtracking, we need to both remove the last item in path and cur node from "visited"=
'''
class Solution:
    def _build_trie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.kids:
                     node.kids[c] = TrieNode()
                node = node.kids[c]
            node.flag = True
        return root

    def dfs(self, trie: TrieNode, x: int, y: int, board: List[List[str]], path: List[str], res: List[str], visited: set[tuple]) -> None:
        if board[x][y] not in trie.kids or (x, y) in visited:
            return
        visited.add((x, y))
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        M, N = len(board), len(board[0])
        path.append(board[x][y])
        if trie.kids[board[x][y]].flag:
            res.append("".join(path))
        for dx, dy in dirs:
            x1, y1 = x + dx, y + dy
            if x1 < 0 or y1 < 0 or x1 == M or y1 == N:
                continue
            self.dfs(trie.kids[board[x][y]], x1, y1, board, path, res, visited)
        path.pop()
        visited.remove((x, y))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, root = [], self._build_trie(words)
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                path = []
                visited = set()
                self.dfs(root, i, j, board, path, res, visited)
        return list(set(res))
