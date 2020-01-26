import pygame
import numpy as n

def generate_square(dimensions):
    vertices = []
    for i in range(0,2**dimensions):
        vertices.append(n.array(str(bin(i))[2:].zfill(dimensions).replace('',',').replace('0','-1')[1:-1].split(','),dtype='int'))
    return vertices

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #draw
            pygame.display.flip()
            pygame.time.wait(10)
pygame.init()
display = (800,800)
screen = pygame.display.set_mode(display)

cube = generate_square(3)
main()
