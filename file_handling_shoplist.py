import pickle
def inp(fin):
    f=input("enter num")
    if f=="exit":
        return
    pickle.dump(f,fin)
    inp(fin)

def shoplist():
    fin=open("shoplist.txt",'wb')
    inp(fin)
    fin.close()
    
shoplist()    
       
def load_shop():
    fout=open("shoplist.txt",'rb')
    #while fout!='NULL':--------error----out of input
    print(pickle.load(fout))
    print(pickle.load(fout))
    
    fout.close()

load_shop()    
