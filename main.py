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

def calc_lines(dimensions):
    binverts = []
    result = []
    for i in range(0,2**dimensions):
        binverts.append(str(bin(i))[2:].zfill(dimensions))
    
    for i,vert in enumerate(binverts):
        for j in range(0,dimensions):
            targ = vert
            if vert[j] == '0':
                s = list(targ)
                s[j] = '1'
                targ = ''.join(s)
            else:
                s = list(targ)
                s[j] = '0'
                targ = ''.join(s)
            result.append([i,binverts.index(targ)])

    return result

def drawVertex(pos,screen):
    pos = (int(50*pos[0])+400,int(50*pos[1])+400)
    pygame.draw.circle(screen,(255,255,255),pos,3)

def drawLine(posA,posB,screen,color=(255,255,255)):
    posA = (int(50*posA[0])+400,int(50*posA[1])+400)
    posB = (int(50*posB[0])+400,int(50*posB[1])+400)
    pygame.draw.line(screen,color,posA,posB)

def draw():
    global theta
    screen.fill((0,0,0))
    projectedPoints = []
    for vertex in cube:
        rotated = rotate(theta,vertex,d)
        if d == 3:
            projected = n.dot(projection,rotated)
        else:
            projected = rotated
        projectedPoints.append(projected)
        drawVertex(projected,screen)
    for line in lines:
        drawLine(projectedPoints[line[0]],projectedPoints[line[1]],screen)

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

def rotate(theta,vertex,dimensions):
    global rotationX3,rotationY3,rotationZ3,rotation2
    if dimensions == 3:
        redefRotMats3(theta)
        r = n.dot(rotationX3,vertex)
        r = n.dot(rotationY3,r)
        r = n.dot(rotationZ3,r)
        return r
    if dimensions == 2:
        redefRotMats2(theta)
        return n.dot(rotation2,vertex)

def redefRotMats3(theta):
    global rotationX3,rotationY3,rotationZ3
    rotationX3 = (
        (1, 0, 0),
        (0, n.cos(theta), -n.sin(theta)),
        (0, n.sin(theta), n.cos(theta)),
    )

    rotationY3 = (
        (n.cos(theta), 0, -n.sin(theta)),
        (0, 1, 0),
        (n.sin(theta), 0, n.cos(theta))
    )

    rotationZ3 = ( 
        (n.cos(theta), -n.sin(theta), 0),
        (n.sin(theta), n.cos(theta), 0),
        (0, 0, 1)
    )

def redefRotMats2(theta):
    global rotation2
    rotation2 = ( 
        (n.cos(theta), -n.sin(theta)),
        (n.sin(theta), n.cos(theta))
    )

d = 3
cube = generate_square(d)
lines = calc_lines(d)
main()
