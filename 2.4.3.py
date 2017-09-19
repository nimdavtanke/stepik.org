###########################
#                         #
# copyright Zaytsev Denis #
#                         #
###########################
#
genome = input()
kol = 0
dlina = 0

for x in genome:
    dlina += 1

kol = genome.upper().count('c'.upper()) + genome.upper().count('g'.upper())

print(kol / dlina * 100)