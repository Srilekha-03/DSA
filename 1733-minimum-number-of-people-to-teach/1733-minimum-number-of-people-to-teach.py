class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        sad=[]
        def isSad(l):
            l1=languages[l[0]-1]
            l2=languages[l[1]-1]
            return set(l1).isdisjoint(set(l2))

        for i in friendships:
            if isSad(i):
                sad.append(i[0])
                sad.append(i[1])
        dic=dict()
        sad=list(set(sad))
        for user in sad:
            langs=languages[user-1]
            for i in langs:
                if i not in dic:
                    dic[i]=1
                else:
                    dic[i]+=1
        max_users_known_lang=max(dic.values())
        return len(sad)-max_users_known_lang
