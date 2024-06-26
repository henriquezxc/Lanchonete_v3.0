# Software de lanchonete, onde o cliente escolhe seu lanche e no final mostra todo o resumo da compra.
import os
os.system('clear')
# importação do Arquivo ( Cores.py ) para ser usado ao longo do programa.
from Cores import *
# Importamos o arquivo ( DastasHoras.py ) para for as horas na nota fiscal do cliente apos encerra a compra.
from DataHoras import *

def app():
    os.system('clear')
    # Usamos o método ( Def ) apenas para impresão do MENU
    def Menu_Inicial():

        print('___________________________________')
        print('     L̲a̲n̲c̲h̲o̲n̲e̲t̲e̲ B̲e̲s̲t̲ L̲a̲n̲c̲h̲e̲s̲ 🍰    ')
        print('____________________________________')
        print('** C   A   R   D   A   P   I   O  **')
        print('------------------------------------')
        print('CODÍGO     ESPECIFICAÇÃO       PREÇO')
        print('____________________________________')
        print('  1       Cachorro Quente 🌭  R$4.89')
        print('  2         X-Salada   🍔     R$1.50')
        print('  3         X-Bacon    🍔     R$2.98')
        print('  4       Torrada Simples 🥪  R$2.49')
        print('  5        Refrigerante  🍾   R$2.00')
        print('____________________________________')

    # esse metodo pega os nomes que foi acrecentado a lista: nomes_lanches = [] e com .CONT conta quantas vezes foi acrescentado.
    # Assim usando IF também para condições
    def Calculo_de_vezes():
        if nomes_lanches.count('Cachorro Quente R$: 4.89'):
            print('    Cachorro Quente R$: 4.89 X',nomes_lanches.count('Cachorro Quente R$: 4.89'))

        if nomes_lanches.count('X-Salada R$: 1.50'):
            print('    X-Salada R$: 1.50 X',nomes_lanches.count('X-Salada R$: 1.50'))

        if nomes_lanches.count('X-Bacon R$ 2.98'):
            print('    X-Bacon R$ 2.98 X',nomes_lanches.count('X-Bacon R$ 2.98'))

        if nomes_lanches.count('Torrada Simples R$ 2.49'):
            print('    Torrada Simples R$ 2.49 X',nomes_lanches.count('Torrada Simples R$ 2.49'))

        if nomes_lanches.count('Refrigerante R$ 2.00'):
            print('    Refrigerante R$ 2.00 X',nomes_lanches.count('Refrigerante R$ 2.00'))

    # Aqui acionamos o metodo acima:  Menu_Inicial():
    Menu_Inicial()
    # Onde ficará os lanches escolhidos pelo usuario.
    lanches_escolhidos = [ ]
    # Onde irá ficar armazenados os nomes dos lanches.
    nomes_lanches = [ ]
    # Valores de cada lanche na lista já definidos.
    Valores = [ 4.89 , 1.50, 2.98, 2.49, 2.00 ]
    # Laço onde começa todas as operações.
    while True:
        Escolha_do_lanche = str(input('Digite o numero referente ao seu lanche ou digite (SAIR): '))
        # Neste exemplo escolhemos o lanche 1 que e Cachorro-quente
        if Escolha_do_lanche == '1':
            # Se a escolha for '1' o cachorro quente e adicionado na lista: lanches_escolhidos = []
            lanches_escolhidos.append(Valores[0])
            # Agora adicionamos como strig o nome ('Cachorro - Quente') a lista: nomes_lanches = []
            nomes_lanches.append('Cachorro Quente R$: 4.89')
            # Imprimimos uma mensagem para saber qual lanche foi selecionado e adicionado a lista: lanches_escolhidos = []
            print(f'{verde2}Cachorro Quente foi adicionado.{defalt}\n')
        # Os demais continua da mesma forma mensionada acima.
            
        elif Escolha_do_lanche == '2':
            lanches_escolhidos.append(Valores[1])
            nomes_lanches.append('X-Salada R$: 1.50')
            print(f'{verde2}X-Salada foi adicionado.{defalt}\n')

        elif Escolha_do_lanche == '3':
            lanches_escolhidos.append(Valores[2])
            nomes_lanches.append('X-Bacon R$ 2.98')
            print(f'{verde2}X-Bacon foi adicionado.{defalt}\n')

        elif Escolha_do_lanche == '4':
            lanches_escolhidos.append(Valores[3])
            nomes_lanches.append('Torrada Simples R$ 2.49')
            print(f'{verde2}Torrada Simples foi adicionado.{defalt}\n')


        elif Escolha_do_lanche == '5':
            lanches_escolhidos.append(Valores[4])
            nomes_lanches.append('Refrigerante R$ 2.00')
            print(f'{verde2}Refrigerante foi adicionado.{defalt}\n')

        # Usamos o (.UPPER ) apos a variavel para trasformar qualquer entrada por Maiuscula.
        # Deste modo digitando de varias formas a string ( SIM ) ela irá aceitar, evitando erros
        elif Escolha_do_lanche.upper() == 'SAIR':
            # Para ficar mais limpo o resultado, apliquei esse comando ao sair.
            os.system('clear')
            break
        
        # Condição para quando o usuário não digitar a opção certa.
        else:
            print(f'{vermelho2}Entrada Invalida!, Digite um numero correspondente ao pedido.{defalt}')

    # Print para ajudar na organização da compra.
    print('''***************************************
          Resumo Da Compra:
          ''')

    # imprime os nomes dos lanches escolhido que ficou armazenado na lista: nomes_lanches = [] usando metodo Def criado acima
    Calculo_de_vezes()
    # Usamos o (SUM) para fazer a soma usando a lista: lanches_escolhidos = []
    soma = sum(lanches_escolhidos)

    # Condição para impressão de mensagem ao não comprar nenhum item
    if soma <=0:
        print(f'         {vermelho2} Não Houve Compra!{defalt}')

    # Valor final das compras.
    print('_______________________________________')
    print('\n''O Total do seu lanche foi de R$: ''%.2f'%soma,'\n')
    #Função abaixo e designada a horarios, usando o arquivo ( DatasHoras.py ) 
    HorariosNota()
    # Funçao abaixo designada a Datas, Usando o aquivo ( DatasHoras.py )
    DataNota()
    print('***************************************')
    

    # Acrescenta os nomes da lista: nomes_lanches = [] ao arquivo 'Dados.txt' Externo.
    with open('dados.txt','a') as arquivo:
        for valor in nomes_lanches:
            arquivo.write(str(valor)+'\n')
    Menu_main2()


# Menu de interação ao finalizar a compra, com opções adicionais.
def Menu_main2():
    print('''
      _________________________
      DESEJA RENICIAR OU SAIR ?
      1 - COMPRAR NOVAMENTE
      2 - MODO LOJA
      3 - PARAR TODO O PROGRAMA
      _________________________
        ''')

    Entrada_Final = str(input('      DIGITE A OPÇÃO DESEJADA: '))
    if Entrada_Final == '1':
        app() 

    elif Entrada_Final == '2':
        def ModoLoja():
            import ModoLoja
            ModoLoja
        ModoLoja()


    elif Entrada_Final == '3':
        print('Fechando Tudo ...')
        exit()
    else:
        print('ENTRADA INVALIDA!')
app()