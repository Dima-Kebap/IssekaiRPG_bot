from Items.Item import Item


class Stand_arrow(Item):
    def __init__(self):
        super().__init__()
        self.name = "Стрела для стэндов"
        self.description = "По легенде, если ты встромиш в себя эту стрелу то у тебя появится могущественный дух " \
                           "хранитель которого называют ""Стэнд"", или это все мифы и ты просто умреш😐"
        self.price = 40  # цена
