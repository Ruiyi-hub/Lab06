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
print(int(collatz_step(27)))
def collatz_step():
    max_steps=0
    max_n=1
    for n in range(1,1001):
        original_n=n
        steps=0
        while n!=1:
            if n%2==0:
                n //=2
            else:
                n=3*n+1
            steps +=1
        if steps>max_steps:
            max_steps=steps
            max_n=original_n
    return max_n, max_steps
print(collatz_step())
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(7))
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return f"{n} is not a prime number"
    return f"{n} is a prime number"
print(is_prime(7))
def describe(name,age,city):
    return f"My name is {name},{age},{city}"
print(describe("Alice",25,"New York"))
def total(*numbers):
    print(numbers)
    return sum(numbers)
print(total(1,2,3,4,5))
def show(first,*args,**kwargs):
    print(first)
    print(args)
    print(kwargs)
show(1,2,3,4,name="Alice",age=25)
a, b = 0b1100, 0b1010
print(f"~a={~a:04b}")