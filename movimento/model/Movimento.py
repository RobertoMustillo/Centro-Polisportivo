from listamovimenti.controller.ControlloreListaMovimenti import ControlloreListaMovimenti


class Movimento():
    def __init__(self, data_movimento, descrizione, importo):
        self.controller = ControlloreListaMovimenti()
        self.indice = self.get_ultimo_id()
        self.indice += 1
        self.id = self.indice
        self.data_movimento = data_movimento
        self.descrizione = descrizione
        self.importo = importo

    def get_ultimo_id(self):
        if not self.controller.get_lista_movimenti():
            return 0
        else:
            indice = len(self.controller.get_lista_movimenti())-1
            print("Indice {}".format(indice))
            movimento = self.controller.get_movimento_by_index(indice)
            print(movimento)
            id = movimento.id
            print(("ID movimento {}".format(id)))
            return id