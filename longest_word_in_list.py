
def longest_word(list1,pos,max_ele):
    #max_ele=list1[pos]
    if(pos==len(list1)):
        return max_ele
    else:
        if len(list1[pos])>len(max_ele) :
            max_ele=list1[pos]
            pos=pos+1
            return longest_word(list1,pos,max_ele)
        else:
            pos=pos+1
            return longest_word(list1,pos,max_ele)

list1=['abc','shweta','vipul','sandhya','ajay','nandini']
pos=1
max_ele=list1[0]
print(longest_word(list1,pos,max_ele))
