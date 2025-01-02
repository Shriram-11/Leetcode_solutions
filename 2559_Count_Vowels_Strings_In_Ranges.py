class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
		n=len(words)
		l=[0]*n
		for i in range(n):
			if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
				l[i]=1
			if i>0:
				l[i]=l[i]+l[i-1]
				#store sum of srings with vowels upto i
		res=[]
		for q in queries:
			if q[0]==0:
				res.append(l[q[1]])
			else:
				res.append(l[q[1]]-l[q[0]-1])
		return res
		
