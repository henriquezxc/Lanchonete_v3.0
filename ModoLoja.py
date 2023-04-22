# Aqui esta todo o algoritmo do modo loja, onde fica armazenado todos os dados de compra
from Cores import *

# Ao selecionar a opção 1 o codigo a seguir e executado.
def Selecao_Um():
    with open('Dados.txt') as arquivo:
        i = arquivo.read()
        print(i)
# Ao usuario digitar a string '1' irá acionar o def Selecao_Um(): criado acima.

# Ao selecionar a opção 2 o codigo a seguir e executado.
def Selecao_Dois():
    # Importa avariavel 'Lista_Temp' do arquivo 'ConversorTXT.py'
    from ConversorTXT import Lista_Temp
    print (Lista_Temp.count ('Cachorro Quente R$: 4.89\n'),'- Cachorro Quente')
    print (Lista_Temp.count ('X-Salada R$: 1.50\n'),'- X-Salada')
    print (Lista_Temp.count ('X-Bacon R$ 2.98\n'),'- X-Bacon')
    print (Lista_Temp.count ('Torrada Simples R$ 2.49\n'),'- Torrada Simples')
    print (Lista_Temp.count ('Refrigerante R$ 2.00\n'),'- Refrigentes')
# Ao usuario digitar a string '2' irá acionar o def Selecao_Dois(): criado acima.

# Ao selecionar a opção 0 o codigo a seguir e executado.
def Selecao_Zero():
    # Contador usado para armazenar a quantidade de erros de senha.
    contador = 0
    print('''
    VOCÊ ESTÁ PRESTES A EXCLUIR TODA BASE SE DADOS !!!
    DIGITE ( S I M ) - PARA EXCLUIR TUDO.
    DIGITE ( N Ã O ) - PARA CANCELAR ESSA OPERAÇÃO.
    ''')
    Entrada_Usuario_Zero = (input('DIGITE AQUI SUA DECISÃO: ').upper())
    if Entrada_Usuario_Zero == 'SIM':
        print(f'''
    {verde2}PARA APAGAR VOCÊ PRECISA DIGITAR A SEGUINTE SENHA:{defalt} {vermelho2}12345{defalt}
        ''')
        while True:
            # Entrada temporaria apenas para esse DEF.
            Imput_Temporario = str(input('DIGITE A SENHA PARA CONFIRMAR: '))
            # Condição onde aceita a senha de 12345 para excluir tudo do banco de dados TXT.
            if Imput_Temporario == '12345':
                # aqui ele acesará o aquivo TXT e irá sobrescrever tudo em branco, com isso a lista irá limpar totalmente.
                with open('Dados.txt','w') as arquivo:
                    arquivo.write("")
                print(f'{verde2}TODA A LISTA FOI APAGADA COM SUCESSO.{defalt}')
                # Comando usado para finalizar o laço e encerrar o programa.
                break
            # Condição usanda para parar o proprama quando erro de senhas ultrapasse os 5 erros.
            if contador == 4:
                print(f'{vermelho2}VOCÊ ERROU A COMBINAÇÃO MAIS DE 5 VEZES! POR ISSO O PROGRAMA ENCERRARÁ.{defalt}')
                # Comando usado para finalizar o laço e encerrar o programa.
                sair_Menu()
                break
            # Usado no laço para imprimir a mensagem de senha ínvalida e mais alguns comandos mensionados abaixo.
            else:
                print(f'{vermelho2}SENHA INVALIDA! TENTE NOVAMENTE.{defalt}')
                # usada para cada erro de senha, somar +1 a variavel ( contador = 0 ) assim podendo manipular ela depois em alguma condição.
                contador = contador +1
                # Essa é a condição para quando o contador estiver perto das 5 tentativas, com isso irá imprimir uma mensagem.
                if contador == 4:
                    print(f'{amarelo}VOCÊ ERROU A SENHA 4 VEZES, VOCÊ SÓ TEM MAIS UMA TENTATIVA.{defalt}')                

    if Entrada_Usuario_Zero == 'NAO':
        print(f'{vermelho2}COMANDO CANCELADO{defalt}')
# Ao usuario digitar a string '0' irá acionar o def Selecao_Zero(): criado acima.

def menu_de_opcoes():
    print(f'''
    #################################################################
    {amarelo}VOCÊ ESTÁ NO MODO LOJA, AQUI ESTARÁ TODOS OS DADOS DE SUA EMPRESA{defalt} 
    #################################################################
    ''')
    print(f'''{verde2}
    1 - LISTAR TODOS OS PRODUTOS VENDIDOS NA ORDEM DE COMPRA 
    2 - MOSTRAR QUANTIDADE DE CADA PRODUTO VENDIDO
    3 - VALOR BRUTO DE TODOS OS PRODUTOS VENDIDOS #Em Desenvolvimento...
    0 - LIMPAR TODA A LISTA DE PRODUTOS POR COMPLETO
    {defalt}''')

def Menu_de_condicoes(): 
    while True:
    
        Entrada_Usuario = str(input('DIGITE UMA OPÇÃO: '))
        if Entrada_Usuario == '1':
            Selecao_Um()
            while True:
                Entrada_temp_1 = str(input('Parar ou continuar: ').upper())
                if Entrada_temp_1 == 'PARAR':
                    sair_Menu()
                elif Entrada_temp_1 ==  'CONTINUAR':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')

        elif  Entrada_Usuario == '2':
            Selecao_Dois()
            while True:
                Entrada_temp_2 = str(input('Parar ou Continuar: ').upper())
                if Entrada_temp_2 == 'PARAR':
                    sair_Menu()
                elif Entrada_temp_2 ==  'CONTINUAR':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')

        elif Entrada_Usuario == '0':
            Selecao_Zero()
            while True:
                Entrada_temp_3 = str(input('Parar ou Continuar: ').upper())
                if Entrada_temp_3 == 'PARAR':
                    sair_Menu()
                elif Entrada_temp_3 ==  'CONTINUAR':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')

def sair_Menu():
    print(f'{vermelho2}SEU PROGRAMA FOI ENCERRADO.{defalt}')
    exit()

menu_de_opcoes()
Menu_de_condicoes()