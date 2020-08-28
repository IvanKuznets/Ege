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
 
p=0
outNumber = -1
while (outNumber<78):
    binIn=to2(p)
    outNumber = int(str(transform(transform(binIn))),2)
    p+=1
print(p-1)
    
