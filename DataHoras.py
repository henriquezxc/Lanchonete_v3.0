

def HorariosNota():
    # Usado para mostrar a Hora na nota fiscal
    import time
    print('         Hora Da Compra:',time.strftime("%H:%M"))

def DataNota():
    #Usado para Mostra a tada na hora na nota fiscal
    from datetime import date
    Data_Atual = date.today()
    print(f'       Data Da compra: {Data_Atual.day}/{Data_Atual.month}/{Data_Atual.year}')


DataNota()
HorariosNota()