# Importa a biblioteca Pygame
import pygame

# Inicializa a Pygame
pygame.init()

# Define cores do fundo, personagem, bala e alvo (RGB)
corFundo = (0, 0, 0)
corPersonagem = (255, 255, 255)
corBala = (255, 255, 255)
corAlvo = (255,255,255)

# Define velocidade do alvo e da bala
alvoVelocidade = 1
balaVelocidade = 5

# Define tamanho da tela do jogo em pixels (X,Y)
tamanhoTela = (900, 500)

# Armazena clock do jogo em uma variável
clock = pygame.time.Clock()

# Armazena tela do jogo com o tamanho definido em uma variável
tela = pygame.display.set_mode(tamanhoTela)

# Define o título da janela onde o jogo roda
pygame.display.set_caption("FIRE SPACE")

# Define valores para danos
larguraAlvoDamage = 900
alturaAlvoDamage = 1
posicaoXDamage = 350
posicaoYDamage = 20

# Define número de vidas e pontos inicial
vidas = 3
pontos = 0

# Define altura largura, posição e velocidade do player
x = 0
y = 460
width = 20
height = 40
vel = 5

# Valores iniciais para vetores de movimentação 
vectorX = 0
vectUm = 0
vectDois = 0

# Define posição inicial do alvo
posicaoX = 350
posicaoY = 20

# Define tamanhos do alvo e da bala
larguraAlvo = 200
alturaAlvo = 20
larguraBala = 5
alturaBala = 5

# Define o tamanho e posição do Alvo - Rect(left, top, width, height)
alvo = pygame.Rect(posicaoX, posicaoY, larguraAlvo, alturaAlvo)
alvoDamage = pygame.Rect(posicaoXDamage, posicaoYDamage, larguraAlvoDamage, alturaAlvoDamage)
bala = pygame.Rect(-100, -100, larguraBala, alturaBala)
player = ''

# Define variável de jogo rodando para verdadeiro
gameRun = True

# Define fonte do jogo
arial = pygame.font.SysFont('Arial', 15)

# Função para desenhar textos da UI
def escreveTexto(text, font, text_col, x, y):
    img = font.render (text, True, text_col)
    tela.blit(img, (x, y))

# Loop de jogo rodando
while gameRun:

    # Delay para início do jogo
    pygame.time.delay(1)

    # Loop para verificação de eventos (update)
    for event in pygame.event.get():

        # Evento de quit, finaliza o jogo
        if event.type == pygame.QUIT:
            gameRun = False

    # Variável para verificação de teclas pressionadas
    keys = pygame.key.get_pressed()
    
    # Evento de pressionar a tecla ESPAÇO para atirar
    if keys[pygame.K_SPACE]:
        spawnBullet = True
        if bala.y < 0:
            bala.y = 0
            bala = pygame.draw.rect(tela, (255,255,255), (player.x + 8, player.y, larguraBala, alturaBala))
            bala.y = bala.y - 7

    # Evento de pressionar a tecla SETA ESQUERDA para movimentar para esquerda
    if keys[pygame.K_LEFT]:
        x -= vel

    # Evento de pressionar a tecla SETA DIREITA para movimentar para direita
    if keys[pygame.K_RIGHT]:
        x += vel

    # Soma ponto quando a bala atinge o colisor do alvo e redesenha a bala
    if bala.colliderect(alvo):
        pontos += 1
        bala = pygame.draw.rect(tela, (255,255,255), (-100, -100, larguraBala, alturaBala))
        bala.y = bala.y - 0

    # Desconta vida quando a bala sai da tela sem atingir o alvo
    if (bala.y < 0 and bala.y > -5):
        vidas -= 1

    # Atualiza posições do alvo e bala, redesenhando o fundo da tela
    alvo.x = alvo.x + alvoVelocidade
    bala.y = bala.y - 7
    tela.fill(corFundo) 

    # Escreve textos de vida e pontos na tela
    escreveTexto("LIFE: "+ str(vidas), arial, (255, 255, 255), 0, 0)
    escreveTexto("SCORE: "+ str(pontos), arial, (255, 255, 255), 750, 0)

    # Condições para inverter movimentação horizontal do alvo
    if alvo.x > 700:
        alvoVelocidade = alvoVelocidade * -1
        
    if alvo.x < 1:
        alvoVelocidade = alvoVelocidade * -1 
     
    # Condições para trocar a velocidade do alvo
    if pontos >= 5:
        if alvoVelocidade < 0:
            alvoVelocidade = -3
        elif alvoVelocidade > 0:
            alvoVelocidade = 3

    if pontos >= 10:
        if alvoVelocidade < 0:
            alvoVelocidade = -5
        elif alvoVelocidade > 0:
            alvoVelocidade = 5

    # Rederizações do jogo (tela, alvo, bala e player)
    pygame.draw.rect(tela, corAlvo, alvo)
    pygame.draw.rect(tela, (255, 255, 255), bala)
    player = pygame.draw.rect(tela, (255,255,255), (x, y, width, height))
    pygame.display.update()
    clock.tick(60)

# Finaliza o jogo
pygame.quit()