flow = True
d = 0
onum = 0
onum_list = []

def main():
    global flow, d, onum_list, onum
    d = 0
    onum = 0
    onum_list = []
    m = int(input("Enter base you are converting from "))
    n = int(input("Enter Base you are converting to "))

    # check if user is stoopid
    inum = int(input("Enter the number you wish to convert, please make sure the number is of proper base, and is non negative and a whole number; "))
    inums = str(inum)

    # check is the base of the inputed number is proper, and double check if user is stoopid
    def check():
        for i in inums:
            if int(i) >= m:
                print("Improper Base")
                main()
        if type(inum) != int:
            print(TypeError)
            main()
        if inum < 0:
            print(ValueError)
            main()
    
    def ntm():
        global d, onum

        # convert number from initial base to decimal
        for i in range(0, len(inums)):
            d += (int(inums[-(i+1)])) * (m**(i))

        # convert number from decimal to final base
        v = 0
        while d >= 1:
            v = d % n
            onum_list.append(str(v))
            d = d // n
        onum_list.reverse()
        onum = int(''.join(onum_list))

    check()
    ntm()
    print(onum)
    

def deci():
    global flow
    decision = input("Do you wish to Convert Next(c), or Quit(q) ")
    if (decision.lower) == "q":
        flow = False
    elif (decision.lower) != "c":
        print("Baka")
        flow = False

while flow == True:
    main()
    deci()


    
            
