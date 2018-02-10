import pickle 
def shoplist():
    '''
       prog ask for user input and adds the input word to shopping list.
       stop reading when "exit " is typed.
       update list using pickle method
    '''
    with open('shoplist.txt','wb') as rf:
        a={"abc","def"}
        pickle.dump(a,rf)
    with open('shoplist.txt','rb') as wf:
        b=pickle.load(wf)
        print(b)
    

print(shoplist())        
