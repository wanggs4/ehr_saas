
def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1)
    print(n)



print(fact(5))


# fact(5)
# 5 * fact(4)     20
# 5 * (4 * fact(3)) 60
# 5 * (4 * (3 * fact(2)))   120
# 5 * (4 * (3 * (2 * fact(1)))) 120
# 5 * (4 * (3 * (2 * 1)))  120
# 5 * (4 * (3 * 2))  120
# 5 * (4 * 6) 120
# 5 * 24 120
# 120



