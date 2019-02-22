# Conversion interger to binary


num = 3602879701896397

# Add Flag
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False

result = ''

if num == 0:
    result = '0'

while num > 0:
    result = str(num % 2) + result
    print(result)
    num = num//2
    print(num)

if isNeg:
    result = '-' + result

# Convert float to binary

x = 0.1

p = 0

while (x*(2**p)) % 1 != 0:
    print('Remainder = ' + str(x*(2**p) - int(x*(2**p))))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num//2

# Placeholder for binary points
for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + 
' is ' + str(result))




# BINARY: .0001100110011001100110011001100110011001100110011001101
# DECIMAL: 0.10000000000000000555

'''
>>> 0.1 == 0.10000000000000000555
True
'''

