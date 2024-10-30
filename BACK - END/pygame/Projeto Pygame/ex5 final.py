import pygame #importa a bliblioteca "pygame"

pygame.init() # inicia os modulos do pygame
pygame.mixer.init() #inicializa o modulo de reprodução de audio

pygame.mixer.music.load("sonora.mp3") #importa o elemento "mp3"
pygame.mixer.music.set_volume(0.2) #define volume do audio
pygame.mixer.music.play(-1) #toca em um loop infinito

screen = pygame.display.set_mode((1280, 720)) #define uma resolução 
pygame.display.set_caption("Ping Fut") #nomeia a janela criada

#define as posiçoes iniciais dos elementos dentro do jogo
x1, y1 = 0, 630 #boneco01 
x2, y2 = 1190, 630 #boneco02 
x3, y3 = 615, 335 #bola

vel_x, vel_y, = 8, 8 #define velocidade do elemento bola 

#define cores
preto = (0, 0, 0)
branco = (255, 255, 255)

campo = pygame.image.load("campo.jpg") #importa as imagem do campo
campo = pygame.transform.scale(campo, (1280, 720))  #ajusta a escala do compo com o tamanho da resolução da janela 

bola = pygame.image.load("bola.png") #importa o elemento bola 

boneco01 = pygame.image.load("jogador01.png") #importa o elemento jogador 01
boneco02 = pygame.image.load("jogador02.png") #importa o elemento jogador 02 

# ajusta o tamanho do jogador 01
largura_boneco01 = 80 #cria uma variavel da largura e define a quantidade de pixels
altura_boneco01 = 150 #cria uma variavel da altura e define a quantidade de pixels
boneco01 = pygame.transform.scale(boneco01, (largura_boneco01, altura_boneco01)) #aplica para a variavel boneco 01

largura_boneco02 = 80 #cria uma variavel da largura e define a quantidade de pixels
altura_boneco02 = 150 #cria uma variavel da altura e define a quantidade de pixels
boneco02 = pygame.transform.scale(boneco02, (largura_boneco02, altura_boneco01)) #aplica para a variavel boneco 02

largura_bola = 50 #cria uma variavel da largura e define a quantidade de pixels
altura_bola = 50 #cria uma variavel da altura e define a quantidade de pixels
bola = pygame.transform.scale(bola, (largura_bola, altura_bola)) #aplica para a variavel bola


clock = pygame.time.Clock() #usado para controlar taxa de quadros

bola_inicial_x, bola_inicial_y = x3, y3    

#inicializa pontuação dos jogadores
pontos_jogador01 = 0
pontos_jogador02 = 0 

font = pygame.font.Font(None,36) #cria uma fonte

running = True #Este é o loop principal do jogo, que continua rodando até que running se torne False.
while running: #Responsável por manter o jogo em execução
    for event in pygame.event.get():##
        if event.type == pygame.QUIT:##Se o evento capturado for do tipo QUIT (quando o jogador clica no "X" para fechar a janela), o loop é interrompido,
            running = False  ##

##################################################################################################

    keys = pygame.key.get_pressed() #captura a teclas do teclado
    if keys[pygame.K_w]: #define a tecla "W" para mover boneco01 para cima
        y1 -= 5  #diminui a cordenada do boneco01 (mover para cima) 
    if keys[pygame.K_s]: #define a tecla "S" para mover o boneco02 para baixo
        y1 += 5 #aumenta a cordenada do bonecoa01 (mover para baixo)

    #limitador de tela jogador 01
    if y1 < 0: #verifica se  a posição vertical do elemento (y1) esta acima do limite superior da tela
        y1 = 0 #ajusta a posição para 0, evitando que o elemento saia da tela
    elif y1 > 720 - boneco01.get_height(): #Verifica se a posição vertical do objeto (y1) está abaixo do limite inferior da tela
        y1 = 720 - boneco01.get_height() #ajusta a posição para o limite inferior evitando que o elemento saia da tela

##################################################################################################

    keys = pygame.key.get_pressed() #captura a teclas do teclado
    if keys[pygame.K_o]: #define a tecla "O" para mover o boneco02 para cima
        y2 -= 5 #diminui a cordenada do boneco02 (mover para cima)
    if keys[pygame.K_l]: #define a tecla "L" para mover o boneco02 para baixo
        y2 += 5 #aumenta a cordenada do boneco02 (mover para baixo)

    if y2 < 0: #verifica se  a posição vertical do elemento (y2) esta acima do limite superior da tela
        y2 = 0 #ajusta a posição para 0, evitando que o elemento saia da tela 
    elif y2 > 720 - boneco02.get_height(): #Verifica se a posição vertical do objeto (y2) está abaixo do limite inferior da tela
        y2 = 720 - boneco02.get_height() #ajusta a posição para o limite inferior evitando que o elemento saia da tela 

##################################################################################################

    x3 += vel_x
    y3 += vel_y

    if x3 <= 0 or x3 >= 1280 - bola.get_width():
        vel_x = -vel_x
    if y3 <= 0 or y3 >= 720 - bola.get_height():
        vel_y = -vel_y
        
     # Verifica colisão dos jogadores
    if (x3 < x1 + largura_boneco01 and x3 + largura_bola > x1 and y3 < y1 + altura_boneco01 and y3 + altura_bola > y1) or \
       (x3 + largura_bola > x2 and x3 < x2 + largura_boneco02 and y3 < y2 + altura_boneco02 and y3 + altura_bola > y2):
        vel_x = -vel_x

    if x3 < 0: #a bola passou pela esquerda (ponto jogador02)
        pontos_jogador02 += 1 #adicona 1 ponto para o jogador que marcou ponto
        x3, y3 = 640, 360 #reseta a bola no centro
        vel_x = 7 #reseta a velocidade para o lado direito
        vel_y = 7
    elif x3 > 1280 - largura_bola: #bola passou pela direita (ponto jogador01)
        pontos_jogador01 += 1 #adicona 1 ponto para o jogador que marcou ponto
        x3, y3 = 640, 360 #reseta a bola no centro
        vel_x = -7 #reseta velocidade para o lado esquerdo
        vel_y = 7

##################################################################################################

    #desenha os elementos na tela
    screen.blit(campo, (0,0)) #desenha o elemento campo
    screen.blit(boneco01, (x1,y1)) #desenha o elemento boneco01
    screen.blit(boneco02, (x2, y2)) #desenha o elemento boneco02
    screen.blit(bola, (x3, y3)) #desenha o elemento bola

    #desenha a pontuação na tela
    texto_pontuação = font.render(f"CORINTHIANS: {pontos_jogador01} PALMEIRAS: {pontos_jogador02}", True, branco)
    screen.blit(texto_pontuação, (10,10))

    pygame.display.flip() #atualiza a tela com tudo que foi desenhado
    clock.tick(60) #limita a taxa de quadros para 60 fps

pygame.quit() #fecha o jogo

