import inc_dec_fun

def sum_inc(first,sec) :
    '''
        objective: find sum of 2 no.s using increment 
        input parameters: the two no.s to be added
        return value: sum of the no.s
    '''
    #approach: not using recurrsion
    if sec==0 :
        return(first)
    else:
        first=inc_dec_fun.inc(first)
        sec=sec-1
        return sum_inc(first,sec)
