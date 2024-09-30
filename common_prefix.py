class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        first_word = strs[0]
        rem_list = strs[1:]
        common_prefix = ""
        end_match = False
        for i in first_word:
            common_prefix = common_prefix + i
            for words in rem_list:
                if not words.startswith(common_prefix):
                    end_match = True
            if end_match:
                break
        if end_match:
            return common_prefix[:-1]
        else:
            return common_prefix

