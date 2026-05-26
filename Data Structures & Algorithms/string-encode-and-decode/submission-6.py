class Solution:
    def encode(self, strs):
        encoded = []
        
        for s in strs:
            # Prefix each string with its length and a delimiter
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        
        return "".join(encoded)

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            # Read the length prefix
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            
            # Move past the delimiter and extract the string
            i = j + 1
            res.append(s[i:i + length])
            i += length
        
        return res