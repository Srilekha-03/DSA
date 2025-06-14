class Solution(object):
    def minMaxDifference(self, num):
        num_str = str(num)       
        for ch in num_str:
            if ch != '9':
                max_num = num_str.replace(ch, '9')
                break
        else:
            max_num = num_str

        for ch in num_str:
            if ch != '0':
                min_num = num_str.replace(ch, '0')
                break
        else:
            min_num = num_str

        return int(max_num) - int(min_num)

        



        
        """
        :type num: int
        :rtype: int
        """
        