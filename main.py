class Solution:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        chrs = list(s)
        num: int = 0
        for i in range(len(chrs)):
            if i != len(chrs) - 1 and self.roman[chrs[i]] < self.roman[chrs[i + 1]]:
                    num -= self.roman[chrs[i]]
                    continue
            num += self.roman[chrs[i]]
        return num

    def strInput(self) -> str:
        while True:
            s = input("Enter a Roman number in range [1:3999] (max length 15): ")
            if self.chkStr(s):
                return s
            else:
                print("Incorrect input! Try again.")

    def chkStr(self, s: str) -> bool:
        if 1 <= len(s) <= 15:
            for ch in s:
                if ch not in a.roman:
                    return False
            return True


a = Solution()
s = a.strInput()
print(a.romanToInt(s))

