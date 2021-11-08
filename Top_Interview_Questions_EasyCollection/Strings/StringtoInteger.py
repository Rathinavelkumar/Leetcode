s = "-0000042a1234"

if " " in s.strip():
    data = s.strip().split(" ")[0]
else:
    data = s
result=[]
sign=[]
int_flag=False
for each in data:
    if each=='+' or each=='-':
        if len(sign)!=0:
            break
        else:
            if int_flag==False:
                sign.append(each)
                continue
            else:
                break
    if each.isdigit():
        int_flag=True
        if each=='0' and len(result)==0:
            continue
        else:
            result.append(each)
    if int_flag==True and not each.isdigit():
        if each=='+' or each=='-':
            result=[]
            break
        else:
            break

if len(result)>0:
    sign.extend(result)
    output = int("".join(sign))
    if output < -2**31:
        print(-2**31)
    elif output > (2**31)-1:
        print((2**31)-1)
    else:
        print(output)
else:
    print(0)