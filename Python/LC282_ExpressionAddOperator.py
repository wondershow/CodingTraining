class Solution:
    """
       This is a double "backtracking" problem. 1. We need to use dfs to search the solution space. 2. On the way, we need to backtrack the expression's value. 
    The 1. is implicit by dfs recursion
    The 2. needs to be maintained in the code. in each recursion call, we spawn 3 different new calls, (+/-/*), when we are doing (-) and (*), the current level's temp evaluation result will be partly canceled, 
    eg. 3-4|*5, the temp result is (3-4) = -1 in the recusion, but to apply '*', we need to cancel the previous operator ('-'). To do that, we always remember last operand, and convert '-' to a negate
    
    Mistakes made:
    1. Fail to handle the case when index is at 0
        1.1 what is the pre and tmp result
    2. Fail to handle the case when a substring number starts with '0' but have 2 or more digits
    3. Fail to handle the case when a number is overflow (need to carefully think the end condition of 'for' loop in the recursion)
    
    
    
    
    
    """
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, res, val, expr, index, pre, target):
            if index == len(num):
                #print(str(val))
                if val == target:
                    res.append(expr)
                return
            for i in range(index + 1, len(num) + 1):
                if num[index] == "0" and i > index + 1:
                    continue
                if i - index > 10:
                    continue
                operand = int(num[index : i])
                if index == 0:
                    dfs(num, res, operand, num[index : i], i, operand, target)
                    continue
                dfs(num, res, val + operand, expr + "+" + num[index : i], i, operand, target)
                dfs(num, res, val - operand, expr + "-" + num[index : i], i, -operand, target)
                dfs(num, res, val - pre + pre * operand, expr + "*" + num[index : i], i, pre * operand, target)
        res = []
        dfs(num, res, 0, "", 0, 0, target)
        return res
