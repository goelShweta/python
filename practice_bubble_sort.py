def bub(list1,pos):
    if len(list1)==pos :
        return list1
    else:
        pos2=0
        while pos2<len(list1)-1 :
            if list1[pos2]>list1[pos2+1]:
                temp=list1[pos2]
                list1[pos2]=list1[pos2+1]
                list1[pos2+1]=temp
                pos2+=1
            else:
                pos2+=1
                continue
        pos+=1    
        return(bub(list1,pos))    

l=[4,3,8,8,2,9,-1,1.4,6]
p=0
print(bub(l,p))
