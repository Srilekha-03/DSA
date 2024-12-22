class Solution(object):
    def merge(self, intervals):
        output=[]
        intervals.sort()
        n=len(intervals)
        for i in range(n):
            if len(output)==0 or output[len(output)-1][1]<intervals[i][0]:
                output.append(intervals[i])
            else:
                output[len(output)-1][1]=max(output[len(output)-1][1],intervals[i][1])
        return output
                



        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        