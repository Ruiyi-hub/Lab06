s='a'
s=s.upper()
print(s)
a,b=1,2
a,b=b,a
print(a,b)
x=4
x+=3
x-=2
x//=2
x*=3
print(x)
first='shanghai'
second='jiaotong'
print(first+' '+second)
print('-'*30)
print(str(123)+'!')
print(int('3'))
print(int(float('3.14')))
pi=3.1415926
print(f"{pi:.2f}")
print(f"{1/3:.3%}")
print(f"{pi:0<10.2f}")
print(f"{'name':<8}{'score':>8}")
x=1
print(f"{x=}")
def area_of_circle(r):
    return 3.1415926*r*r
print(area_of_circle(2))
def hi(name):
    print('greeting')
    print(f"hi,{name}")
hi('jessica')
def hi(name):
    return f"hi,{name}"
print(hi('jessica'))
def say_bye():
    return "bye"
print(say_bye())
def no_return():
    return f"this function has no return value"
print(no_return())