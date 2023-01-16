
n = int(input("Number you want to convert"))
m = n
con_num = []
b = 0

def tentwo():
    global m, con_num, b
    while m >= 1:
        b = m % 2
        con_num.append(b)
        m = m//2
    con_num.reverse()
    b = ''.join(str(e) for e in con_num)
    print(f"Bianry form of your number is, {b}")


def twoten():
    global m, con_num, b
    m = str(n)
    a = 0
    for e in m :    
        if e != '0' and e != '1':
            print("invalid input")
        else:
            a+=1
            
    if a == len(m):
        for i in range(0,len(m)):
            b += int(m[i]) * (2**(len(m) - i - 1))
        print(f"The Decimal form of your digit is {b}")
        

                

twoten()
