num = 2

while num < 10:
    if num == 2:
        print('print', num)
    num += 2
    print('prints', num)
print('prints Goodbye!')

num = 2
while num <= 10:
    print(num)
    num += 2
print('Goodbye!')

num = 10
print('Hello!')
while num >= 2:
    print(num)
    num -= 2

n = 1
y = 0
s = 0
while y < 6:
    total = n + y
    s += total
    y += 1

print(s)

total = 0
current = 1
end = 6
while current <= end:
    total += current
    print(total)
    current += 1
    print(current)
    
print(total)



iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 




x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    print(guess)
    if abs(guess**2 -x) >= epsilon:
        guess += step
        print(guess)

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))