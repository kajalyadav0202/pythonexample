a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
if (a>b):
    if(a>c):
        print("a is greater than b and c")
    else:
        print("c is greater then a and b")
elif(b>c):
    print("b is greater then a and c")
else:
    print("c is greater then a and b")
