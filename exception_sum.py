def addn(a,b):
    try:
        c=a+b
    except ValueError:   
        print("invalid format")
    except:
        print("erroe")
    return c

print(addn(2,3))
print(addn(0))
