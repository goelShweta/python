def count_words():
    '''
       removing whitespace from the file and coping into another file
    '''
    with open('poem.txt','r') as rf :
    #wf=open('white_space_copy','w')
        wrd_cnt=0
        vowel_cnt=0
        alpha_cnt=0
        you_cnt=0
        cont=rf.readline()
        while(cont) :
            splitted= cont.split(" ")    #splitting one line into words
            for i in splitted :
                if i[0]=='a'or i[0]=='A' or i[0]=='e' or i[0]=='E'or i[0]=='i'or i[0]=='I'or i[0]=='o'or i[0]=='O'or i[0]=='u'or i[0]=='U' :
                    vowel_cnt=vowel_cnt+1 #counting words starting with vowels
            ##############################counting occurences of word "you"
                if i=="you" or i=="YOU" or i=="You" :
                    you_cnt=you_cnt+1

            ########################## counting alphabets
            
                alphabets=i.split()
                print(alphabets)
                for j in alphabets :
                    alpha_cnt=alpha_cnt+len(j)
            ############################################ 
                
                wrd_cnt=wrd_cnt+1    #counting total no. of alphabets
            print(splitted)
            cont=rf.readline()
        print(wrd_cnt)
        print(vowel_cnt)
        print(alpha_cnt)
        print(you_cnt)

print(count_words())
