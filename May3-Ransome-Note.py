#My solution

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l = {}
        for i in ransomNote:
            if i in l:
                l[i] = l[i] +1
            else:
                l[i] = 1
            
        for key,value in l.items():
            c = magazine.count(key)
            if c < value:
                return False
        return True
