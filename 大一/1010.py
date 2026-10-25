def grade(score:int):
    if score>100 or score<0:
        return 'Invalid score'
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    elif score >=0:
        return 'F'
print(str(grade(95)))
def digit_sum(n:int):
    if n<0:
        return 'Invalid number'
    total=0
    while n>0 and n%1==0:
        total += n%10
        n //= 10
    return total
print(int(digit_sum(12345)))
def is_prime(n:int):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(7))
def collatz_step(n:int):
    if n<=0:
        return 'Invalid number'
    steps=0
    while n != 1:
        if n%2==0:
            n //=2
        else:
            n = 3*n + 1
        steps += 1
    return steps
print(int(collatz_step(6)))
def collatz_step():
    max_steps=0
    max_n=1
    for n in range(1,1001):
        original_n=n
        steps=0
        while n != 1:
            if n%2==0:
                n //=2
            else:
                n = 3*n + 1
            steps += 1
        if steps > max_steps:
            max_steps = steps
            max_n=original_n
    return max_n, max_steps
print(collatz_step())
def triangle(n:int):
    if n==0:
        return ""
    if n<1:
        return 'Invalid number'
    row=""
    for i in range(1,n+1):
        row +='*'*i +"\n"
    row=row[:-1]
    return row
print(triangle(5))
def hanoi_steps(n:int):
    if n==0:
        return 0
    if n<1:
        return 'Invalid number'
    steps=0
    for i in range(1,n+1):
        steps=2*steps+1
    return steps
print(hanoi_steps(10))
def initials(full_name:str):
    initials=""
    for i in full_name.split():
        initials += i[0].upper()+"."
    return initials
print(initials("Zhang San Feng"))
def caesar(text:str,k:int):
    k=k%26
    result=""
    for i in text:
        if ord(i)<65 or (90<ord(i)<97) or ord(i)>122:
            result +=i
        if 65<=ord(i)<=90:
            if ord(i)+k>90:
                result += chr(ord(i)+k-26)
            else:
                result += chr(ord(i)+k)
        elif 97<=ord(i)<=122:
            if ord(i)+k>122:
                result += chr(ord(i)+k-26)
            else:
                result += chr(ord(i)+k)
    return result
print(caesar("xyz", 3))
def to_base(n:int,b:int):
    num=""
    if n==0:
        return "0"
    if n<0 or b<2 or b>16:
        return 'Invalid number or base'
    while n>0:
        if n%b<10:
            num = str(n%b)+num
        else:
            num = chr(n%b-10+ord('A'))+num
        n//=b
    return num
print(to_base(255,16))
import math
def leibniz(n:int):
    p=0
    for i in range(1,n+1):
        p+=1/((2*i-1)*((-1)**(i+1)))
    pi=4*p
    return pi
print(abs(leibniz(10000000)-math.pi))
import random
def monte_carlo(n:int):
    inside=0
    for i in range(n):
        x,y=random.random(),random.random()
        if x**2+y**2<=1:
            inside +=1
    return 4*inside/n
print(abs(monte_carlo(10000000)-math.pi))