import pygame
import numpy as n

projection = ( # 3d -> 2d projection matrix
    (1,0,0),
    (0,1,0)
)

def generate_square(dimensions):
    vertices = []
    for i in range(0,2**dimensions):
        vertices.append(n.array(str(bin(i))[2:].zfill(dimensions).replace('',',').replace('0','-1')[1:-1].split(','),dtype='int'))
    return vertices

def drawVertex(pos,screen):
    pos = (int(50*pos[0])+400,int(50*pos[1])+400)
    pygame.draw.circle(screen,(255,255,255),pos,3)

def draw():
    screen.fill((0,0,0))
    projectedPoints = []
    for vertex in cube:
        projected = n.dot(projection,vertex)
        projectedPoints.append(projected)
        drawVertex(projected,screen)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            draw()
            pygame.display.flip()
            pygame.time.wait(10)
pygame.init()
display = (800,800)
screen = pygame.display.set_mode(display)

cube = generate_square(3)
main()
