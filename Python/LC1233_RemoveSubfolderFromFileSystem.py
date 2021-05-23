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
