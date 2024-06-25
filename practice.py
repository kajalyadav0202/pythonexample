# # # # # # # print("hellow,world")

# # # # # # num1=4.5
# # # # # # num2=5.6
# # # # # # sum=num1+num2
# # # # # # print("addition of two numbers is :",sum)

# num=int(input("enter the value of number"))
# square_root=num**0.5
# print("the square root of the number is %0.3f:" %square_root)

# #  len=int(input("enter the length of the triangle"))
# #  wit=int(input("enter the width of the triangle"))
# #  area=(len*wit)/2
# #  print("area of the triangle ios :",area)

# # # a=int(input("enter the value of a"))
# # # b=int(input("enter the value of b"))
# # # c=int(input("enter the value of c"))
# # # s=(a+b+c)/2
# # # area=(s*(s-a)*(s-b)*(s-c))**0.5
# # # print("semiperimeter is:",s)
# # # print("area of the traingle is %0.2f" %area)

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
d=(b**2)-4*a*c
s1=(-b+d**0.5)/2*a
s2=(-b-d**0.5)/2*a
print("the value of discriment is :",d)
print("solution  of quadratic equation is {0} and {1}".format(s1,s2))
