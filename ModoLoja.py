# Aqui esta todo o algoritmo do modo loja, onde fica armazenado todos os dados de compra

print('''
#################################################################
VOCÊ ESTÁ NO MODO LOJA, AQUI ESTARÁ TODOS OS DADOS DE SUA EMPRESA 
#################################################################
''')
print('''
1 - LISTAR TODOS OS PRODUTOS VENDIDOS
2 - MOSTRAR QUANTIDADE DE CADA PRODUTO VENDIDO
3 - VALOR BRUTO DE TODOS OS PRODUTOS VENDIDOS 
''')

Entrada_Usuario = str(input('DIGITE UMA OPÇÃO: '))

def Selecao_Um():
    pass


# Ao selecionar a opção 2 o codigo a seguir e executado.
def Selecao_Dois():
    # Importa avariavel 'Lista_Temp' do arquivo 'ConversorTXT.py'
    from ConversorTXT import Lista_Temp
    print (Lista_Temp.count ('Cachorro Quente R$: 4.89\n'),'- Cachorro Quente')
    print (Lista_Temp.count ('X-Salada R$: 1.50\n'),'- X-Salada')
    print (Lista_Temp.count ('X-Bacon R$ 2.98\n'),'- X-Bacon')
    print (Lista_Temp.count ('Torrada Simples R$ 2.49\n'),'- Torrada Simples')
    print (Lista_Temp.count ('Refrigerante R$ 2.00\n'),'- Refrigentes')
if Entrada_Usuario == '2':
    Selecao_Dois()



def Selecao_Tres():
    pass

def Selecao_Quatro():
    pass
