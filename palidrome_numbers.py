class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num = str(x)
        rev_str_num = str_num[::-1]
        if str_num == rev_str_num:
            return True
        return False