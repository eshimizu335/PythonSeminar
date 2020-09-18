import copy
a = [[1,2],[3,4],[5,6],[7,8]]
b = copy.deepcopy(a)
print(b)
b.append([9,10])
print("b = ",b)
print("a = ", a)
