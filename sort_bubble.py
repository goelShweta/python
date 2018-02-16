'''  sorting the list  by bubble sort '''

def bubble_sort(list1,pos):
    pos=pos+1
    if(len(list1)==pos):
        return(list1)
    else:
        i=0
        while(i<len(list1)-1) :
            if(list1[i]>list1[i+1]):
                temp=list1[i]
                list1[i]=list1[i+1]
                list1[i+1]=temp
            i=i+1    
        return(bubble_sort(list1,pos))        

list1=[80,50,40,90,20,10,50]
pos=0
bubble_sort(list1,pos)
