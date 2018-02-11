def flatten(list1,list2,pos):
    if len(list1)==pos:
        return list2
    else:
        if type(list1[pos])!=list:
            list2.append(list1[pos])
            pos=pos+1
            return flatten(list1,list2,pos)
        else:
            i=0                              #use in place of all this
            while i<len(list1[pos]):         #list2.extend(list1[pos])
                list2.append(list1[pos][i])  #
                i=i+1                        #
            pos=pos+1
            return flatten(list1,list2,pos)

list1=[1,2,[3,4],5,[7,8,9]]
list2=[]
pos=0
print(flatten(list1,list2,pos))
