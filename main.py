import pygame.freetype
import numpy as np
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Math Contest')

f = pygame.freetype.Font("consola.ttf", 36)

points_data = [
    [0, 0],
    [7, 0],
    [9, 2],
    [26, 2],
    [25, 1],
    [22, 0],
    [26, 1],
    [30, 3],
    [26, 5],
    [22, 6],
    [25, 5],
    [26, 4],
    [9, 4],
    [7, 6],
    [0, 6],
    [2, 4],
    [1, 4],
    [1, 2],
    [2, 2]
]

points = np.array(points_data)
points += 7
points *= 30

a1 = 22 + 11 / 8 - (np.sqrt(633) / 8)
a2 = (a1 + 17) / 2
a3 = (a1 - 17) / 2

circle_data = [
    [73 / 18, 3, np.sqrt((73 / 18) ** 2 + 9)],
    [11, 3, np.sqrt(5)],
    [15, 3, np.sqrt(5)],
    [a2, 3, np.sqrt(a3 * a3 + 1)],
    [22 + 11 / 8, 3, np.sqrt((11 / 8) ** 2 + 9)],
    [27.5, 3, 2.5],
]

while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, (0, 0, 0), points, 3)
    sum = 0
    for i in circle_data:
        pygame.draw.circle(screen, (100, 100, 100), (i[0] * 30 + 210, i[1] * 30 + 210), i[2] * 30, 2)
        sum += i[2] * i[2] + 4
    f.render_to(screen, (30, 30), f"Score : {sum}")
    pos = pygame.mouse.get_pos()
    f.render_to(screen, (950, 30), "Pos x : %.3f" % (pos[0] / 30 - 7))
    f.render_to(screen, (950, 70), "Pos y : %.3f" % (pos[1] / 30 - 7))
    for i in range(6):
        p1 = 200
        p2 = 470 + i * 30

        f.render_to(screen, (p1, p2), "Circle %d X: %6.3f Y: %.3f R: %.3f" % (i + 1, circle_data[i][0], circle_data[i][1], circle_data[i][2]))
    pygame.display.update()
