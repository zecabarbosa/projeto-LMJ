from model.carro import Carro

class carroum(Carro):
    __placa = ""
    __marca = ""
    __modelo = ""
    __cor = ""
    __ano = ""

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo 

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.__placa = placa 

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor    

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __str__(self):
        return f'{super().__str__()};  {self.marca}; {self.modelo};{self.placa}; {self.cor}; {self.ano}; '