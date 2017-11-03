#import pdb
#pdb.set_trace()

def merge(list1,list2,list3,i,j):
    '''
       objective:to merge the two sorted list
       input parameters: two sorted list and an empty list
       result:a sorted list after merging
    '''
    len1=len(list1)
    len2=len(list2)
    if (i==len1 and j==len2) :
        return list3
    elif i==len1-1 :
        list3.append(list2[j])
        j=j+1
        return(merge(list1,list2,list3,i,j))
    elif j==len2-1 :
        list3.append(list1[i])
        i=i+1
        return(merge(list1,list2,list3,i,j))
    elif list1[i]<list2[j] :
        list3.append(list1[i])
        i=i+1
        return(merge(list1,list2,list3,i,j))
    elif list2[j]<list1[i] :
        list3.append(list2[j])
        j=j+1
        return(merge(list1,list2,list3,i,j))
    elif list1[i]==list2[j] :
        list3.append(list1[i])
        i=i+1
        return(merge(list1,list2,list3,i,j))
    
       
list1=[1,3,6,8,10,12,14]
list2=[2,5,7,12]
list3=[]
i=0
j=0
print(merge(list1,list2,list3,i,j))
       
       
       
