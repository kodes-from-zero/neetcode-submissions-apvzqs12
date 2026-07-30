class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output+=str(len(s))+"#"+s
        return output
    def decode(self, s: str) -> List[str]:
        pos=0
        leng=0
        result=[]
        while pos!=len(s):
            curr_len=""
            current = pos
            while(s[current]!="#"):
                curr_len+=s[current]
                current+=1
            leng=int(curr_len)
            word = s[current+1:current+leng+1]
            result.append(word)
            pos=leng+current+1
        return result



    
