class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        """
        For preorder, when we tag all the null nodes as #, then: 
        1. number of '#' = number nodes + 1
        2. the preorder traversal stack pops when sees a '#'

        We just need to verify this process. Some small tricks, remove last '#'.
        """
        stack, steps = [], preorder.split(",")
        if steps[-1] != "#":
            return False
        steps.pop()
        nulls, nodes = 0, 0
        for step in steps:
            if step != '#':
                nodes += 1
                stack.append(step)
            elif len(stack) == 0:
                return False
            else:
                nulls += 1
                stack.pop()
        if len(stack) == 0 and nulls == nodes:
            return True
        return False
