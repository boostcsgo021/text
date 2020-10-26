import pygame

box_pos_x = 380
c = (36, 0, 80)

flag = 0

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((800, 600))

font = pygame.font.SysFont('Arial', 50, False, False)
font2 = pygame.font.SysFont('Arial', 25, False, False)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    screen.fill(c)
    screen.blit(font.render('Всем привет', True, (255, 255, 255)), (400 - font.size('Всем привет')[0] // 2, 300))
    screen.blit(font2.render('задание на урок', True, (255, 255, 0)), (400 - font2.size('задание на урок')[0] // 2, 370))
    pygame.draw.rect(screen, (255, 0, 0), (box_pos_x, 250, 45, 45))
    if flag == 0: 
        box_pos_x += 1
    elif flag == 1:
        box_pos_x -=1
    if box_pos_x > 755:
        flag = 1
    elif box_pos_x < 0:
        flag = 0
    pygame.display.update()
