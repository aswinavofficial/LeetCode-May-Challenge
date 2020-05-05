from collections import OrderedDict 
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = OrderedDict() 
        
        for i in s:
            if i in d.keys():
                d[i] = d[i] + 1
            else:
                d[i] = 1
        
        for k,v in d.items():
            if v ==1:
                return s.find(k)
        return -1
        
