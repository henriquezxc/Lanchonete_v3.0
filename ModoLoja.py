# Aqui esta todo o algoritmo do modo loja, onde fica armazenado todos os dados de compra
from Cores import *

# Ao selecionar a opção 1 o codigo a seguir e executado.
def Selecao_Um():
    with open('dados.txt') as arquivo:
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
                with open('dados.txt','w') as arquivo:
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

def Selecao_Tres():

    # Dicionario onde irá armazenar os dado do aquivo dos ('dados.txt) temporariamente:
    Dicionario = {}

    # Onde pegamos os dados do arquivo externo ( 'dados.txt ) para adicionar no Dicionario acima:
    with open('dados.txt', 'r') as arquivo:
        i = arquivo.readlines()
        Dicionario = i

    # Tive que adicionar as variaveis com valores ZERO pois assim quando estiver apenas 1 lanche para ser somado, não vai dar erros.
    Calculo_cachorro = 0
    Calculo_X_Salada = 0
    Calculo_X_Bacon = 0
    Calculo_Torrada_Simples = 0
    Calculo_Refrigerante = 0

    # Condiçoes para quando for encontrado o o item mensionados fazer os calulos dos lanches.
    # Aqui usamos a condição para caso estiver (Cachorro Quente R$: 4.89) na lista ele entra e faz os comandos necessarios:
    if Dicionario.count('Cachorro Quente R$: 4.89\n'):
        # Abaixo pegamos o valor item acima e multiplicamos por quantas vezes ele tem na lista usando o (.Count) + o valor pré definido acima:
        Calculo_cachorro = 4.89 * (Dicionario.count('Cachorro Quente R$: 4.89\n'))

    if Dicionario.count('X-Salada R$: 1.50\n'):
        # Abaixo pegamos o valor item acima e multiplicamos por quantas vezes ele tem na lista usando o (.Count) + o valor pré definido acima:
        Calculo_X_Salada = 1.50 * (Dicionario.count('X-Salada R$: 1.50\n'))

    if Dicionario.count('X-Bacon R$ 2.98\n'):
        # Abaixo pegamos o valor item acima e multiplicamos por quantas vezes ele tem na lista usando o (.Count) + o valor pré definido acima:
        Calculo_X_Bacon = 2.98 * Dicionario.count('X-Bacon R$ 2.98\n')

    if Dicionario.count('Torrada Simples R$ 2.49\n'):
        # Abaixo pegamos o valor item acima e multiplicamos por quantas vezes ele tem na lista usando o (.Count) + o valor pré definido acima:
        Calculo_Torrada_Simples = 2.49 * Dicionario.count('Torrada Simples R$ 2.49\n')

    if Dicionario.count('Refrigerante R$ 2.00\n'):
        # Abaixo pegamos o valor item acima e multiplicamos por quantas vezes ele tem na lista usando o (.Count) + o valor pré definido acima:
        Calculo_Refrigerante = 2.00 * Dicionario.count('Refrigerante R$ 2.00\n')
    else:
        if len(Dicionario) == 0:
            print(f'{vermelho2}Sua lista está totalmente vazia, pois foi excluida recentemente.{defalt}')
        

    # Toda soma das condições acima são armazenadas nessa variavel:
    Soma_de_todos_os_lanches = (
       Calculo_cachorro
    + Calculo_X_Salada
    + Calculo_X_Bacon
    + Calculo_Torrada_Simples
    + Calculo_Refrigerante
    )
    # Agora imprimimos o resultado dos dados armazenados acima:
    print(f'O Valor Bruto de vendas até o momento e de: {verde2}R$ {round(Soma_de_todos_os_lanches,2)}{defalt}')
    # Usei a função ( round() ) e logo apos a variavel o numero ',2' para 2 casas decimais.
# Menu com as opção apenas para impresão:
def menu_de_opcoes():
    print(f'''
    #################################################################
    {amarelo}VOCÊ ESTÁ NO MODO LOJA, AQUI ESTARÁ TODOS OS DADOS DE SUA EMPRESA{defalt} 
    #################################################################
    ''')
    print(f'''{verde2}
    1 - LISTAR TODOS OS PRODUTOS VENDIDOS NA ORDEM DE COMPRA 
    2 - MOSTRAR QUANTIDADE DE CADA PRODUTO VENDIDO
    3 - VALOR BRUTO DE TODOS OS PRODUTOS VENDIDOS
    0 - LIMPAR TODA A LISTA DE PRODUTOS POR COMPLETO
    {defalt}''')
# Menu usado para a condição de todo modo loja:
def Menu_de_condicoes(): 
    while True:
    
        Entrada_Usuario = str(input('DIGITE UMA OPÇÃO: '))
        if Entrada_Usuario == '1':
            Selecao_Um()
            while True:
                Sair_impressao()
                Entrada_temp_1 = str(input('ESCOLHA UMA OPÇÃO:  ').upper())
                if Entrada_temp_1 == '2':
                    sair_Menu()
                elif Entrada_temp_1 ==  '1':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')

        elif  Entrada_Usuario == '2':
            Selecao_Dois()
            while True:
                Sair_impressao()
                Entrada_temp_2 = str(input('ESCOLHA UMA OPÇÃO:  ').upper())
                if Entrada_temp_2 == '2':
                    sair_Menu()
                elif Entrada_temp_2 ==  '1':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')

        elif Entrada_Usuario == '0':
            Selecao_Zero()
            while True:
                Sair_impressao()
                Entrada_temp_0 = str(input('ESCOLHA UMA OPÇÃO: ').upper())
                if Entrada_temp_0 == '2':
                    sair_Menu()
                elif Entrada_temp_0 ==  '1':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')
        elif Entrada_Usuario == '3':
            Selecao_Tres()
            while True:
                Sair_impressao()
                Entrada_temp_0 = str(input('ESCOLHA UMA OPÇÃO:  ').upper())
                if Entrada_temp_0 == '2':
                    sair_Menu()
                elif Entrada_temp_0 ==  '1':
                    menu_de_opcoes()
                    break
                else:
                    print(f'{vermelho2}Entrada Invalida!{defalt}')
        else:
            print(f'{vermelho2}Entrada Invalida, Escolha a opção certa.{defalt}')

# Usamos essa função apenas para fechar o programa:
def sair_Menu():
    print(f'{vermelho2}SEU PROGRAMA FOI ENCERRADO.{defalt}')
    exit()

def Sair_impressao():
    print(f'''
{azul_bebe}DESEJA CONTINUAR OU SAIR? , SELECIONE UMA OPÇÃO ABAIXO:{defalt}
DIGITE 1 - PARA {verde2}VOLTAR{defalt} AO MODO LOJA
DIGITE 2 - PARA {vermelho2}ENCERRAR{defalt} O PROGRAMA
    ''')

menu_de_opcoes()
Menu_de_condicoes()