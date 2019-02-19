# x is re-defined in scope of f
# different x objects

def f(y):
    x = 1
    x += 1
    print(x)


x = 5
f(x)
print(x)

# x from outside g
# x inside g is picked up from scope that called function g

def g(y):
    print(x)
    print(x + 1)

x = 5
g(x)
print(x)

# Local variable 'x' referenced before assignment

def h(y):
    x += 1

x = 5
h(x)
print(x)