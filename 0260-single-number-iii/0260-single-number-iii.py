class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_r=0

        for num in nums:
            xor_r^=num

        #Find rightmost set bit(mask)
        mask=xor_r&-xor_r

        groupa=0
        groupb=0
        for num in nums:
            if num & mask:
                groupa^=num
            else:
                groupb^=num

        return [groupa,groupb]