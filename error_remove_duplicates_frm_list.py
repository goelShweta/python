def duplicate(list1,pos,n):
    if pos!=len(list1) :
        i=1
        while i<n:
            count=0
            if list1[0]==list1[i] :
                count=count+1
                list1.remove(list1[i])
                temp=list1[0]
                list1[0]=list1[i-1]
                list1[i-1]=temp
                i=i+1
            else:
                i=i+1
                continue
            n=len(list1)
            pos=pos+1
            list1=list1[1:]
            return duplicate(list1,pos,n)
    else:
        return list1

list1=[1,2,3,1,4,5,6,7,5,3,6]
pos=0
print(duplicate(list1,pos,11))
