# Aqui esta todo o algoritmo do modo loja, onde fica armazenado todos os dados de compra
from Cores import *
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
# Usuario seleciona a opção desejada conforme pede acima. 
Entrada_Usuario = str(input('DIGITE UMA OPÇÃO: '))

# Ao selecionar a opção 1 o codigo a seguir e executado.
def Selecao_Um():
    with open('Dados.txt') as arquivo:
        i = arquivo.read()
        print(i)
# Ao usuario digitar a string '1' irá acionar o def Selecao_Um(): criado acima.
if Entrada_Usuario == '1':
    Selecao_Um()

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
if Entrada_Usuario == '2':
    Selecao_Dois()


# Ao selecionar a opção 3 o codigo a seguir e executado.
def Selecao_Tres():
    pass


def Selecao_Quatro():
    pass


# Ao selecionar a opção 0 o codigo a seguir e executado.
def Selecao_Zero():
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
            Imput_Temporario = str(input('DIGITE A SENHA PARA CONFIRMAR: '))
            if Imput_Temporario == '12345':
                with open('Dados.txt','w') as arquivo:
                    arquivo.write("")
                print(f'{verde2}TODA A LISTA FOI APAGADA COM SUCESSO.{defalt}')
                break
            else:
                print(f'{vermelho2}SENHA INVALIDA! TENTE NOVAMENTE.{defalt}')

    if Entrada_Usuario_Zero == 'NAO':
        print(f'{vermelho2}COMANDO CANCELADO{defalt}')

# Ao usuario digitar a string '0' irá acionar o def Selecao_Zero(): criado acima.
if Entrada_Usuario == '0':
    Selecao_Zero()