class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def get_distances(beginWord, endWord, word_set):
            que = [beginWord]
            seen, res, depth = {beginWord}, {}, 0
            seen_endWord = False
            while que:
                size = len(que)
                for _ in range(size):
                    word = que.pop(0)
                    res[word] = depth
                    if word == endWord:
                        seen_endWord = True
                    for i in range(len(word)):
                        tmp = list(word)
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            tmp[i] = c
                            neighbor = "".join(tmp)
                            if neighbor not in seen and neighbor in word_set:
                                que.append(neighbor)
                                seen.add(neighbor)
                
                if seen_endWord:
                    break
                depth += 1
            return res
        
        def dfs(word, depth, endWord, word_distance, path):
            #print(path)
            nonlocal res
            if word == endWord:
                res.append(list(path))
                return
            for i in range(len(word)):
                tmp = list(word)
                for c in "abcdefghijklmnopqrstuvwxyz":
                    tmp[i] = c
                    neighbor = "".join(tmp)
                    if neighbor in word_distance and word_distance[neighbor] == depth + 1:
                        path.append(neighbor)
                        dfs(neighbor, depth + 1, endWord, word_distance, path)
                        path.pop()
        
        
        word_set = set(wordList)
        word_distance = get_distances(beginWord, endWord, word_set)
        #print(word_distance)
        res = []
        dfs(beginWord, 0, endWord, word_distance, [beginWord])
        return res
