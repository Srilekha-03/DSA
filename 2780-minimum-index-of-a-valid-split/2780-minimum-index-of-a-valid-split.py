from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count=Counter(nums)
        majority_element=max(count,key=count.get)
        majority_count=count[majority_element]
        left_count=0
        right_count=majority_count
        n=len(nums)       
        for i in range(n-1):
            if nums[i]==majority_element:
                left_count+=1
                right_count-=1
            if left_count*2>(i+1) and right_count*2>(n-i-1):
                return i
        return -1
        