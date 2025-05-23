import math

IN = str(input('Input Number  : '))
IB = str(input('Input Base    : '))
decimal = 0
pos = len(IN)

if IB == '2':
    for i in IN:
        pos -= 1
        if int(i) != 0:
            decimal += 2 ** pos
elif IB == '16':
    for i in IN:
        pos -= 1
        if i.isdigit():
            decimal += int(i) * (16 ** pos)
        else:
            decimal += (ord(i) - 55) * (16 ** pos)
    
print("Output Decimal : ", decimal)


