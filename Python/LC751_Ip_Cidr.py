class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ipToNum(ipStr):
            sections = ipStr.split(".")
            return (int(sections[0]) << 24) + (int(sections[1]) << 16) + (int(sections[2]) << 8) + int(sections[3])

        def numToIp(ipNum):
            octet1 = (ipNum >> 24) & 255
            octet2 = (ipNum >> 16) & 255
            octet3 = (ipNum >> 8) & 255
            octet4 = ipNum & 255
            return str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)

        def ipNumToBlock(ipNum):
            # Note that this needs to checked when the input is 0
            if ipNum == 0:
                return (0, 2**32)
            rightMost1Num = ipNum & (-ipNum)
            mask, size = 32, 1
            while rightMost1Num != 1:
                mask -= 1
                size <<= 1
                rightMost1Num >>= 1
            return (mask, size)

        # Find the most siginificante 1's mask and size
        def mostSiginicantBit(num):
            size, mask = 1, 32
            while num != 1:
                size <<= 1
                num >>= 1
                mask -= 1
            return mask, size

        res, ipNum = [], ipToNum(ip)
        while n != 0:
            mask, size = ipNumToBlock(ipNum)
            if size <= n:
                res.append(numToIp(ipNum) + "/" + str(mask))
                ipNum += size
                n -= size
            else:
                mask1, size1 = mostSiginicantBit(n)
                res.append(numToIp(ipNum) + "/" + str(mask1))
                ipNum += size1
                n -= size1
        return res