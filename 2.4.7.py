###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
stroka = input()
i = 0
j = 1
kol = 1

while i <= len(stroka) - 1:
    if j == len(stroka) or (stroka[i] != stroka[j]):
        kol = 1
        print(stroka[i], end='')
        print(kol, end='')
        i += 1
        j += 1
    else:
        while (j < len(stroka)) and (stroka[i] == stroka[j]):
            kol += 1
            j += 1
        print(stroka[i], end='')
        print(kol, end='')
        kol = 1
        i = j
        j += 1###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
stroka = input()
i = 0
j = 1
kol = 1

while i <= len(stroka) - 1:
    if j == len(stroka) or (stroka[i] != stroka[j]):
        kol = 1
        print(stroka[i], end='')
        print(kol, end='')
        i += 1
        j += 1
    else:
        while (j < len(stroka)) and (stroka[i] == stroka[j]):
            kol += 1
            j += 1
        print(stroka[i], end='')
        print(kol, end='')
        kol = 1
        i = j
        j += 1