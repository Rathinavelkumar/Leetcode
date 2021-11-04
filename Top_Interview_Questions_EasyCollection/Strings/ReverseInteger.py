x = 1563847412

sum=0
temp=abs(x)
while temp>0:
    sum = (sum*10) + (temp%10)
    temp //= 10

if sum >= -(2**31) and sum <= ((2**31)-1):
    if x<0:
        sum = -1 * sum
        print(sum)
    else:
        print(sum)
else:
    print(0)