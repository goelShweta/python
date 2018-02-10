def copy_file():
    '''
       removing whitespace from the file and coping into another file
    '''
    with open('poem.txt','r') as rf :
        with open('poem_copy','w') as wf :
            cont=rf.readline()
            while(cont) :
                wf.write(cont)
                cont=rf.readline()
    


print(copy_file())
