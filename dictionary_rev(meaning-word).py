def dict_rev(dict1,dict2,pos):
    '''
       reversing dictonary
       meaning:word
    '''
    if len(dict1)==pos :
        return dict2
    else:               
        value=list(dict1.values())[pos]
        dict2[value]=list(dict1.keys())[pos]
        pos=pos+1
        return(dict_rev(dict1,dict2,pos))
        
            


dict1={"morning":"early","evening":"dawn","b":"cde","a":"abc"}
dict2={}
pos=0
print(dict_rev(dict1,dict2,pos))
