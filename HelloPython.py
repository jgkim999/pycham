print("Hello, Python!")

# add value and print it.
watch = 100000
lighter = 300
print(watch + lighter)

# string + string.
a = 'pig'
b = 'dad'
print(a + ' ' + b)

# print family len.
family = ['mother', 'father', 'gentleman', 'sexy lady']
print('family len:' + str(len(family)))

# remove one element and print family len.
family.remove('gentleman')
print(family)
print('family len:' + str(len(family)))


print('직각삼각형 그리기\n')
d = float(input('변의 길이:'))

for i in range(int(d)+1):
    print('* ' * i)

area = float((d ** 2) / 2)
print('넓이:%s' % area)

input()
