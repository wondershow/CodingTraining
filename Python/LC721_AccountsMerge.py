class Solution:
    """
    UnionFind solution
    1. Get UF size, email2name, name2email 
    2. iterate accounts, union other emails with first email
    3. build email groups
    4. return
    """
    def accountsMerge1(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        1. EmailToName
        2. UF
        3. EmailToNumber, NumberToEmail
        """
        def find(uf, a):
            if uf[a] != a:
                uf[a] = find(uf, uf[a])
            return uf[a]
        
        def union(uf, a, b):
            ra, rb = find(uf, a), find(uf, b)
            if ra != rb:
                uf[ra] = rb
        
        def get_total_emails(accounts):
            emailToNumber, numberToEmail = {}, {}
            for account in accounts:
                for email in account[1:]:
                    if email not in emailToNumber:
                        emailToNumber[email] = len(emailToNumber)
                        numberToEmail[len(emailToNumber) - 1] = email
            return [emailToNumber, numberToEmail]
        
        seenEmail = set()
        email2Name = {}
        emailToNumber, numberToEmail = get_total_emails(accounts)
        uf = [i for i in range(len(numberToEmail))]
        
        #Build UionFind, create email to name mapping
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email2Name[email] = name
                union(uf, emailToNumber[email], emailToNumber[account[1]])
        
        total_emails = len(email2Name)
        email_group = defaultdict(set)
        for i in range(total_emails):
            root = find(uf, i)
            email_group[root].add(i)
        
        res = []
        for root, members in email_group.items():
            root_email = numberToEmail[root]
            emails = sorted([numberToEmail[member] for member in members])
            tmp = [email2Name[root_email]]
            tmp.extend(emails)
            res.append(tmp)
        return res
    
    """
    dfs solution. Use stack not recursion to implement dfs.
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name, graph = {}, defaultdict(set)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name
        
        seen, res = set(), []
        for email in email_to_name:
            if email not in seen:
                stack = [email]
                seen.add(email)
                component = [email]
                while stack:
                    for neighbor in graph[stack.pop()]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            component.append(neighbor)
                            stack.append(neighbor)
                res.append([email_to_name[email]] + sorted(component))
        return res
        
        
        
        
