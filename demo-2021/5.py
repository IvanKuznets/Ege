#Перевод в двоичную СС. Можно проще при помощи bin()
def to2(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
    
#Выполнение пункта 1 и 2 (преобразование числа)
def transform(n):
    strNumber = str(n)
    summ=0
    for strDigit in strNumber:
        x = int(strDigit)
        summ+=x
    x = summ%2
    return strNumber+str(x)
 
p=0
outNumber = int(str(transform(transform(to2(p)))),2)
while (outNumber<78):
    p+=1
    binIn=to2(p)
    outNumber = int(str(transform(transform(binIn))),2)
print(p)
    
