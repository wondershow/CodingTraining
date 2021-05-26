class Solution:
    def validIPAddress(self, IP: str) -> str:
        def check_ipv4(IP):
            sections = IP.split(".")
            if len(sections) != 4:
                return False
            for section in sections:
                if not section or section[0] == "0" and len(section) > 1:
                    return False
                try:
                    val = int(section)
                    if val < 0 or val >= 256:
                        return False
                except:
                    return False
            return True
        
        def check_ipv6(IP):
            sections = IP.split(":")
            if len(sections) != 8:
                return False
            for section in sections:
                section = section.lower()
                if len(section) > 4 or len(section) == 0:
                    return False
                try:
                    int(section, 16)
                except:
                    return False
            return True
        if not IP:
            return "Neither"
        if check_ipv4(IP):
            return "IPv4"
        if check_ipv6(IP):
            return "IPv6"
        return "Neither"
