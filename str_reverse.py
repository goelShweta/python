def str_rev(str1,str2,pos,i):
    if len(str1)==pos :
        return str2
    else:
        a=str1[i-1]
        str2=str2+a
        pos=pos+1
        i=i-1
        return str_rev(str1,str2,pos,i)

str1="shweta"
str2=""
pos=0
i=6
print(str_rev(str1,str2,pos,i))
        

#passing length of string in i
#pos is for counting no. of loop iterations
