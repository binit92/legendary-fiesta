
# built-in class
def addBinary1(a, b) :
    return '{0:b}'.format(int(a,2) + int(b,2))

# Bit by bit computation
def addBinary2(a,b):
    n = max(len(a), len(b))
    a,b = a.zfill(n), b.zfill(n)
    
    carry = 0
    answer = []
    for i in range (n-1, -1, -1):
        if a[i] == '1':
            carry += 1

        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            answer.append('1')
        else:
            answer.append('0')

        carry //=2 
    if carry == 1:
        answer.append('1')
    answer.reverse()

    return ''.join(answer)

# 