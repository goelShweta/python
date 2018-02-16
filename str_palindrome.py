def str_rev(str1,str2,pos,i):
    if len(str1)==pos :
        if str2==str1 :
            return "palindrome"
        else: 
            return "not palindrome"
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
print("*******************************")
print(str_rev("abcba","",0,5))
