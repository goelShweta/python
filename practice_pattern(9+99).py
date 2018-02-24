def patt(num,sum1):
    if num!=0:
        print(num," "," + ",)
        sum1=sum1+num
        num=num//10
        return(patt(num,sum1))
    else:
        return(sum1)

num=999
s=0
print(patt(num,s))




##example

list1=[1,2,[3,4],5]
list2=[]
print(list2.append(list1[0]))
