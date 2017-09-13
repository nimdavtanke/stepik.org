##################################
#
# copyright Zaytsev Denis
#
##################################
#
num=int(input())

num6=num%10
num5=(int(num/10))%10
num4=(int(num/100))%10
num3=(int(num/1000))%10
num2=(int(num/10000))%10
num1=int(num/100000)

sum1=num1+num2+num3
sum2=num4+num5+num6

if sum1 == sum2 :
    print("Счастливый")
else:
    print("Обычный")