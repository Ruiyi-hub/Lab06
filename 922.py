print("""        (()__(()
        /       \\
       ( /    \\  \\
        \\ o o    /
        (_()_)__/ \\
       / _,==.____ \\
      (   |--|      )
      /\\_.|__|'-.__/\\_
     / (        /     \\
     \\  \\      (      /
      )  '._____)    /
   (((____.--(((____/""")
print(chr(ord('A')+32))
print(ord('y'))
print(bin(121))
print(oct(121))
print(hex(121))
print(chr(121))
print(chr(121-32))
a=3
b=4
c=5
s=(a+b+c)/2
c=(s*(s-a)*(s-b)*(s-c))**0.5
print("s=",s,"c=",c)
a=0.3
b=0.4
c=0.5
s=(a+b+c)/2
c=(s*(s-a)*(s-b)*(s-c))**0.5
print("s=",s,"c=",c)
print(abs(0.3-(0.2+0.1))<1e-9)
print(8/4)
print(8//4)
print(8.0/4)
print(8%3)
print(-8%3)
print(-8//3)
print(2**10)
print(2**-2)
print(2**0.5)
print("true"+"true")
print(0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(f"{0.3:.20f}")
print(f"{0.1 + 0.3:.20f}")
print(f"{0.4:.20f}")
print(0.4+0.2==0.6)
print(0.8+0.4==1.2)
print(1e15 + 1 == 1e15)
print(1e16 + 2 == 1e16)
def to_lower(ch):
    if 'A' <= ch <= 'Z':
        return chr(ord(ch) + 32)
    return ch
print(to_lower('a'))
a=0.3
b=0.2+0.1
print(abs(a-b)<1e-9)
def almost_equal(a,b,eps=1e-9):
    return abs(a-b)<eps
print(almost_equal(0.3, 0.2 + 0.1))
def roots(a,b,c):
    d=(b**2-4*a*c)**0.5
    大根=(-b+d)/(2*a)
    小根=(-b-d)/(2*a)
    return 大根,小根
print(roots(1,2,1))
def to_lower(letter):
    if ord('A')<=ord(letter)<=ord('Z'):
        return chr(ord(letter)+32)
    else:
        return letter
print(to_lower('a'))
def almost_equal(a,b,eps=1e-9):
    return abs(a-b)<eps
print(almost_equal(0.3,0.2+0.1))
def roots(a,b,c):
    d=(b**2-4*a*c)**0.5
    if d>=0:
        大根=(-b+d)/(2*a)
        小根=(-b-d)/(2*a)
        return 大根,小根
    else:
        return None,None
print(roots(1,2,1))