import time
import random

def checker(znack, tag):
    checksum = []
    for i in range(1, 10):
        if pole_znakov[i] == znack:
            checksum.append(i)
    for a in range(0, len(checksumlist)):
        if checksumlist[a][0] in checksum and checksumlist[a][1] in checksum and checksumlist[a][2] in checksum:
            if tag == 'chel':
                print('\n\nВы победили!')
            else:
                print('\n\nВы были повержены машиной...')
            return False
    return True
            
def hod(x_ili_o, tag):
    if tag == 'chel':
        time.sleep(0.2)
        print('\n{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}'.format(pole[7], pole[8], pole[9], pole[4], pole[5], pole[6], pole[1], pole[2], pole[3]))
        time.sleep(0.2)
        for i in range(0, 100):
            vybor_polya = int(input('Куда ставите вы?  '))
            if vybor_polya in zanyato or vybor_polya > 9:
                print('Эта ячейка кем-то занята!')
            else:
                break
        zanyato.append(vybor_polya)
    else:
        for i in range(0, 100):
            vybor_polya = random.randint(1, 9)
            if vybor_polya in zanyato:
                vybor_polya = random.randint(1, 9)
            else:
                break
        zanyato.append(vybor_polya)
        print('Компьютер ходит...')
        time.sleep(1)
    pole_znakov[vybor_polya] = x_ili_o
    pole[vybor_polya] = ' '
    print('\n\n{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}'.format(pole_znakov[7], pole_znakov[8], pole_znakov[9], pole_znakov[4], pole_znakov[5], pole_znakov[6], pole_znakov[1], pole_znakov[2], pole_znakov[3]))
    
def kto_pervyi(x):
    print("\n\nМонетка подброшена...")
    time.sleep(2)
    coin = random.randint(0, 1)
    if x == coin:
        return 1
    else:
        return 0


pole = {7 : '7', 8 : '8', 9 : '9', 4 : '4', 5 : '5', 6 : '6', 1 : '1', 2 : '2', 3 : '3 '}

pole_znakov = {7 : '_', 8 : '_', 9 : '_', 4 : '_', 5 : '_', 6 : '_', 1 : ' ', 2 : ' ', 3 : ' '}

znak = ['x', 'o']

zanyato = []

checksumlist = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [7, 5, 3], [9, 8, 7], [9, 6, 3], [8, 5, 2], [4, 5, 6]]

game_on = True
print('\n\nДОБРО ПОЖАЛОВАТЬ В ИГРУ!\n\n')
time.sleep(0.5)

ochered = kto_pervyi(int(input('Орел или решка? "0"/"1" ')))

if ochered == 1:
    print('\n\nВы ходите первым!')
    time.sleep(1)
    znak_chel = znak[0]
    znak_comp = znak[1]
    hod(znak_chel, 'chel')
    ochered = 0
else:
    print('\n\nКомпьютер ходит первым!')
    time.sleep(1.5)
    znak_comp = znak[0]
    znak_chel = znak[1]
    hod(znak_comp, 'comp')
    ochered = 1
    
while game_on:
    if len(zanyato) > 8:
        print('\n\nНИЧЬЯ')
        break
    if ochered == 1:
        hod(znak_chel, 'chel')
        game_on = checker(znak_chel, 'chel')
        time.sleep(1)
        ochered = 0
    else:
        time.sleep(1)
        hod(znak_comp, 'comp')
        game_on = checker(znak_comp, 'comp')
        ochered = 1
    
print('\n\n\nКонец игры')