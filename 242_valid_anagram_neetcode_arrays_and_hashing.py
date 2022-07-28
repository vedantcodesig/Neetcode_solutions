class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst1=[]
        lst2=[]
        for c in s:
            lst1.append(c)
        for c in t:
            lst2.append(c)
        if sorted(lst1)==sorted(lst2):
            return True
        else:
            return False