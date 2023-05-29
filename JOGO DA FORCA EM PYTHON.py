import random #para vir aleatório.
import os
def clear(): os.system('cls')

def jogo_da_forca():
    clear()
    input("""

--- JOGO DA FORCA ---

= FEITO POR EWELLYN, GUSTAVO E MARIA =

-> APERTE "ENTER" PARA COMEÇAR O JOGO! <-
    """)

    escolha = int(input(""" ESCOLHA UMA OPÇÃO:
[1]Jogo da forca em que você escolhe uma palavra 
[2]Jogo da forca com palavra aleatória

Digite a sua opção desejada: \n
""")) 



    #várias opções em cada tema para não ficar repetitivo:
    animais = ['cachorro', 'gato', 'girafa', 'leao', 'porco', 'vaca', 'abelha', 'mosquito', 'zebra', 'gavião']
    comidas = ['banana', 'sushi', 'maçã', 'macarrao', 'melancia', 'arroz', 'beterraba', 'pizza', 'feijoada', 'sopa', 'omelete', 'cuscuz', 'empada']
    cores = ['azul', 'rosa', 'violeta', 'roxo', 'branco', 'preto', 'marrom', 'vermelho', 'verde', 'laranja', 'cinza', 'amarelo']
    objetos = ['bola', 'borracha', 'oculos', 'pedra', 'tesoura', 'sapato', 'relogio', 'ventilador', 'vassoura', 'sabonete', 'garfo', 'garrafa', 'copo', 'canudo', 'anel']

    temaslista = ['animais', 'comidas', 'cores', 'objetos'] #os 4 temas separados

    while escolha != 1 and escolha != 2: #uso de while para ter certeza que não ocorra erros e tenha chance de refazer corretamente.
        clear()
        print('INVÁLIDO, tente novamente.\n')
        escolha = int(input(""" ESCOLHA UMA OPÇÃO:
[1]Jogo da forca em que você escolhe uma palavra 
[2]Jogo da forca com palavra aleatória

Digite a sua opção desejada: 
"""))

    if escolha == 1: #escolha 1 é para a pessoa que está jogando decidir a palavra que quiser
            palavra_usuario = input('Digite a palavra que você deseja para ser adivinhada no jogo da forca: ')
            tema_usuario = input('Digite o tema da palavra que você escolheu: ')

            clear() #limpar o console para o tema não ficar aberto
            print("TEMA: {}".format(tema_usuario))
        
            chances = 7 #as chances que a pessoa tem 
            letras_chutadas = [] #uma lista para adicionar as letras aos poucos
            ganhou = False #determina ainda que o usuário não ganhou

            while True:
                for letra in palavra_usuario: # verifica cada letra dentro da palavra
                    if letra in letras_chutadas: # verifica a letra está dentro das letras que já foram chutadas
                        print(letra, end=" ") ##verifica se a letra está na palavra, caso esteja, ele vai aparecer no código
                    else:
                        print("_", end=" ") ### caso não esteja, ele vai imprimir _ 
                print("\n ")

                chute =  input("Chute uma letra: ").lower() ### escolhe o usuário para chutar uma palavra, o lower é para sempre ser em minúsculo
                
                caracteres =  len(chute)  #lê a quantidade de caracteres
                if caracteres != 1:
                    print("PERDEU UMA CHANCE POR COLOCAR MAIS DE UM CARACTERE!") #vê se o usuário não está tentando burlar, chutando mais de um caractere, caso coloque mais de um caractere ele perde
                letras_chutadas.append(chute) ##adicionar letra na lista de letras chutadas pelwo usuário

                if chute not in palavra_usuario: ##averigua se a letra chutada não está na palavra
                    chances -= 1 #caso não esteja, ele tira uma chance
                
                if chances == 7: #aqui aparece o boneco de acordo com o número de chances restantes
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |             ")
                    print(" |             ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 6:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |             ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 5:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |        |    ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 4:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |       /|    ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 3:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |       /|\   ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 2:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |       /|\   ")
                    print(" |       /     ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 1:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |       /|\   ")
                    print(" |       / \   ")
                    print(" |             ")
                    print("_|___          ")
                elif chances == 0:
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |       ( )   ")
                    print(" |       /|\   ")
                    print(" |       / \   ")
                    print(" |             ")
                    print("_|___          ")

                ganhou = True # colocando que ele ganhou, mas o código irá ler depois e verificar que ele ainda não completou a palavra e definir que ele ainda não ganhou

                for letras in palavra_usuario:
                    if letras not in letras_chutadas:  
                        ganhou = False #verifica se o usuário ganhou ou não, se tiver ainda letras faltando, ele ainda não ganhou

                if chances == 0 or ganhou: #parar o código de inserir letras quando perder as chances ou finalmente ganhou
                        break

            if ganhou:
                print("ganhou") #  -- aqui vai ter o sistema de vitoria
            else:
                print("Perdeu") #  -- vai mostrar a derrota 

    if escolha == 2: #escolha 2 é para ser palavra aleatória.
        tema_escolhido = int(input(""" ESCOLHA UM TEMA:
[1]"ANIMAIS"
[2]"COMIDAS"
[3]"CORES"
[4]"OBJETOS"

Digite sua opção desejada: \n
        """))
        if tema_escolhido == 1: #opção entre o tema "animais"
            palavra_escolhida = random.choice(animais)
            tema_random = "animais"
        elif tema_escolhido == 2: #opção entre o tema "comidas"
            palavra_escolhida = random.choice(comidas)
            tema_random = "comidas"
        elif tema_escolhido == 3: #opção entre o tema "cores"
            palavra_escolhida = random.choice(cores)
            tema_random = "cores"
        elif tema_escolhido == 4: #opção entre o tema "objetos"
            palavra_escolhida = random.choice(objetos)
            tema_random = "objetos"
        while tema_escolhido != 1 and tema_escolhido != 2 and tema_escolhido != 3 and tema_escolhido != 4:
            clear()
            print('\n INVÁLIDO, tente novamente! \n') #uso de while para ter certeza que não ocorra erros e tenha chance de refazer corretamente.
            tema_escolhido = int(input("""ESCOLHA UM TEMA:
[1]"ANIMAIS"
[2]"COMIDAS"
[3]"CORES"   
[4]"OBJETOS"

Digite sua opção desejada: \n
        """))
            if tema_escolhido == 1: #opção entre o tema "animais"
                palavra_escolhida = random.choice(animais)
                tema_random = "animais"
            elif tema_escolhido == 2: #opção entre o tema "comidas"
                palavra_escolhida = random.choice(comidas)
                tema_random = "comidas"
            elif tema_escolhido == 3: #opção entre o tema "cores"
                palavra_escolhida = random.choice(cores)
                tema_random = "cores"
            elif tema_escolhido == 4: #opção entre o tema "objetos"
                palavra_escolhida = random.choice(objetos)
                tema_random = "objetos"
        clear()
        print("TEMA: {}".format(tema_random))
        
        chances = 7 #as chances que a pessoa tem 
        letras_chutadas = [] #uma lista para adicionar as letras aos poucos
        ganhou = False #determina ainda que o usuário não ganhou

        while True:
            for letra in palavra_escolhida: # verifica cada letra dentro da palavra
                if letra in letras_chutadas: # verifica a letra está dentro das letras que já foram chutadas
                    print(letra, end=" ") ##verifica se a letra está na palavra, caso esteja, ele vai aparecer no código
                else:
                    print("_", end=" ") ### caso não esteja, ele vai imprimir _ 
            print("\n ")

            chute =  input("Chute uma letra: ").lower() ### escolhe o usuário para chutar uma palavra, o lower é para sempre ser em minúsculo
            
            caracteres =  len(chute)  #lê a quantidade de caracteres
            if caracteres != 1:
                print("PERDEU UMA CHANCE POR COLOCAR MAIS DE UM CARACTERE!") #vê se o usuário não está tentando burlar, chutando mais de um caractere, caso coloque mais de um caractere ele perde
            letras_chutadas.append(chute) ##adicionar letra na lista de letras chutadas pelwo usuário

            if chute not in palavra_escolhida: ##averigua se a letra chutada não está na palavra
                chances -= 1 #caso não esteja, ele tira uma chance
                print(chances) 
            
            if chances == 7: #aqui aparece o boneco de acordo com o número de chances restantes
                    print("  ________     ")
                    print(" |/       |    ")
                    print(" |             ")
                    print(" |             ")
                    print(" |             ")
                    print(" |             ")
                    print("_|___          ")
            elif chances == 6:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |             ")
                print(" |             ")
                print(" |             ")
                print("_|___          ")
            elif chances == 5:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |        |    ")
                print(" |             ")
                print(" |             ")
                print("_|___          ")
            elif chances == 4:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |       /|    ")
                print(" |             ")
                print(" |             ")
                print("_|___          ")
            elif chances == 3:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |       /|\   ")
                print(" |             ")
                print(" |             ")
                print("_|___          ")
            elif chances == 2:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |       /|\   ")
                print(" |       /     ")
                print(" |             ")
                print("_|___          ")
            elif chances == 1:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |       /|\   ")
                print(" |       / \   ")
                print(" |             ")
                print("_|___          ")
            elif chances == 0:
                print("  ________     ")
                print(" |/       |    ")
                print(" |       ( )   ")
                print(" |       /|\   ")
                print(" |       / \   ")
                print(" |             ")
                print("_|___          ")

            ganhou = True # colocando que ele ganhou, mas o código irá ler depois e verificar que ele ainda não completou a palavra e definir que ele ainda não ganhou

            for letras in palavra_escolhida:
                if letras not in letras_chutadas:  
                    ganhou = False #verifica se o usuário ganhou ou não, se tiver ainda letras faltando, ele ainda não ganhou

            if chances == 0 or ganhou: #parar o código de inserir letras quando perder as chances ou finalmente ganhou
                    break

        if ganhou:
            print("Parabéns, você ganhou!!!!") #  -- aqui vai ter o sistema de vitoria
        else:
            print("Você perdeu :(") #  -- vai mostrar a derrota 
        #  - Coloque  jogar novamente ou menu 

jogo_da_forca()


repeticao = 0
while repeticao == 0:
    opcao = input("Deseja jogar novamente? Responda com 'Sim' para tentar novamente, ou 'Não': ").upper()  #pergunta se deseja jogar novamente ou sair para o menu
    if opcao == "SIM" or opcao == "S": #reinicia o jogo
        jogo_da_forca()
    elif opcao == "NAO" or opcao == "N":
        print("Jogo finalizado!") #inicia um novo jogo
        break