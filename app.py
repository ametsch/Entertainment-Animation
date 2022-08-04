from datetime import datetime
import glob
import random
import hashlib

import pyautogui

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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


width, height = pyautogui.size()

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
    pygame.mixer.init()
    display = (width / 2 , height / 2)
    pygame.display.set_caption('Entertainment Animation', 'sclogo.png')
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)    
    pygame.mixer.music.set_volume(1.0)

    li = glob.glob('./music/*.ogg')
    for i in glob.glob('./music/*.mp3'):
        li.append(i)
    for i in glob.glob('./music/*.wav'):
        li.append(i)
    now = datetime.now()
    random.seed(hashlib.sha256(now.__str__().encode('UTF-8')).hexdigest())
    random.shuffle(li)

    print(li[0])
    pygame.mixer.music.load(li.pop(0))
    pygame.mixer.music.play()
    print(li[0])
    pygame.mixer.music.queue(li.pop(0))
    pygame.mixer.music.set_endevent(765045)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    sph = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                pygame.quit()
                exit(0)
            if event.type == pygame.mixer.music.get_endevent():
                print(li[0])
                pygame.mixer.music.queue(li.pop(0))
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
                if keys[K_f] or keys[K_F11]:
                    pygame.display.toggle_fullscreen()
                if keys[K_BACKSLASH]:
                    random.shuffle(li)
                if keys[K_h]:
                    sph = not sph

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        glColor4f(0x00, 0xff, 0xff, 1)
        if sph:
            gluSphere(sphere, 0.069, 64, 64)
        pygame.display.flip()
        pygame.time.wait(10)

main()
