import time

def function(func):
    def passs(*w):
        print(time.time())
        func(*w)
    return passs


@function
def test_function(test1):
    print('this is function' + test1)

@function
def test_function1(test1,test2):
    print('this is function' + test1)
    print('this is function' + test2)

@function
def async1():
    pass