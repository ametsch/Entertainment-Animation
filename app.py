from datetime import datetime
import glob
import random

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


# sphereCenter = (
#     (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
#     (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1),
#     (0, 0, 0)
# )

verticies = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1),
    (0, 0, 0), (1, 0, 1), (-1, 0, -1), (-1, 0, 1),
    (1, 0, -1), (1, 1, 0), (-1, -1, 0), (1, -1, 0),
    (-1, 1, 0), (0, 1, 1), (0, -1, -1), (0, 1, -1),
    (0, -1, 1)
)

edges = (
    (0, 1), (0, 3), (0, 4), (2, 1),
    (2, 3), (2, 7), (6, 3), (6, 4),
    (6, 7), (5, 1), (5, 4), (5, 7),
    (0, 8), (1, 8), (2, 8), (3, 8),
    (4, 8), (5, 8), (6, 8), (7, 8),
    (9, 8), (10, 8), (11, 8), (12, 8),
    (13, 8), (14, 8), (15, 8), (16, 8),
    (17, 8), (18, 8), (19, 8), (20, 8)
)

# verticies = (
#     (.05, -.05, -.05), (.05, .05, -.05), (-.05, .05, -.05), (-.05, -.05, -.05),
#     (.05, -.05, .05), (.05, .05, .05), (-.05, -.05, .05), (-.05, .05, .05),
#     (0, 0, 0), (.05, 0, .05), (-.05, 0, -.05), (-.05, 0, .05),
#     (.05, 0, -.05), (.05, .05, 0), (-.05, -.05, 0), (.05, -.05, 0),
#     (-.05, .05, 0), (0, .05, .05), (0, -.05, -.05), (0, .05, -.05),
#     (0, -.05, .05)
# )

sphere = gluNewQuadric()

def Cube():
    glColor4f(0xff, 0x00, 0x00, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_caption('PyOpenGL X pygame test')
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | pygame.FULLSCREEN)
    pygame.mixer.init()
    
    pygame.mixer.music.set_volume(.9)

    li = glob.glob('./music/*.ogg')
    for i in glob.glob('./music/*.mp3'):
        li.append(i)
    for i in glob.glob('./music/*.wav'):
        li.append(i)
    random.seed(datetime.now().microsecond)
    random.shuffle(li)

    #print(li[0])
    pygame.mixer.music.load(li.pop(0))
    pygame.mixer.music.play()


    for song in li:
        #print(song)
        pygame.mixer.music.queue(li.pop(li.index(song)))

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_q] or keys[K_x] or keys[K_ESCAPE]:
                    pygame.mixer.quit()
                    pygame.quit()
                    exit(0)
                if keys[K_s]:
                    pygame.mixer.music.pause()
                if keys[K_p]:
                    pygame.mixer.music.unpause()
                if keys[K_r]:
                    pygame.mixer.music.rewind()


        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        glColor4f(0x00, 0xff, 0xff, 1)
        gluSphere(sphere, 0.069, 64, 64)
        pygame.display.flip()
        pygame.time.wait(10)


main()
