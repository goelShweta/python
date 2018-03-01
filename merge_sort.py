def merge_sort(l1,l2,l3,p1,p2):
    if((p1==len(l1))and(p2==len(l2))):
        return l3
    else:
        if len(l1)==p1:
            l3.append(l2[p2])
            p2+=1
        elif len(l2)==p2:
            l3.append(l1[p1])
            p1+=1
        elif l1[p1]<l2[p2]:
            l3.append(l1[p1])
            p1+=1
        elif l2[p2]<l1[p1]:
            l3.append(l2[p2])
            p2+=1
        elif l2[p2]==l1[p1]:
            l3.append(l2[p2])
            l3.append(l1[p1])
            p1+=1
            p2+=1
        return merge_sort(l1,l2,l3,p1,p2)    
    

l1=[1,2,5,9,12]
l2=[3,5,7,10]
l3=[]
p1,p2=0,0
print(merge_sort(l1,l2,l3,p1,p2))
