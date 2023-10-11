import random
loesung = random.randint(1,100)
raten = False
count = 0
while raten == False:
    if count == 10:
        print('Keine Versuche mehr. Die Lösung war', loesung)
        break
    count = count + 1

    userzahl = int(input('Rate die zahl zwischen 1-100: '))
    if loesung == userzahl:
        print(f'Richtig du hast {count} mal geraten')
        raten = True
    elif userzahl < loesung:
        print('Größer!')
    else:
        print('Kleiner!')


