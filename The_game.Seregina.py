box = [['']*3 for i in range(3)]

def visual():
    print(f" 0 1 2")
    print(f'0 {box[0][0]} {box[0][1]} {box[0][2]}')
    print(f'1 {box[1][0]} {box[1][1]} {box[1][2]}')
    print(f'2 {box[2][0]} {box[2][1]} {box[2][2]}')

def coordinates(gamer): #выбор координат, проверка возможности ходить в клетку
    x = int(input(f'{gamer}, введите первую координату: ', ))
    y = int(input(f'{gamer}, введите вторую координату: ', ))
    if box[x][y] == '':
        box[x][y] = Xor0
    else:
        print('В указанную клетку ходить нельзя')
        coordinates(gamer)
    print('Ваш ход: ', (x,y))
    return box[x][y]
def who_winner():
    win_comb = ([((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2)),
                  ((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2)),
                  ((0,0),(1,1),(2,2)), ((2,0),(1,1),(0,2))])
    for num in win_comb:
        check_list = []
        for c in num:
            check_list.append(box[c[0]][c[1]])
        if check_list == ['X','X','X']:
            print('Выиграл Х!')
            return True
        if check_list == ['0','0','0']:
            print('Выиграл 0!')
            return True
    return False

print("Добро пожаловать в игру 'Крестики-Нолики'!")
print()
gamer_one = input('Введите имя первого игрока: ', )
gamer_two = input('Введите имя второго игрока: ', )
for i in range(9):
    visual()
    if who_winner():
        break
    if i in (0,2,4,6,8):
        Xor0 = 'X'
        coordinates(gamer_one)
    else:
        Xor0 = '0'
        coordinates(gamer_two)





