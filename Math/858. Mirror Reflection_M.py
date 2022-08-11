"""
858. Mirror Reflection_M

https://leetcode.com/problems/mirror-reflection/

##############################

类似题型:


#################################
考点或思路:

"""



class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        今天状态差，想了一早上。
        https://leetcode.com/problems/mirror-reflection/discuss/2377070/Pseudocode-Explain-Why-Odd-and-Even-Matter
        
        """
        
        # reduce 2 from the equation
        while (p%2==0 and q%2==0):
            p = p / 2
            q = q / 2
        

        # conclusion
        if (p%2 == 0):
            return 2

        if (q%2 == 0):
            return 0

        return 1
    