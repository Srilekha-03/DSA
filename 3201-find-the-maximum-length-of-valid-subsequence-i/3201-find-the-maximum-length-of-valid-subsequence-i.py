class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        i = 0
        odd_cnt = 0
        even_cnt = 0
        cnt = 0   # to track 3rd condition.
        flag = nums[0] % 2  # odd

        while i < len(nums):
            if nums[i] % 2:
                if flag:
                    flag = not flag
                    cnt += 1
                
                odd_cnt += 1
                
            else:
                if not flag:
                    flag = not flag
                    cnt += 1
                
                even_cnt += 1
            
            i += 1

        return max(cnt, odd_cnt, even_cnt)