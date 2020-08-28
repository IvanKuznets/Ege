def to2(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
def transform(n):
    strNumber = str(n)
    summ=0
    for strDigit in strNumber:
        x = int(strDigit)
        summ+=x
    x = summ%2
    return strNumber+str(x)

inNumber = int(input())
binIn=to2(inNumber)
print(transform(transform(binIn)))