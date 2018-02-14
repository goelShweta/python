def sum_fun(*var):
    '''
       objective: to print the sum of variables
    '''
    sum=0
    for i in var :
        sum=sum+i
    print(sum)

#*************************************************
def sum_fun2(a,b,c):
    '''
       printing the elements
    '''   
    sum=0
    sum=a+b+c
    return sum

d=[10,20,30]
print(sum_fun2(d[0],d[1],d[2]))
print(sum_fun2(*d))
