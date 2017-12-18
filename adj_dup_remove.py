def adj_dup(list1,i):
    if i==len(list1):
        return list1
    else:
        if i<len(list1)-1 :
            if list1[i]==list1[i+1] :
                list1.pop(list1[i])
                i=i+1
                adj_dup(list1,i)
            else:
                i=i+1
                adj_dup(list1,i)
        else:
             return list1

l=[1,2,2,2,2,2,8,9,5]
i=0
print(adj_dup(l,i))
print(l)
            
