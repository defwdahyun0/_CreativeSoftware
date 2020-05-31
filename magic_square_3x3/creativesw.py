'''
a = int('-0b100',2)
b = hex(a)
c = bin(-4)

print(a)
print(b)
print(c)
'''
'''
print(bin(201921120))
print(bin(201921120))
print(201921120>>2)
print(201921120&2000)
print(201921120|-1)
'''
'''
print((2**3)+(4*(5**2)//2))
print((2 ** (1 + 1)) * (5 ** (~2)))
print((4 >> (1 + 2)) == 0)
print(not 2 + 2 << 2 == 4 and ~0 >> 3 == -1)
print(3 % 4 * 5 // 3 * -2 ** 3)
print(2**8)
'''

sum_all = 0
def funcA(a):
    global sum_all; 
    fsum = 0
    for i in range(64):
            fsum = fsum + ((a >> i) & 1)
    sum_all = sum_all + fsum
    return fsum

print (funcA (218))
#?A
print(funcA(-1))
#?B
fsum = 100
funcA(20)
print(fsum)
#?C
print(sum_all)
#?D