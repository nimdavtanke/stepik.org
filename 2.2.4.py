##################################
#
# copyright Zaytsev Denis
#
##################################
#

count = 1

while count > 0:
    num = int(input())
    count += 1
    if num <= 10:
        continue
    elif num > 100:
        break
    else:
        print(num)