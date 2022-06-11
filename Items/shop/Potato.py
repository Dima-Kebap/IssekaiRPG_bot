from Items.Item import Item


class Potato(Item):
    def __init__(self):
        super().__init__()
        self.name = "🥔"
        self.description = "Основной источних доходов 🇧🇾"
        self.price = 3  # цена
        self.is_used = True  # можно ли использовать этот предмет

    def use(self, user):
        user.heal(5)
        super().use(user)
        return "Ты использовал {0} и получил: +5 ❤\n\nТеперь у тебя {1}/{2} ❤".format(self.name, user.hp, user.max_hp)