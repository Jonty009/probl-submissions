class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(ord('a'), ord('z'), s.lower())
        s = s.lower()
        stripped = ""
        for ch in s:
            if (ord(ch) in range(97,123)) or (ord(ch) in range(48, 58)):
                stripped += ch
            # print (ch)
        left, right = 0, len(stripped) - 1
        # print(stripped)
        while left < right:
            if stripped[left] == stripped[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        # s = s.
        # return False