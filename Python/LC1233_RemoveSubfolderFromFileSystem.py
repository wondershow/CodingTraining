class Solution:
    """
    Sort and add.
    Need to be careful when decide if path A is a subfolder of path B
    e.g A = /a B= /ab
    we can not use 'startswith' directly, we concatenate A with "/" and B with "/" to explicitly indicate endo f a path
    """
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not (path + "/").startswith(res[-1] + "/"):
                res.append(path)
        return res
    
    """
    1. sort all paths by length
    2. iterate each path, check every substring ends at "/" to see if it already in the result if yes it has a parent
    """
    def removeSubfolders2(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda v:len(v))
        seen = set()
        for path in folder:
            size = len(path)
            for i, c in enumerate(path):
                if c == "/" and i != 0 and path[:i] in seen:
                    break
            else:
                seen.add(path)
        return list(seen)
