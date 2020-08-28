def F(a):
    s = int(a)
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    return(n)

p = 0

while(F(p)!=64):
    p+=1
print(p)