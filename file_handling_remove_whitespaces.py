def rem_spaces():
    '''
       removing the whitespaces
    '''
    with open('poem.txt','r') as rf :
    #rf=open('poem.txt','r')
        wf=open('remove_whitespaces','w')
        cnt=rf.read()
        split_txt=cnt.split()
        print(split_txt)
        for i in split_txt :
            wf.write(i)
        

    
    ##join_txt=split_txt.join()   join does not work on list
    ##print(join_txt)
        


print(rem_spaces())
