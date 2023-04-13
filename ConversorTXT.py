# Feita a leitura de todos os itens do aquivo: 'dados.txt e acrescentando em: Lista_Temp = []
Lista_Temp = []

with open('dados.txt', 'r') as arquivo:
    i = arquivo.readlines()
    for linha in i:
        Lista_Temp.append(linha)