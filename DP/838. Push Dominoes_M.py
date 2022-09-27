"""
838. Push Dominoes——M

https://leetcode.com/problems/push-dominoes/
##############################

类似题型:


#################################
考点或思路:
[DP][logic]
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        """
        time: 3:10---3:54
        第一次做
        分情况讨论吗？这个是DP问题。
        DP[i] 是i个牌的结果。
        DP[i] = 
           1 如果D[i]是点，那么DP[i]维持是点，
           2，如果D[i]是L，那么判断前边有没有R，如果没有R，那么前边所有的点都变成L，
                                    如果有R，那么之前需要标记R的起始idx，从这个rightIdx到当前L的位置，对称的标
                                    然后把rightIdx置为空
           3, 如果D[i]是R,判断前边有没有R，如果有，那么前边的R到现在的R都设置为R，更新rightIDx，
                                   如果没有rightIdx，那么现在设定为当前idx
        """
        
        Dlst = list(dominoes)
        l = len(Dlst)
        DP = ["."] * l
        startidx = 0
        hasRight = False
        for i in range(l):
            if Dlst[i] == "L":
                if hasRight:
                    # 左右对称的标注
                    seglen = i+1 - startidx
                    rightend = startidx + (seglen//2) 
                    DP[startidx : rightend] = ["R"] * (seglen//2)
                    DP[i-(seglen//2)+1 : i+1] = ["L"] * (seglen//2)
                    startidx = i+1
                    hasRight = False
                else:
                    DP[startidx : i+1] = ["L"] * (i+1- startidx)
            elif Dlst[i] == "R":
                if hasRight:
                    DP[startidx : i] = ["R"] * (i - startidx)
                    startidx = i
                else:
                    hasRight = True
                    startidx = i
        
        if hasRight:
            DP[startidx : ] = ["R"] * (l - startidx)
        return "".join(DP)
        
        