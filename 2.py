

def login():
    a=150
    b=123456

    print('请输入用户名')
    a_a=input()
    a_a=int(a_a)
    print('请输入密码')
    b_b=input()
    b_b = int(b_b)
    if a == a_a  and b == b_b:
        print('正确')
    else:
        print('错误')

def sum(x,y):
    count=x+y
    count= int(count)
    return count

login()

print(sum(2,6))