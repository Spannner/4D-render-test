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
    global theta
    screen.fill((0,0,0))
    redefRotMats(theta)
    projectedPoints = []
    for vertex in cube:
        rotated = n.dot(rotationZ,vertex)
        rotated = n.dot(rotationX,rotated)
        rotated = n.dot(rotationY,rotated)
        projected = n.dot(projection,rotated)
        projectedPoints.append(projected)
        drawVertex(projected,screen)


def main():
    global theta
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw()
        theta += 0.01
        pygame.display.flip()
        pygame.time.wait(10)
pygame.init()
display = (800,800)
screen = pygame.display.set_mode(display)

theta = 0

def redefRotMats(theta):
    global rotationX,rotationY,rotationZ
    rotationX = (
        (1, 0, 0),
        (0, n.cos(theta), -n.sin(theta)),
        (0, n.sin(theta), n.cos(theta)),
    )

    rotationY = (
        (n.cos(theta), 0, -n.sin(theta)),
        (0, 1, 0),
        (n.sin(theta), 0, n.cos(theta))
    )

    rotationZ = ( 
        (n.cos(theta), -n.sin(theta), 0),
        (n.sin(theta), n.cos(theta), 0),
        (0, 0, 1)
    )

cube = generate_square(3)
main()
