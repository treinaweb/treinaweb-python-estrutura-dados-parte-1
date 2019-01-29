from listas import lista_duplamente_ligada

class Pilha():
    def __init__(self):
        self.__elementos = lista_duplamente_ligada.ListaDuplamenteLigada()

    def empilhar(self, elemento):
        self.__elementos.inserir(elemento)
