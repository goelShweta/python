def int_dict(d1,d2,d3,pos):
    if len(d1)==pos:
        return d3
    else:
        i=0
        while i<len(d2):
            key=list(d1.keys())[pos]
            if(key==list(d2.keys())[i]):
                d3[key]=int(list(d1.values())[pos])
                #d3[key]=int(list(d1.values())[pos])+int(list(d2.values())[i])
                i=i+1          #trial of sum of common ele #
            else:
                #key=list(d2.keys())[i]
                #d3[key]=list(d2.values())[i]
                i=i+1
                continue
        #key=list(d1.keys())[pos]
        #d3[key]=list(d1.values())[pos]    
        pos=pos+1
        return(int_dict(d1,d2,d3,pos))



d1={'a':'1','b':'2','c':'3'}
d2={'c':'3','d':'2'}
d3={}
pos=0
print(int_dict(d1,d2,d3,pos))
