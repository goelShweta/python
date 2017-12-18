import power_fun

def armstrong(num):
    res1=int(num[0])
    num1=power_fun.power_fun(int(num[0]),3,res1)
    res2=int(num[1])
    num2=power_fun.power_fun(int(num[1]),3,res2)
    res3=int(num[2])
    num3=power_fun.power_fun(int(num[2]),3,res3)
    sum1=num1+num2+num3
    if(sum1==int(num)):
        return(" ARMSTRONG ")
    else:
        return(" NOT ARMSTRONG ")
    
num="153"
