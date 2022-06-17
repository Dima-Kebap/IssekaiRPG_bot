class Item:
    def __init__(self, stats):
        self.name = stats[0]
        self.description = stats[1]
        self.price = stats[2]  # цена

    def buy(self, user):  # покупка предмета
        if user.money >= self.price:  # если у пользователя хватает денег, то предмет можно купить
            user.minusmoney(self.price)
            user.add_item(self)
            return "Ты успешно купил: " + self.name + "\n\nпо цене " + str(self.price) + " 💵"  # квитанция об оплате
        else:  # если у пользователя не хватает денег
            return "Прости, Линк. Я не могу предоставить тебе кредит. Возвращайся, когда ты станешь… мммммм… побогаче!"

    def sell(self, user):  # продажа предмета
        self.use(user)
        user.money += self.price
        return "Ты продал {0} и получил {1} 💵".format(self.name, self.price)

    def use(self, user):  # игрок использовал предмет (его количество уменьшается на 1)
        user.items[self.name][1] -= 1
        if user.items[self.name][1] == 0:  # если после использования количество этого предмета в инвентаре стало = 0
            user.items.pop(self.name)

    def __repr__(self):  # описание предмета
        return "{0}\nЦена: {1} 💵 :\n{2}".format(self.name, self.price, self.description)
