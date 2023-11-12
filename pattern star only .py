n = int(input("\n\n\nENTER THE NUMBER OF ROWS: "))
for a in range(n,0,-1):
    for b in range(n -a):
        print(' ',end=' ')
    for b in range(2*a-1):
        print('*',end =' ')
    print()