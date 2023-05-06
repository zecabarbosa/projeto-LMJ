from model.carrodois import carrodois

def create_cr2(carro):
    #criar
    carros = open('carroDois.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close

def read_cr2():
    #listar
    lista_carros = []
    carros = open('carroDois.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)
        carroDois = carrodois()
        carroDois.marca = carro_objeto[0]
        carroDois.modelo = carro_objeto[1]
        carroDois.placa = carro_objeto[2]
        carroDois.cor = carro_objeto[3]
        carroDois.ano = carro_objeto[4]
        lista_carros.append(carroDois)

    carros.close()
    return lista_carros

def delete_cr2(carro):
    carros = open('carroDois.txt', 'r')
    linhas = carros.readlines()
    carros.close()
            
    with open('carroDois.txt', 'w') as arquivo:
        for linha in linhas:
            if carro not in linha:
                arquivo.write(linha)

def update_cr2(carro_Velho, carro_Novo):
    #Alterar
    carros = open('carrodois.txt', 'r')
    linhas = carros.readlines
    carros.close()

    with open('carrodois.txt', 'w') as arquivo:
        for linha in linhas:
            if carro_Velho in linha:
                linha = linha.replace(carro_Velho,carro_Novo)
                arquivo.write(linha)
