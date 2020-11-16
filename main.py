class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        chrs = list(s)
        num: int = 0
        for i in range(len(chrs)):
            if i != len(chrs) - 1 and roman[chrs[i]] < roman[chrs[i + 1]]:
                    num -= roman[chrs[i]]
                    continue
            num += roman[chrs[i]]
        return num


a = Solution()
s = "III"
print(a.romanToInt(s))
s = "IV"
print(a.romanToInt(s))
s = "IX"
print(a.romanToInt(s))
s = "LVIII"
print(a.romanToInt(s))
s = "MCMXCIV"
print(a.romanToInt(s))
