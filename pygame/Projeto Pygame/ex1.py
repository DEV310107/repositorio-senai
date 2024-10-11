import pygame

#Para importar funções e constantes do código
from pygame.locals import *

#Para fechar a janela
from sys import exit

#Para iniciar todas as funções e variáveis da biblioteca pygame 
pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('sdjibhisdbcho')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()