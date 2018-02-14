def ar_tri(h=4,b=3):
    '''
        objective: area of triangle
        input parameters:height and base
        return value: area of triangle
    '''
    #approach: not using recurrsion
    area = 1/2*h*b
    return(area)

def ar_tri_recc(h,b,hnew):   
    #using recurrsion
    assert h>=0 & b>=0 
    if b==0 :
        return(0)
    elif b==1 :
        return(hnew/2)
    else :
        hnew=hnew+h
        b=b-1
        return(ar_tri_recc(h,b,hnew))
        
