# Giovanni dos Santos Alves

import requests
import random
url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text # pega as palavras
palavras = palavras.lower() #formata as palavras
palavras = palavras.split() #formata as palavras

forca = [ '''
            _________
           |        |         
           O        |         
                    |         
                    |        
                    |        
                    |
                    |
                --------- ''',
                  '''
            _________
           |        |         
           O        |         
           |        |         
                    |        
                    |        
                    |
                    |
                --------- ''',
                  '''
            _________
           |        |         
           O        |         
          -|        |         
                    |        
                    |        
                    |
                    |
                --------- ''',
                  '''
            _________
           |        |         
           O        |         
          -|-       |         
                    |        
                    |        
                    |
                    |
                --------- ''',
                  '''
            _________
           |        |         
           O        |         
          -|-       |         
          |         |        
                    |        
                    |
                    |
                --------- ''',
                  '''
            _________
           |        |         
           O        |         
          -|-       |         
          | |       |        
                    |        
                    |
                    |
                --------- '''] #forca 

erradas = str() #string para as erradas
certas = str() #string para as certas
juntador = str() # junta todas as letras certas
c = str() #usado como auxiliador para juntar as letras que já estão certas e as novas a colocar
n = 0 # usado para mostrar a forca
letra_certa = str() #a letra certa escolhida que irá ser colocada no juntador
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def chute(a):
    global certas
    global erradas
    global letra
    while letra not in alfabeto:
        letra = input('escolha uma letra: ') #digite uma letra
    while letra in certas or letra in erradas:
        letra = input('já foi, escolha uma letra: ') #digite uma letra
    return letra
def ganhou():
    return print('ganhou')
def desenha():
    return print(forca[n])
def escolhe():
    global escolhida
    escolhida = random.choice(palavras) #escolhe uma palavra do dicionario
    return escolhida
def jogar_novamente(joga):
    global c
    global letra_certa
    global juntador
    global certas
    global erradas
    global n

    letra_certa = str()
    junta = str()
    c = str()
    certas = str()
    juntador = str()
    erradas = str()
    n = 0
    
    if joga == 's' or joga == 'S':
        escolhe()
        for i in range(len(escolhida)): #juntador começa do tamanho da palavra escolhida
            juntador = juntador + '_'
        
        while len(certas) < len(set(escolhida)) and n < 6: #condição de parada
            global letra
            letra = input('digite uma letra: ')
            
            chute(letra)
            if letra in escolhida: #verifica se a letra está na palavra escolhida
                for i in escolhida: # para cada letra da palavra escolhida
                    if letra == i: #se a letra q escolhi é igual a palavra escolhida
                        letra_certa = letra_certa + letra #adiciona a letra escolhida
                    else:
                        letra_certa = letra_certa + '_' #adiciona um '_'
                for i in range(len(letra_certa)):# aqui é onde se junta as palavras
                    if letra_certa[i] != '_': #se a letra é diferente de '_'
                        c = c + letra_certa[i] 
                    elif juntador[i] != '_': #se o juntador é diferente de '_' 
                        c = c + juntador[i]
                    else:
                        c = c + '_' #o 'c' irá receber tanto juntador quanto letra_certa
                juntador = c #juntador é a junção de todas a letras
                c = str() #'c' volta a ser vazio
                letra_certa = str() #letra_certa volta a ser vazio
                certas = certas + letra #adiciona a letra na lista de certas
            else:
                desenha()
                erradas = erradas + letra #adiciona a letra na lista de erradas
                n += 1 #atualiza a forca
                
            print(juntador)
            print('letras certas', certas)
            print('letras erradas',erradas)
    if len(certas) == len(set(escolhida)):
        ganhou()
    if joga == 'n' or joga == 'N':
        print('end game')
    else:
       jogar_novamente(input('quer jogar novamente? digite S/s ou N/n')) 
jogar_novamente(input('quer jogar? digite S/s ou N/n'))
