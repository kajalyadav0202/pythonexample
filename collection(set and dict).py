# # set is collection of data but it does not have index
# # dublicate value can not add not allowed
# # it suffled and try to arrange the set in assending order only try not compalsory
# s={12,23,22,21,34,33,45,55,54,56,57}
# print(s)
# s.add(13)
# print(s)
# s.update([10,20,30])
# print(s)
# s.pop() # delete value from first position
# print(s)
# s.remove(21)
# print(s)

# dict is also collection of data and accept value in pair frim first is 
# Index called key andv sceond is value of element

d={1: "delhi", 2: "bhopal", 3:"mumbai", 4: "goa", 5: "jaipur"}
print(d[1])
print(d.get(2))

l=[1,2,3,4,5]
l2=["a","b","f","s","d","g"]
d2=dict(zip(l,l2))
print(d2,d)