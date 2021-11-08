class Solution:
    def myAtoi(self, s: str) -> int:
        data = s.strip().split(" ")[0]

        sign=[]
        result=[]
        active_flag=False
        for each in data:
            if (each=='+' or each=="-") and len(sign)==0:
                if active_flag==False:
                    sign.append(each)
                    continue
                else:
                    break
            if not each.isnumeric():
                break
            else:
                active_flag=True
                if len(result)==0 and each=='0':
                    continue
                else:
                    result.append(each)


        if len(result)>0:
            sign.extend(result)
            output = int("".join(sign))
            if output < -2**31:
                return(-2**31)
            elif output > (2**31)-1:
                return((2**31)-1)
            else:
                return(output)
        else:
            return(0)