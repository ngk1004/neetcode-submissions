class Solution:

    def encode(self, strs: List[str]) -> str:
        #res is set to an empty string
        res = ""
        #have a for loop itirate through the string
        for s in strs:
            res += str(len(s)) + '#' + s  #starts the algorithm to encode the string using hashes and 
        return res #returns the encoded string

    def decode(self, s: str) -> List[str]:
        res = [] #declare an emtpy array for the result to be returned
        i = 0 # I is to keep track of the spae we are at in the array?

        while i < len(s): # start a while loop to itirate througj the encoded string 
            j = i # set j = i to keep the encoded string untouched but copied to this variable
            while s[j] != '#': # nested while loop it go through and replace every letter with the true value o the string?
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res