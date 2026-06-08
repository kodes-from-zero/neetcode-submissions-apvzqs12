class Solution:

    def encode(self, strs: List[str]) -> str:
        output_string=""
        for i in range(len(strs)):
            len1 = len(strs[i])
            output_string+= str(len1)+'#'+strs[i]
        return output_string

    def decode(self, s: str) -> List[str]:
        strs = []
        i=0
        len1=""
        j=0
        while i<len(s):
            while(s[i] != '#'):
                len1+=s[i]
                i+=1
            length = int(len1)
            i+=1
            word = s[i:i+length]
            strs.append(word)
            len1=""
            i += length  
        return strs



