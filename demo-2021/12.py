s='8'*70
print(s)
while (s.find('2222')!=-1) or (s.find('8888')!=-1):
    if (s.find('2222')!=-1):
        s = s.replace('2222','88',2) #str.replace(old, new[, max])
    else:
        s = s.replace('8888','22',)
    print(s)
print(s)
