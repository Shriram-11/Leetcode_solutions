class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        if n<3:
            return 0
        if n==3:
            if s[0]==s[1]:
                return 1
            return 0
		occurences=dict()
        for i in range(n):
            a=s[i]
            if a in occurences:
                occurences[a][1]=i
            else:
                occurences[a]=[i,i]
        count=0
        for char in occurences:
            first=occurences[char][0]
            last=occurences[char][1]
            if last-first>1:
                vals=set()
                for i in range(first+1,last):
                    if s[i] not in vals:
                        vals.add(s[i])
                        count+=1
        return count
