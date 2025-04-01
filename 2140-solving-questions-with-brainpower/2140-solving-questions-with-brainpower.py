class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        def maxProfitMemoization(questions,pos,mem):
            if pos>=n:
                return 0
            if mem[pos]!=-1:
                return mem[pos]
            not_take=maxProfitMemoization(questions,pos+1,mem)
            take=questions[pos][0]+maxProfitMemoization(questions,pos+questions[pos][1]+1,mem)
            mem[pos]=max(not_take,take)
            return mem[pos]

        n=len(questions)
        mem=[-1]*n
        return maxProfitMemoization(questions,0,mem)
        