def evil_no(num,pos,count):
    if pos==len(num):
        if count%2==0 :
            return("EVIL NUMBER")
        else:
            return("NOT EVIL NO")
    if num[pos]=='1' :
        count=count+1
        pos=pos+1
        return evil_no(num,pos,count)
    else:
        pos=pos+1
        return evil_no(num,pos,count)

num='1101010'
pos=0
count=0
print(evil_no(num,pos,count))

####################################
def evil2(num,count):
    #count=0
    if num!=0:
        if num%2==1:
            count+=1
            num=num//2
        else:
            num=num//2
        return evil2(num,count)
    else:
        #print(count)
        if count%2==0:
            return "evil"
        else:
            return "not evil"
        
num=21
#pos=0
count=0
print(evil2(num,count))
