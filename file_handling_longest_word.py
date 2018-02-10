def longest_word():
    '''
       finding longest word in a file'''
    with open('poem.txt','r') as rf:
        cont=rf.read()
        #print(cont)
        splitted=cont.split()  #splitting the text into list
        #print(splitted)
        max_len=len(splitted[0])  #storing len of 1st element as max length
        word=splitted[0]          #storing 1st word as longest word
        for i in splitted :
            if len(i)>max_len :   #comparing the elements with the 1st  
                max_len=len(i)
                word=i
            else:
                continue
        print("longest word is ",word)
        print("length is ",max_len)
        


print(longest_word())
