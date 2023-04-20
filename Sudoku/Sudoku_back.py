import random
import copy
sudoku_field=[]
number = [1,2,3,4,5,6,7,8,9]
line=[]
field_line=[]
index=[[0,1,2],[3,4,5],[6,7,8]]
# print_sudoku_field = ('')
answer=[]
#answer_field=[]
fix_list=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
#------------------------------------------------Генератор поля------------------------------------------------------

#------------------------------------------------Генератор строки----------------------------------------------------
for numbers in range(9):
    string = number[random.randint(0, len(number) - 1)]
    line.append(string)
    number.remove(string)
sudoku_field.append(line)
#-----------------------------------------------first block line----------------------------------------------------
for i in range(3,9):
    field_line.append(line[i])
for i in range(0,3):
    field_line.append(line[i])
sudoku_field.append(field_line)
field_line=[]
for i in range(6,9):
    field_line.append(line[i])
for i in range(0,6):
    field_line.append(line[i])
sudoku_field.append(field_line)
field_line=[]

#-----------------------------------------------secnd block line-------------------------------------------------------
for y in range(3):
    for i in range(1,9):
        field_line.append(sudoku_field[y][i])
    field_line.append(sudoku_field[y][0])
    sudoku_field.append(field_line)
    field_line=[]
#------------------------------------------------thrid block line------------------------------------------------------
for y in range(3,6):
    for i in range(1,9):
        field_line.append(sudoku_field[y][i])
    field_line.append(sudoku_field[y][0])
    sudoku_field.append(field_line)
    field_line=[]
#------------------------------------------Генератор матричных сдвигов-------------------------------------------------

#------------------------------------------Изменения по линиям---------------------------------------------------------
for i in range(100000):
    first_change_line = random.randint(0,8)
    second_change_line = index[first_change_line//3].copy()
    second_change_line = second_change_line[random.randint(0,2)]
    sudoku_field[second_change_line], sudoku_field[first_change_line] = sudoku_field[first_change_line], sudoku_field[second_change_line]

#-------------------------------------------Изменения по колонкам------------------------------------------------------
    first_change_column = random.randint(0, 8)
    second_change_column = index[first_change_column // 3].copy()
    second_change_column = second_change_column[random.randint(0, 2)]
    for i in range(9):
        sudoku_field[i][second_change_column], sudoku_field[i][first_change_column] = sudoku_field[i][
                                                                                          first_change_column], \
                                                                                      sudoku_field[i][
                                                                                second_change_column]
#------------------------------------------------------Вывод поля---------------------------------------------------
answer=copy.deepcopy(sudoku_field)
for y in range(9):
    for x in range(8):
        i=random.randint(0,8)
        for x in range(9):
            if sudoku_field[x][i]!=(''):
                sudoku_field[y][i] = ('')
                fix_list[y][i] = 1
# print(answer)
# print(sudoku_field)
#
# for y in range(9):
#     for x in range(9):
#         if answer_field[y][x]!=sudoku_field[y][x]:
#             answer.append(answer_field[y][x])
# for y in range(9):
#     if y%3==0 and y!=0:
#         print_sudoku_field+='\n'
#     for x in range(9):
#         if x%3==0 and x!=0:
#             print_sudoku_field+='  '
#         print_sudoku_field+=str(sudoku_field[y][x])+(' ')
#     print_sudoku_field+='\n'
# print(print_sudoku_field)
# print('В случаее возникновения ошибки, пожалуйста сохраните копию теста и пните разраба под зад!\n')
# user_answer=answer#[int (i) for i in input('Введите недостающие числа с 1 по 9 строку слева на право отделяя пробелом:\n').split()]
# if user_answer==answer:
#     sudoku_field=answer_field
#     print_sudoku_field=('')
#     for y in range(9):
#         if y % 3 == 0 and y != 0:
#             print_sudoku_field += '\n'
#         for x in range(9):
#             if x % 3 == 0 and x != 0:
#                 print_sudoku_field += '  '
#             print_sudoku_field += str(sudoku_field[y][x]) + (' ')
#         print_sudoku_field += '\n'
#     print(print_sudoku_field)
#     print('\n\n\nПоздравляю! :)')
# else:
#     print('\n\n\nНе угадал :(')


