
list_a = [1,2,3,4,5,6,7,8,9]
list_b = [1, 4, 9, 16, 25, 36, 49, 64, 81]
q = map(lambda a : a * a,list_a)
print(type(q))
q = list(q)
print(list(q))
print(list_b)
if list_b == q:
    print('相同')
else:
    print('不同')