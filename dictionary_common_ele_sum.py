def dict_add(dict1,dict2,dict3,pos1,pos2):
    '''
       intersecting two dictonary
       first : adding elements of 1st list and then of second list
       the same key value pairs value willbe added together
    '''
    #if len(dict1)==pos1 and len(dict2)==pos2 :
     #   return dict3
    #else:
    while(pos1<len(dict1)):  #finding the common keys from 2 dict and then adding value of both and
        pos2=0               #store the updated value in dict1
        while(pos2<len(dict2)):
            if list(dict1.keys())[pos1]==list(dict2.keys())[pos2] :
                dict1[list(dict1.keys())[pos1]]=list(dict2.values())[pos2]+list(dict1.values())[pos1]
                #dict2[list(dict1.keys())[pos2]]=list(dict2.values())[pos2]+list(dict1.values())[pos1]
                #del dict1[list(dict1.keys())[pos1]]
                #del dict1[list(dict1.keys())[pos1]]
                #del dict2[list(dict2.keys())[pos2]]
            pos2=pos2+1
        pos1=pos1+1
        
    pos1=0
    pos2=0
    
    while(pos2<len(dict2)) :              #adding all the values of dict2 first
        key=list(dict2.keys())[pos2]
        dict3[key]=list(dict2.values())[pos2]
        pos2=pos2+1
        
    while(pos1<len(dict1)) :              #adding values of dict2 and updating the common values
        key=list(dict1.keys())[pos1]
        dict3[key]=list(dict1.values())[pos1]
        pos1=pos1+1
    
    return(dict3)    
                        
                    
dict1={"morning":100,"evening":100,"b":200}
dict2={"a":300,"b":200,"evening":300}
dict3={}
pos1=0
pos2=0
#pos=0
print(dict_add(dict1,dict2,dict3,pos1,pos2))
