class Solution(object):
    def isPalindrome(self, x):
        res = ''

        for i in range(len(str(x)) - 1, -1, -1):
            res += str(x)[i]
        if str(x) == res:
            return True
        else:
            return False