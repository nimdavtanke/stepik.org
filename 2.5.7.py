###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
a = [int(i) for i in input().split()]

count = 0
sum = 0
kol = len(a)

while count < kol:
    sum = sum + a[count]
    count = count + 1

print(sum)
