###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a <= b and c <= d:

    for i in range(c,d+1):
        print('\t',i, end='\t')

    print()
    for i in range(a,b+1):
        print(i, end='')
        for j in range(c,d+1):
            print('\t',i*j, end='\t')
        print()

else:
    print("Someting wrong")