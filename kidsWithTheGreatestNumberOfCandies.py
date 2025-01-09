class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #the wording in this question is quite bad I had sloved the problem before but gave the wrong answer due to the stange explination.
        #simple for loop that checks to see if the candie in the list plus the extra candy is more then the max candie in the list.
        b=max(candies)
        a=[]
        for i in candies:
            #I simplfied the code so it can be done in less lines.
            #since > and < returns true or false you can write it in one line of code.
            a.append(i + extraCandies >= b)
        return(a)