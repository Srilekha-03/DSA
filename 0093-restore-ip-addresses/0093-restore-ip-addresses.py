class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        n = len(s)
        def isValid(segment: str) -> bool:
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255
        def backtrack(index: int, dots: int, path: List[str]):
            if dots == 4 and index == n:
                result.append(".".join(path))
                return
            if dots >= 4:
                return
            for length in range(1, 4):#backtracking in loop only
                if index + length > n:
                    break
                segment = s[index:index+length]
                if isValid(segment):
                    backtrack(index + length, dots + 1, path + [segment])
        if n > 12:
            return [] #very base condition
        backtrack(0, 0, [])
        return result
