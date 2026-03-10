class Solution:
    def largestSwap(self, s):
        s = list(s)
        last = {}
        for i in range(len(s)):
            last[int(s[i])] = i

        for i in range(len(s)):
            for d in range(9, int(s[i]), -1):
                if d in last and last[d] > i:
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return "".join(s)

        return "".join(s)
        #code here
        