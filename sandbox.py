
# Problem 1

s = 'azcbobobegghakl'

count = 0

for i in s:
    if i in 'aeiou':
        count += 1

print('Number of vowels: ' + str(count))

# Problem 2

s = 'azcbobobegghakl'
count = 0

for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        count += 1
    i += i

print('Number of times bob occurs is: ' + str(count))

# Problem 3

s = 'fvpwhwyfpblawzxhzzryzlqa'
s = 'jhmihplibmftflp'
s = 'zyxwvutsrqponmlkjihgfedcba'
substring = s[0]
longest = s[0]

for i in range(1, len(s)):
    if s[i-1] <= s[i]:
        substring += s[i]
        print('Subs: ' + str(substring))
        # compare the longest string
        if len(substring) > len(longest):
            longest = substring
            print('Long: ' + str(longest))
    else:
        substring = s[i]
        print('Subs: ' + str(substring))

print('Longest substring in alphabetical order is: ' + str(longest))
