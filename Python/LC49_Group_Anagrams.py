class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            ans[tuple(sorted(word))].append(string)
        return ans.values()
