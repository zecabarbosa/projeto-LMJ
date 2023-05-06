from model.carroum import carroum
from model.carrodois import carrodois

from controller.carroum import create_cr1, read_cr1, delete_cr1,update_cr1
from controller.carrodois import create_cr2, read_cr2, delete_cr2, update_cr2

def menu():
    menu = 1
    menu = 10
    while (menu !=0):
        print("*"*10)
        
        menu_inicial = int(input('Quer cadastrar o carro em qual lista?\n1º - Carro de lista [1]\n2º - Carro de lista [2] \nDigite o número da opção desejada: '))
           
        match menu_inicial:
            case 1:

                menu = int(input("\nPara cadastrar digite >>[1] \nPara listar  digite  >>[2] \nPara excluir um carro digite >>[3] \nPara alterar os dados do veiculo digite >>[4] \nPara sair digite >>[0] \n>>> "))
                match menu: 

                    case 1:
                        print("Cadastro da conta")
                        carroUm = carroum()
                        carroUm.marca = input("Digite a marca: ")
                        carroUm.modelo = input("Digite o modelo: ")
                        carroUm.placa = input("Digite a placa: ")                      
                        carroUm.cor = input("Digite a cor: ")
                        carroUm.ano = input("Digite o ano: ")
                        
                        create_cr1(carroUm)

                    case 2:
                        print("Lista")
                        read_cr1()

                    case 3:
                        carro = input('Qual carro quer excluir?(Digite a informação escrita antes) ')
                        delete_cr1(carro)

                    case 4:
                        carro_Velho = input('qual carro deseja alterar?')
                        carro_Novo = input('Insira os novos Dados: ')
                        update_cr1(carro_Velho, carro_Novo)

            case 2:
                menu = int(input("\nPara cadastrar digite >>[1] \nPara listar  digite  >>[2] \nPara excluir um carro digite >>[3] \nPara alterar os dados do veiculo digite >>[4] \nPara sair digite >>[0] \n>>> "))
                match menu: 

                    case 1:
                        print("Cadastro da conta")
                        carroDois = carrodois()                       
                        carroDois.marca = input("Digite a marca: ")
                        carroDois.modelo = input("Digite o modelo: ")
                        carroDois.placa = input("Digite a placa: ")
                        carroDois.cor = input("Digite a cor: ")
                        carroDois.ano = input("Digite o ano: ")

                        create_cr2(carroDois)

                    case 2:
                        print("Lista")
                        read_cr2()

                    case 3:
                        carro = input('Qual carro quer excluir?(Digite a informação escrita antes)>> ')
                        delete_cr2(carro)   

                    case 4:
                        carro_Velho = input('Qual carro deseja alterar?')
                        carro_Novo = input('Insira os novos Dados: ')
                        update_cr2(carro_Velho, carro_Novo)

