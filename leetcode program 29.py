#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
#The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits. only issue i faced was how to do +1 if  testcase is 999. it was important part of the program.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            digits[i] += 1
            if digits[i] <10:
                return digits
            digits[i]=0
        return [1]+digits
