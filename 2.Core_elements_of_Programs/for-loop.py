import sys
for count in range(11):
    if count != 0 and count % 2 == 0:
        print(count)
print('Goodbye!')

for count in range(2, 12, 2):
    print(count)
print('Goodbye!')

print('Hello!')
for i in range(10, 0, -2):
    print(i)

total = 0
end = 3
for current in range(1, end+1):
    total += current
    print(total)
print(total)

total = end
for current in range(end):
    total += current
print(total)


num = 10
for num in range(5):
    print(num)
print(num)


divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
        print(numVowels)
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1
        print(numCons)

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))


count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))

# Problem 1
countVow = 0
s = 'azcbobobegghakl'
for letter in s:
    if letter in ('a', 'e', 'i', 'o', 'u'):
        countVow += 1
print('Number of vowels: ', countVow)

# Problem 2
bobCount = 0
n = 0
i = 3
s = 'boboboobobboboboboobobbbobobobobob'

while i <= len(s):
    if s[n:i] == 'bob':
        bobCount += 1
    n += 1
    i += 1

print('Number of times bob occurs is: ', bobCount)

# Problem 3:
''''
programming pattern that comes up where you have to walk 
pairwise through a string or list (or any other iterable, really). 
One way to do so is to first seed a temporary buffer with 
the first item, then walk over the rest of the iterable, 
comparing each item to the buffer. On certain conditions, 
here out of ordered letters, you reset the buffer to the 
new current 
'''

s = 'ciao'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i_s = []
i_a = []
index = 0

for i in range(len(s)):
    index = 0
    while index < len(alphabet):
        if s[i] == alphabet[index]:
            i_s.append(i)
            i_a.append(index)
        index += 1

outputString = s[0]
tempString = outputString
tempInter = i_a[0]

for i in range(1, len(i_a)):
    if i_a[i] >= tempInter:
        tempInter = i_a[i]
        tempString += s[i]
        if len(tempString) > len(outputString):
            outputString = tempString
    else:
        tempInter = i_a[i]
        tempString = s[i]

print('Longest substring in alphabetical order is: ', outputString)


outputString = s[0]  # accumulative
tempString = outputString  # placeholder

for i in range(1, len(s)):
    if s[i] >= tempString[-1]:
        tempString += s[i]
        if len(tempString) > len(outputString):
            outputString = tempString
    else:
        tempString = s[i]

print('Longest substring in alphabetical order is: ', outputString)
