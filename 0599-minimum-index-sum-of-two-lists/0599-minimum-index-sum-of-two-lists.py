class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        mini=float('inf')
        for i in range(len(list1)):
            if list1[i] in list2:
                if i+list2.index(list1[i])<mini:
                    res=[list1[i]]
                    mini=i+list2.index(list1[i])
                elif i+list2.index(list1[i])==mini:
                    res.append(list1[i])
        return res

        