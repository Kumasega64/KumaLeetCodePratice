class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s != "":
            #We need to see if the first String can be found in the 2 string
            #first lets create a variable that tracks what of the first string has been found in the second
            p= 0
            #loop thorugh each charater in the t string
            for char in t:
                print(char)
                if char == s[p]:
                    print(s[p])
                    #if the first charater of s is found in the t incress the tracking varaible by 1
                    p+=1
                    if p == len(s):
                       return True
            else: 
                return False
        else:
            return True