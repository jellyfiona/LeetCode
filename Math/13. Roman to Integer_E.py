class Solution:
    def romanToInt(self, s: str) -> int:
        """
        time: 08152022  8:30---
        [Approach]
        It is a string , we can iterate it, see how many each letter stands for.
        We also need to keep a order, when smaller letter appears before bigger letter, we treats it differently.
        time_O(N) go through the string once.
        spaceO(1) no extra space needed.
        """
        
        LtoInt = {
            "I" : 1,
            "V" : 5,
            "X" :10,
            "L"  : 50,
            "C"  : 100,
            "D"  : 500,
            "M"  : 1000,
            "IV" : 4,
            "IX"  :9,
            "XL"  : 40,
            "XC"  :90,
            "CD"  : 400,
            "CM"   :900
         }
        
        sSet = {"I", "X", "C"}
        
        output = 0
        
        l = len(s)
        i = 0
        while i < l:
            if s[i] in sSet and i < l-1 and s[i:i+2] in LtoInt:
                output += LtoInt[ s[i:i+2] ]
                i += 2
            else:
                output += LtoInt[ s[i] ]
                i += 1
        return output
                    