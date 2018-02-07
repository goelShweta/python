class complex_no :
    def __init__(self,first,second,third,fourth):
        self.x=first
        self.y=second
        self.a=third
        self.b=fourth
    def addn_complex(self):
        z1=complex(self.x,self.y)
        z2=complex(self.a,self.b)
        real_prt=z1.real+z2.real
        img_prt=z1.imag+z2.imag
        z_res=complex(real_prt,img_prt)
        return z_res
    

comp_num=complex_no(3,4,5,6)
print(comp_num.addn_complex())

####################################################################
class complex2:
    def __init__(self,first,second):
        self.a=first
        self.b=second
    def addn(self,other):
        res=complex(self.a+other.a,self.b+other.b)
        return res


comp1=complex2(3,4)
comp2=complex2(5,6)

print(comp1.addn(comp2))

##############################################
class complex_no3 :
    def __init__(self,first,second):
        self.x=first
        self.y=second
        #self.a=third
        #self.b=fourth
    def addn_complex1(self,other):
        z1=complex(self.x,self.y)
        z2=complex(other.x,other.y)
        real_prt=z1.real+z2.real
        img_prt=z1.imag+z2.imag
        z_res=complex(real_prt,img_prt)
        return z_res
    
a1=complex_no3(3,4)
a2=complex_no3(5,6)
#comp_num1=complex_no3(3,4,5,6)
print(a1.addn_complex1(a2))

