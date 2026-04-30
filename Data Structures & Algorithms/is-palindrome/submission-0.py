class Solution:
    def isPalindrome(self, s: str) -> bool:
        # case insensitive
        # ignores non-alphanumeric (spaces too)
        # "Was it a car or a cat I saw?"
        # "o" - odd 19 // 2 = 9
        # "" - even - 4

        s = ''.join([z.lower() for z in s if z.isalnum()])

        for i in range(len(s) // 2):

            left_char = s[i]
            right_char = s[-(i + 1)]

            if left_char != right_char:
                return False

        return True