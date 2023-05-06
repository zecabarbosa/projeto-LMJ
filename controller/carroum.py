from model.carroum import carroum

def create_cr1(carro):
    #Criar
    carros = open('carroUm.txt', 'a')
    carros.write(str(carro)+'\n')
    carros.close()

def read_cr1():
    #Listar
    lista_carros = []
    carros = open('carroUm.txt', 'r')
    for carro in carros:
        carro = carro.strip()
        carro_objeto = carro.split(';')

        print(carro_objeto)
        carroUm = carroum()
        carroUm.marca = carro_objeto[0]
        carroUm.modelo = carro_objeto[1]
        carroUm.placa = carro_objeto[2]
        carroUm.cor = carro_objeto[3]
        carroUm.ano = carro_objeto[4]
        lista_carros.append(carroUm)

    carros.close()
    return lista_carros

def delete_cr1(carro):
    #Deletar
    carros = open('carroUm.txt', 'r')
    linhas = carros.readlines()
    carros.close()
            
    with open('carroUm.txt', 'w') as arquivo:
        for linha in linhas:
            if carro not in linha:
                arquivo.write(linha)

def update_cr1(carro_Velho, carro_Novo):
    #Alterar
    carros = open('carroUm.txt', 'r')
    linhas = carros.readlines()
    carros.close()

    with open('carroUm.txt', 'w') as arquivo:
        for linha in linhas:
            if carro_Velho in linha:
                linha = linha.replace(carro_Velho,carro_Novo)
            arquivo.write(linha)
            
               