class Solution:

    def encode(self, strs: List[str]) -> str:
        #["Hello","World"]
        #5$Hello5$World
        output = ""
        for str1 in strs:
            output+=str(len(str1))+"$"+str1
        return output

    def decode(self, s: str) -> List[str]:
        #read the string until we get a $
        #Store the length, read upto the length. 
        #add to list
        #5$Hello5$World
        cLen=''
        iLen=0
        output=[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "$":
                cLen+=s[j]
                j=j+1
            iLen=int(cLen)
            i=j
            cLen=''
            str1=""
            for k in range(j+1, j+iLen+1, 1):
                str1 = str1+s[k] 
            output.append(str1)
            i=i+iLen+1
        return output








