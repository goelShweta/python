def sum_flatten(list1,list2,pos,sum1):
    '''
         sum of elements of list in list
    '''
    if len(list1)==pos:
        return sum1
    else:
        if type(list1[pos])!=list:
            list2.append(list1[pos])
            sum1=sum1+list1[pos]
            pos=pos+1
            return sum_flatten(list1,list2,pos,sum1)
        else:
            i=0
            while i<len(list1[pos]):
                list2.append(list1[pos][i])
                sum1=sum1+list1[pos][i]
                i=i+1
            pos=pos+1
            return sum_flatten(list1,list2,pos,sum1)

list1=[1,2,[3,4],5,[7,8,9]]
list2=[]
pos=0
sum1=0
print(sum_flatten(list1,list2,pos,sum1))
