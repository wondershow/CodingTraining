class Solution:
    
    """
    The key is how to carefully compute the 'signature' of each string
    """
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def get_signature(string):
            delta = ord(string[0]) - ord('a')
            res = ""
            for c in string:
                res += chr( ord('a') + (ord(c) - ord('a') - delta + 26) % 26)
            return res
        
        res = defaultdict(list)
        #print(get_signature("def"))
        for string in strings:
            res[get_signature(string)].append(string)
            
        return res.values() 
