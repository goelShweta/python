''' searching an element in the list'''

def search_fun(list1,ele,pos):
    '''
       objective:to search an element
    '''
    if(len(list1)==pos):
        return("ELE NOT FOUND")
    elif(list1[pos]==ele):
        return("ELE FOUND AT POSITION",pos)
    elif(list1[pos]!=ele):
        pos=pos+1
        return(search_fun(list1,ele,pos))

#global a
def search_fun2(list1,ele,a):
    #a=0
    '''
       objective:to search an element
    '''
    if(len(list1)==a):
        return("ELE NOT FOUND")
    elif(list1[0]==ele):
        return("ELE FOUND AT POSITION",a)
    elif(list1[0]!=ele):
        a=a+1
        return(search_fun2(list1[a:],ele,a))

list1=[1,2,3,4,5,6,7]
search_fun(list1,5,0)
print("************")
search_fun2(list1,7,0)
