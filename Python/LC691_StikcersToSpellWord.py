class Solution:
    """
        DFS search with multi pruning
        1. Convert each sticker into a Counter mapping, only those "overlap" with the target mapping will be stored
        2. In each dfs, we iterate stickers and do a Counter deduction to get the next level of target and keep search
            2.1 Note that in this process, we ditch searching space which the target[0] is not contained in the sticker's counter. 
               This way it significantlly reduced runtime (like 95%). Not sure how this works.
    """
    def minStickers(self, stickers, target):
        self.memo, stickers = {}, [Counter(s) for s in stickers if set(list(s)) & set(list(target))]
        def dfs(target):
            if not target:
                return 0
            if target in self.memo:
                return self.memo[target]
            res = float("inf")
            c = Counter(target)
            for sticker in stickers:
                
                #Not sure how this step works, but it reduces the run time by 95%
                if sticker[target[-1]] == 0:
                    continue
                new_target = "".join([c * v for c, v in (c - sticker).items()])
                if new_target == target or c[target[0]] == 0:
                    continue
                    
                next_val = dfs(new_target)
                if next_val != -1:
                    res = min(res, next_val + 1)
            self.memo[target] = -1 if res == float("inf") else res
            return self.memo[target]
        return dfs(target)
