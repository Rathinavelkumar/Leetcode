class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        temp = abs(x)
        while temp>0:
            sum = (sum*10) + (temp%10)
            temp = temp//10
        
        if sum >= -(2**31) and sum <= ((2**31)-1):
            if x<0:
                sum = -1*sum
                return sum
            else:
                return sum
        else:
            return 0