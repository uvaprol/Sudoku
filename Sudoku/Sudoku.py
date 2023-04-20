import pygame
import Sudoku_back
import time
# import random
sudoku=Sudoku_back.sudoku_field
fix_list=Sudoku_back.fix_list
answer=Sudoku_back.answer
pygame.init()
wh = 457
display = pygame.display.set_mode((wh, wh))
white = (255,255,255)
grey=(83, 87, 83)
black = (0,0,0)
red=(189, 6, 6)
pygame.display.set_caption('Sudoku')
font = pygame.font.SysFont("None", 90)
message = font.render("Congratulation", True, red)

def draw_field_answer(click_x,click_y,ans):
    display.fill(white)
    for y in range(9):
        for x in range(9):
            if fix_list[y][x] == 1:
                display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, grey), [15+50*x+x, 10+50*y+y])
            else:
                display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, black),[15 + 50 * x + x, 10 + 50 * y + y])
    pygame.draw.rect(display, white, [50 * click_x + click_x, 50 * click_y + click_y, 50, 50])
    display.blit(pygame.font.SysFont("None", 50).render(str(ans), True, red),[15 + 50 * click_x + click_x, 10 + 50 * click_y + click_y])

    for i in range(1, 9):
        pygame.draw.rect(display, black, [50 * i + i - 1, 0, 1, wh])
        pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 1])
    for i in range(3, 7, 3):
        pygame.draw.rect(display, black, [50 * i + i - 1, 0, 5, wh])
        pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 5])

    pygame.display.flip()
def draw_field(click_x,click_y):
    display.fill(white)
    if click_x != None:
        pygame.draw.rect(display, grey, [50 * click_x + click_x , 50 * click_y + click_y , 50, 50])

    for i in range(1, 9):
        pygame.draw.rect(display, black, [50 * i + i - 1, 0, 1, wh])
        pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 1])
    for i in range(3, 7, 3):
        pygame.draw.rect(display, black, [50 * i + i - 1, 0, 5, wh])
        pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 5])
    for y in range(9):
        for x in range(9):
            if fix_list[y][x] == 1:
                display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, grey), [15+50*x+x, 10+50*y+y])
            else:
                display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, black),[15 + 50 * x + x, 10 + 50 * y + y])
    pygame.display.flip()
#----------------------------------------------start-------------------------------------------------

#------------------------------------------------------------------------------------------------------------





while sudoku != answer:

    draw_field(None,None)
    events = pygame.event.get()
    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
#------------------------------------------------warning--------------------------------------------------

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = pygame.mouse.get_pos()
                click_x = click[0] // 51
                click_y = click[1] // 51
                if fix_list[click_y][click_x] == 0:
                    stop = 1
                else:
                    draw_field(click_x, click_y)
                    stop = 0
            while stop==0:
                events = pygame.event.get()
                for event in events:
                    #print(event)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            click = pygame.mouse.get_pos()
                            click_x = click[0] // 51
                            click_y = click[1] // 51
                            if fix_list[click_y][click_x] == 0:
                                stop = 1
                            else:
                                draw_field(click_x, click_y)
                                stop = 0
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_h:
                            draw_field(click_x, click_y)
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_h:
                            draw_field_answer(click_x, click_y, answer[click_y][click_x])

                        elif event.key == pygame.K_1:
                            sudoku[click_y][click_x] = 1
                            stop=1
                        elif event.key == pygame.K_2:
                            sudoku[click_y][click_x] = 2
                            stop=1
                        elif event.key == pygame.K_3:
                            sudoku[click_y][click_x] = 3
                            stop = 1
                        elif event.key == pygame.K_4:
                            sudoku[click_y][click_x] = 4
                            stop = 1
                        elif event.key == pygame.K_5:
                            sudoku[click_y][click_x] = 5
                            stop = 1
                        elif event.key == pygame.K_6:
                            sudoku[click_y][click_x] = 6
                            stop = 1
                        elif event.key == pygame.K_7:
                            sudoku[click_y][click_x] = 7
                            stop = 1
                        elif event.key == pygame.K_8:
                            sudoku[click_y][click_x] = 8
                            stop = 1
                        elif event.key == pygame.K_9:
                            sudoku[click_y][click_x] = 9
                            stop = 1
                        elif event.key == pygame.K_KP1:
                            sudoku[click_y][click_x] = 1
                            stop = 1
                        elif event.key == pygame.K_KP2:
                            sudoku[click_y][click_x] = 2
                            stop=1
                        elif event.key == pygame.K_KP3:
                            sudoku[click_y][click_x] = 3
                            stop = 1
                        elif event.key == pygame.K_KP4:
                            sudoku[click_y][click_x] = 4
                            stop = 1
                        elif event.key == pygame.K_KP5:
                            sudoku[click_y][click_x] = 5
                            stop = 1
                        elif event.key == pygame.K_KP6:
                            sudoku[click_y][click_x] = 6
                            stop = 1
                        elif event.key == pygame.K_KP7:
                            sudoku[click_y][click_x] = 7
                            stop = 1
                        elif event.key == pygame.K_KP8:
                            sudoku[click_y][click_x] = 8
                            stop = 1
                        elif event.key == pygame.K_KP9:
                            sudoku[click_y][click_x] = 9
                            stop = 1
# ------------------------------------------------warning--------------------------------------------------



#---------------------------------------------final-----------------------------------------------------------

display.fill(white)
for i in range(1, 9):
    pygame.draw.rect(display, black, [50 * i + i - 1, 0, 1, wh])
    pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 1])
for i in range(3, 7, 3):
    pygame.draw.rect(display, black, [50 * i + i - 1, 0, 5, wh])
    pygame.draw.rect(display, black, [0, 50 * i + i - 1, wh, 5])
for y in range(9):
    for x in range(9):
        if fix_list[y][x] == 1:
            display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, grey), [15+50*x+x, 10+50*y+y])
        else:
            display.blit(pygame.font.SysFont("None", 50).render(str(sudoku[y][x]), True, black),[15 + 50 * x + x, 10 + 50 * y + y])

display.blit(message, [0, (wh // 2 )-35])
pygame.display.flip()
time.sleep(3)