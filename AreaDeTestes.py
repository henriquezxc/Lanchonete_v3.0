
with open('dados.txt') as arquivo:
        # x = arquivo.read()
        i = arquivo.read()
        if len(i) >= 1:
            print('A lanchonete vendeu:')
            print(i)
            lista = [ ]
            lista.append(i)
            print(len(lista))