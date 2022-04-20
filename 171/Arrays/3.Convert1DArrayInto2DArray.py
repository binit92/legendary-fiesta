
# https://leetcode.com/problems/convert-1d-array-into-2d-array/


def convert(input, m, n ):
    i = 0
    ret = []
    while i < len(input):
        
        new = input[i:i+n]
        ret.append(new)
        i += n
    return ret

if __name__ == "__main__":
    input1 = [1,2,3,4]
    m1 = 2
    n1 = 2
    output1 =  [[1,2],[3,4]]
    print(convert(input1,m1,n1))

    input2 = [1,2,3]
    m2= 1
    n2 =3
    output2 = [[1,2,3]]
    print(convert(input2,m2,n2))
