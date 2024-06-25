maths=int(input("enter the marks of maths"))
physics=int(input("enter the marks of physic"))
chemistry=int(input("enter the marks of  chemikstry"))
english=int(input("enter the marks of english"))
computer=int(input("enter the marks of computer"))
count=0
if maths<33:
    count=count+1
    print("fail in maths")
if physics<33:
    print(" fail is physics")
    count=count+1
if chemistry<33:
    print("fail in chemistry")
    count=count+1
if english<33:
    print("fail in english")
    count=count+1
if computer<33:
    print("fail in computer")
    count=count+1


if count==0:
    print("pass in all subject")
else:
    print("fail in ",count,"subjects")    