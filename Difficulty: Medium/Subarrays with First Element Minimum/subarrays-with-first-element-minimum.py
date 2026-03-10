class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        nse = [0] * n
        self.nextSmallerElement(arr, nse, n)
        count = 0
        for i in range(n):
            count += (nse[i] - i)
        return count

    def nextSmallerElement(self, arr, nse, n):
        st = []
        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if not st:
                nse[i] = n
            else:
                nse[i] = st[-1]
            st.append(i)
        # code here
        