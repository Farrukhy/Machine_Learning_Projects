a = 18
b = 3
print(a + b)
print(a * b)
print(a / b)
print(a - b)
print(a ** b)
a+=2
print(a)
b*=3
print(b)
#
c = -77.1
print(int(-c))
#
import math

x = 4
print(float(math.exp2(x))) #print(math.exp2(x))
print(int(math.pow(2,x)))  #print(math.pow(2,x))
print(2.0**x)

balance = 0.7 + 0.60000000000001

if balance >= 1.3:
    balance -= 1.3
    print('Purchase successful!')
else:
    print("Insufficient Funds")



