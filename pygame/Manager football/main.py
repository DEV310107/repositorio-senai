import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
pygame.display.set_caption("MANAGER SOCCER 2024")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)


pygame.font.init()
font = pygame.font.Font(None, 32)


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Login/Cadastro')


username = ''
password = ''
active_field = None  
show_message = ''  


users = {}


def draw_text(text, x, y, color=BLACK):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_input_box(rect, active, text):
    color = BLUE if active else GRAY
    pygame.draw.rect(screen, color, rect, 2)
    draw_text(text, rect.x + 5, rect.y + 5)


def login_screen():
    global username, password, active_field, show_message
    
    input_box_user = pygame.Rect(200, 150, 240, 40)
    input_box_pass = pygame.Rect(200, 220, 240, 40)
    button_login = pygame.Rect(270, 300, 100, 40)
    
    running = True
    while running:
        screen.fill(WHITE)

        draw_text('Login / Cadastro', 220, 50)
        draw_text('Nome de Usuário:', 70, 160)
        draw_text('Senha:', 70, 230)
        
  
        draw_input_box(input_box_user, active_field == 'username', username)
        draw_input_box(input_box_pass, active_field == 'password', '*' * len(password))
        
        
        pygame.draw.rect(screen, GRAY, button_login)
        draw_text('Entrar', button_login.x + 20, button_login.y + 10)
        
        if show_message:
            draw_text(show_message, 150, 400, color=(255, 0, 0) if "erro" in show_message.lower() else (0, 255, 0))
        
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_user.collidepoint(event.pos):
                    active_field = 'username'
                elif input_box_pass.collidepoint(event.pos):
                    active_field = 'password'
                elif button_login.collidepoint(event.pos):
                    if username and password:  
                        if username in users:
                            if users[username] == password:
                                show_message = 'Login bem-sucedido!'
                            else:
                                show_message = 'Erro: Senha incorreta!'
                        else:
                            users[username] = password  
                            show_message = 'Usuário cadastrado com sucesso!'
                    else:
                        show_message = 'Erro: Preencha todos os campos!'
            
            if event.type == pygame.KEYDOWN:
                if active_field == 'username':
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif active_field == 'password':
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode
        
        pygame.display.flip()

login_screen()
