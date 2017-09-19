###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
S = 0
z = 0
a = int(input())
b = int(input())

if a % 3 == 0:
    for i in range(a,b+1,3):
        z += 1
        S = S + i
elif (a + 1) % 3 == 0:
    for i in range(a+1,b+1,3):
        z += 1
        S = S + i
else:
    for i in range(a+2,b+1,3):
        z += 1
        S = S + i

print(S/z)