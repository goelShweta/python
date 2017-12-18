def possible_comb(list1,list2,list3):
    '''
       printing all the combinations of the three lists
    '''
    pos=0
    while pos<len(list1):
        pos2=0
        while pos2<len(list2):
            pos3=0
            while pos3<len(list3):
                print(list1[pos]+list2[pos2]+list3[pos3])
                pos3=pos3+1
            pos2=pos2+1
        pos=pos+1

list1=[' I ',' You ']
list2=[' like ',' love ']
list3=[' football ',' programming ']
print(possible_comb(list1,list2,list3))
