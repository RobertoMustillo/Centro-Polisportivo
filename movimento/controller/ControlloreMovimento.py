class ControlloreMovimento():
    def __init__(self, movimento):
        self.model = movimento

    def get_id_movimento(self):
        return self.model.id

    def get_data_movimento(self):
        return self.model.data_movimento

    def get_descrizione_movimento(self):
        return self.model.descrizione

    def get_importo_movimento(self):
        return self.model.importo