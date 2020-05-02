#My Solution
#Runtime - 32 ms

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c  =0
        for i in range(len(J)):
            c= c + S.count(J[i])
        return c
        
        
 #Optimal Solution
 # Runtime - 5ms
 class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        setJ = set(J)
        return sum(s in setJ for s in S)
