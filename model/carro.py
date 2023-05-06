class Carro:
    __pais = "Brasil"
    __estado = "SC"

    @property
    def pais(self):
        return self.__pais
    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado):
        self.__estado = estado    

    def __str__(self):
        return f'{self.pais}; {self.estado}'