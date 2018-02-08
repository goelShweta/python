def dict_inter(dict1,dict2,dict3,pos1,pos):
    '''
       intersecting two dictonary
       first : adding elements of 1st list and then of second list
       the same key value pair will be replaced
    '''
    if len(dict1)==pos1 and len(dict2)==pos :
        return dict3
    else:               
        if pos<len(dict2):
            key=list(dict2.keys())[pos] #taking value of key from dict1
            dict3[key]=list(dict2.values())[pos] #put the key and the corresponding value in dict3
            pos=pos+1
            return(dict_inter(dict1,dict2,dict3,pos1,pos))
        else:
            key=list(dict1.keys())[pos1]
            dict3[key]=list(dict1.values())[pos1]
            pos1=pos1+1
            return(dict_inter(dict1,dict2,dict3,pos1,pos))


dict1={"morning":"early","evening":"dawn","b":"cde"}
dict2={"a":"abc","b":"cde","evening":"dawn"}
dict3={}
pos1=0
#pos2=0
pos=0
print(dict_inter(dict1,dict2,dict3,pos1,pos))
