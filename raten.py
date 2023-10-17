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
import numpy as np
liste = []
for x in range(1, 65537):

    liste.append(x)
np_array = np.array(liste)
print(np_array.sum())
print(sum(liste))


