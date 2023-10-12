# import random
# loesung = random.randint(1,100)
# raten = False
# count = 0
# while raten == False:
#     if count == 10:
#         print('Keine Versuche mehr. Die Lösung war', loesung)
#         break
#     count = count + 1
#
#     userzahl = int(input('Rate die zahl zwischen 1-100: '))
#     if loesung == userzahl:
#         print(f'Richtig du hast {count} mal geraten')
#         raten = True
#     elif userzahl < loesung:
#         print('Größer!')
#     else:
#         print('Kleiner!')

# import random
#
# ran_zahlen = []
# for x in range(100):
#     ran_zahlen.append(random.randint(1, 100))
# print(ran_zahlen)
# print('------------------------------------------')
#
# n = len(ran_zahlen)
# for x in range(n - 1):
#     for y in range(n - 1 - x):
#         print(f'überprüfen {ran_zahlen[y]} größer als {ran_zahlen[y + 1]}')
#         input()
#         if ran_zahlen[y] > ran_zahlen[y + 1]:
#             ran_zahlen[y], ran_zahlen[y + 1] = ran_zahlen[y + 1], ran_zahlen[y]
#
import random

zahl1 = random.randint(1, 10)
zahl2 = random.randint(1, 10)
antwort = ''
zahlenstring = []
for i in range(10):
    zahlenstring.append(str(i))

while antwort != (zahl1 + zahl2):
    isint = True
    antwort = input(f'Was ist {zahl1} + {zahl2}? ')

    while isint:
        for stelle in antwort:
            if stelle not in zahlenstring:
                antwort = input('Gib eine Zahl ein!!!')
                isint = True
                break
            else:
                isint = False
    antwort = int(antwort)

    if zahl1 + zahl2 != antwort:
        print('Falsch')
print('richtig')
