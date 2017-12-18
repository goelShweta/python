def ar_rect(l=4,b=3):
    '''
        objective: area of rectangle
        input parameters:length and breadth
        return value: area of rectangle
    '''
    #approach: not using recurrsion
    area = l*b
    return(area)

def ar_rect_recc(l,b,lnew):   
    #using recurrsion
    assert l>=0 & b>=0 
    if b==0  :
        return(0)
    elif b==1 :
        return(lnew)
    else :
        lnew=lnew+l
        b=b-1
        return(ar_rect_recc(l,b,lnew))
        
