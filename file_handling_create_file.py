def create_file():
    '''
       creating a file poem.txt
    '''
    f = open('poem.txt','w')
    f.write('my name is shweta /n she is beautiful /n apple mango banana')
    #print(f.read())

    #f.read(10)  mode is write only not read



print(create_file())
