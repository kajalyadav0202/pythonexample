# # # # # # # # # # # # a=[2,3,5,6,56,78,"ddf"]
# # # # # # # # # # # # print(a)

# # # # # # # # # # # # # # # a=[2,3,4,56,74,34,2,45,]
# # # # # # # # # # # # # # # print(a.count (45)


# # # # # # # # # # # # # # a=[2,4,5,6,7,3,1,12,13,15,17]
# # # # # # # # # # # # # # # print(a[0])

# # # # # # # # # # # # # a=[2,4,5,12,13,15,17,23,2,3,4]
# # # # # # # # # # # # # print(a[4]*a[6])

# # # # # # # # # # # # a=[2,4,5,6,8,9,90,56,78,34,23,45]
# # # # # # # # # # # # a[4]=56
# # # # # # # # # # # # print(a[4])
# # # # # # # # # # # # a.insert(1,3)
# # # # # # # # # # # # print(a)


# # # # # # # # # # # # a=[2,4,45,4,6,43,23,33,12,13,15,16,27]
# # # # # # # # # # # # a[2]=6
# # # # # # # # # # # # a.insert(4,78)
# # # # # # # # # # # # print(a[7])

# # # # # # # # # # # a=[1,4,5,6,7,8,9,4,5]
# # # # # # # # # # # print(a)


# # # # # # # # # # a=[3,3,5,4,6,7,67,56,45,34,12,12,12,23,34,]
# # # # # # # # # # print(a.count(12) )

# # # # # # # # # a=[3,4,5,6,745,46,47,56,56,67,2,312,34,32,21,76,87]
# # # # # # # # # print(a[0:6])
# # # # # # # # # print(a[:6])
# # # # # # # # # print(a[0:])
# # # # # # # # # print(a[0::2])
# # # # # # # # # print(a.count(56))
# # # # # # # # # a.insert(5,89)
# # # # # # # # # print(a)
# # # # # # # # # print(a[7])

# # # # # # # # a=[1,2,3,4,5,6,7,8,9,0,2,3,23,3,243,54]
# # # # # # # # b=[3,4,5,3,423,32,43,54,65,76,87,98,21,]
# # # # # # # # # print(a+b)
# # # # # # # # # print(a*2)
# # # # # # # # # a.append(100)
# # # # # # # # # print(a)
# # # # # # # # # b.insert(4,78)
# # # # # # # # # print(b)
# # # # # # # # # a.pop()
# # # # # # # # # print(a)
# # # # # # # # b.remove(3)
# # # # # # # # print(b)
# # # # # # # # del a[4]
# # # # # # # # print(a)

# # # # # # # t=(1,2,3,4,5,6,7,8)
# # # # # # # print(t)
# # # # # # # print(t[0:4])
# # # # # # # a=list(t)
# # # # # # # # a.append(76)
# # # # # # # # print(a)
# # # # # # # a.extend([3,4,5])
# # # # # # # print(a)
# # # # # # # t=tuple(a)
# # # # # # # print(t)


# # # # # # s={10,3,4,8,9,50,11,12,15}
# # # # # # print(s)
# # # # # # s.add(20)
# # # # # # print(s)
# # # # # # s.pop()
# # # # # # print(s)
# # # # # # s.remove(9)
# # # # # # print(s)

# # # # # d={0:"rose", 1:"sunflower", 2:"lily", 3:"lotus"}
# # # # # print(d)
# # # # # print(d[2])


# # # # d={"name":"kajal", "age":20, "flower":"rose", "animal":"dog", "next":"text"}
# # # # print(d["animal"])
# # # # d.pop()
# # # # print(d)

# a=[1,2,3,4,5,6,7,8,9,12,23,13,14,25,16,17,18,19]
# # # print(a[-1:-4:-1])
# # # print(a[-1:-8:-3])
# # # add new element in list
# # a.insert(3,100)
# # print(a)
# # a.append(200)#add value at last position
# # print(a)
# # a.extend([2,45,67])# add more than one value at last
# # print(a)
# # c=[1,34,43,23,32,56,76]
# # a.extend(c) # adding two list
# # print(a)
# # a.append(c)
# # print(a)
# # a.remove(7) # delete the elemet that you mention
# # print(a)
# # a.pop() # delete the last value
# # print(a)
# # del a[6] # removing using index
# # print(a)
# # a[0]=110
# # print(a)

# a=[1,2,3,4,5,6,7,8,9,0]
# b=[12,12,32,14,15,16,17,18,19,34,23]
# print(a)
# print(b)
# print(a+b)
# print(a*2)

a=[2,4,34,54,23,12,13,14,151,6]
b=[33,44,55,66,77,88,99,221,11,31,21,41]
x=(1,2,3,4,5,6,74,35,36,43,23,43)
print(x[1:4])
print(x.index(23))
print(x[::-1]) #use to reverse the list and tuple
print(x)
print(sorted(a))# arrange the list
print(len(x)) # use to find the length of the list and tuple or number element in your list
d=b.copy() # copy the b list
e=b
b[0]=99
print(d,b,e)

