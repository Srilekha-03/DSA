class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        res.append(str(q))
        if r == 0:
            return "".join(res)
        res.append(".")
        m = {}
        while r != 0:
            if r in m:
                idx = m[r]
                res.insert(idx, "(")
                res.append(")")
                break
            m[r] = len(res)
            r *= 10
            q, r = divmod(r, denominator)
            res.append(str(q))
        return "".join(res)