import re

def de_identify(input):
    numbers = re.sub(r'[^0-9]', '', input)
    li = list(numbers)
    for i in range(6,len(li)):
        li[i]='*'

    return ''.join(li)

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))