n = int(input("Enter base you are converting from "))
m = int(input("Enter base you are converting to "))
inum = int(input("Enter the number you wish to convert, please make sure it is of proper base; "))
d = 0
ns = str(n)
ms = str(m)
ds = str(d)
inums = str(inum)
ounum_list = []
fnum = 0

# convert number from initial base to decimal
def ntd():
    global d, ns, ds, inums
    for i in range(0, len(inums)):
        d += (int(inums[-(i+1)])) * (n**(i))


def dtm():
    global d, ms, ds, inums ,ounum_list, fnum
    v = 0
    while d >= 1:
        v = d % m
        ounum_list.append(str(v))
        d = d // m
    ounum_list.reverse()
    fnum = int(''.join(ounum_list))

ntd()
dtm()
print(fnum)


        