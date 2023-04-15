# Aqui esta todo o algoritmo do modo loja, onde fica armazenado todos os dados de compra

print('''
#################################################################
VOCÊ ESTÁ NO MODO LOJA, AQUI ESTARÁ TODOS OS DADOS DE SUA EMPRESA 
#################################################################
''')
print('''
1 - LISTAR TODOS OS PRODUTOS VENDIDOS NA ORDEM DE COMPRA 
2 - MOSTRAR QUANTIDADE DE CADA PRODUTO VENDIDO
3 - VALOR BRUTO DE TODOS OS PRODUTOS VENDIDOS
0 - LIMPAR TODA A LISTA DE PRODUTOS DA LISTA
''')
# Usuario seleciona a opção desejada conforme pede acima. 
Entrada_Usuario = str(input('DIGITE UMA OPÇÃO: '))

# Ao selecionar a opção 1 o codigo a seguir e executado.
def Selecao_Um():
    from ConversorTXT import Lista_Temp
    for i in Lista_Temp:
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


