class Solution:
    def maxAscendingSum(self, arr: List[int]) -> int:

        if not arr:

            return 0



        max_sum = arr[0]

        current_sum = arr[0]



        for i in range(1, len(arr)):


                  
            if arr[i] > arr[i - 1]:

                current_sum += arr[i]

            else:


                    
                max_sum = max(max_sum, current_sum)
                current_sum = arr[i]
        return max(max_sum, current_sum)