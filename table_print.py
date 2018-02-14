def table(num,i):
    if i<=10 :
        print(num," ","*"," ",i," ","="," ",num*i)
        i=i+1
        return table(num,i)
    else:
        return
table(10,1)
