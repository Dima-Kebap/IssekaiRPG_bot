from Items.Item import Item


class Sock(Item):
    def __init__(self):
        super().__init__()
        self.name = "Носок 🧦"
        self.description = "Этот носок может комуто помочь стать свободным"
        self.price = 100  # цена
