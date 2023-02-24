# print('hello wor

def greet(fx):
    def df(*args, **kwargs):
        print('Good morning')
        fx(*args, **kwargs)
        print("thanks for using this function!")
    return df
# @greet
def hello():
    print('Hello world')

# @greet
def add(*args, **kwargs):
    x=0
    for element in args:
        x=x+element
    print(x)
    print(type(args))
    print(args)
    sum =0
    for key,val in kwargs.items():
        sum=sum+val
    print(type(kwargs) , 'and', 'sum=',sum)
    print(kwargs)
dict = {'a':3,'b':5}
# tup = 1,2,3,4,5,6,7
add(1,2,3,4,5,6,7,a=3,b=5)
# add(tup)
# add(dict)
# add(2,3)