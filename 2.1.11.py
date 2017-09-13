##################################
#
# copyright Zaytsev Denis
#
##################################
#

s = 0
i = 1
while i > 0:
     num = int(input())
     s += num
     if num == 0:
         i = 0
     else:
         i += 1
print(s)
