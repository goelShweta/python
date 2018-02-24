def palindrme(list1,pos,res):
    if len(list1)//2==pos :
        return res
    else:
        if pos<len(list1)/2 :
            if list1[pos]==list1[-(pos+1)] :
                pos=pos+1
                res='palindrome'
                return(palindrme(list1,pos,res))
            else:
                return("not palindrome")


l=[1,3,3,2,1]
p=0
res=''
print(palindrme(l,p,res))            
