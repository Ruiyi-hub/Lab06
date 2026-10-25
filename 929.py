def c_to_f(c):
    f=c*9/5+32
    return round(f,1)
print(c_to_f(37))
def mask_id(sid):
    if len(sid)<8:
        return sid
    else:
        return f"{sid[0:4]}{'*'*(len(sid)-8)}{sid[-4:]}"
print(mask_id('12345678'))
def format_row(name,score):
    return f"{name:<10}{score:>6.1f}"
print(format_row('jessica',99.5))
def average(a, b):
    return (a+b)/2
result = average(10, 20) * 2
print(result)
def read_int(prompt):
    print(type(prompt))
    return int(input(prompt))
print(read_int("please input an integer:"))
def stats(a,b,c):
    return min(a,b,c),max(a,b,c),(a+b+c)/3
lower,high,mean=stats(3,9,5)
print(lower,high,mean)
def area(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
print(area(3,4,5))
def circles(a,b,c):
    s=(a+b+c)/2
    S=area(a,b,c)
    R=a*b*c/(4*S)
    r=S/s
    return R,r
print(circles(3,4,5))
a=int(input("please input a:"))
b=float(input("please input b:"))
c=input("please input c:")
print(type(a))
print(type(b))
print(type(c))
print(a,b,c)
def parse(record):
    record=record.split(',')
    name=record[0]
    score=float(record[1])
    return name, score
print(parse("张三,87.5"))
print(parse("欧阳修远,92"))
print(format_row(*parse("张三,87.5")))
print(format_row(*parse("欧阳修远,92")))
print(format_row(*parse("李四,65.25")))