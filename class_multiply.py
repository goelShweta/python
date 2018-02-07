class multiply:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    #def multi(self,a,b):
    def multi(self):    
        #c=a*b                       #can be able to give arguments acco. to us
        c=self.first*self.second     #parameters used here are of init function
        return c


res=multiply(2,4)  #res is a obj
#print(res.multi(res.first,res.second))
print(res.multi())
