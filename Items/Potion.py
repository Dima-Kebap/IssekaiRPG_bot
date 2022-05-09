class Potion:
    def __init__(self):
        self.name = "Зелье хп"
        self.description = "зелье хп, лечит вас от легких ранений"
        self.count = 1  # количество
        self.price = 20  # цена
        self.is_used = True# можно ли использовать этот предмет
        self.heal = 10  # сколько хилит(если это хилящий предмет)
        self.addpower = 0  # сколько добавляет силы(если это предмет добавляющий силу)
        self.adddefence = 0  # сколько добавляет защиты(если это предмет добавляющий защиту)
        self.damage = 0  # сколько наносит урона(если это оружие)

    def buy(self, user):  # покупка предмета
        if user.money >= self.price:  # если у пользователя хватает денег, то предмет можно купить
            user.money -= self.price
            if self.name not in user.items.keys():
                user.items[self.name] = self
            else:
                # если у пользователя уже есть этот предмет, то его количество увеличивается на 1
                user.items[self.name].count += 1
            return "Ты успешно купил: " + self.name + "\n\nпо цене " + str(self.price) + " 💵"  # квитанция об оплате
        else:
            return "Прости, Линк. Я не могу предоставить тебе кредит. Возвращайся, когда ты станешь… мммммм… побогаче!"

    def sell(self, user):
        user.money += self.price
        self.count -= 1
        price = str(self.price)
        name = self.name
        if user.items[self.name].count == 0:
            user.items.pop(self.name)
        return "Ты продал {0} и получил {1} 💵".format(name, price)

    def use(self, user):
        message = "Ты использовал " + self.name + " и получил: +"
        if self.heal != 0:
            user.heal(self.heal)
            message = str(self.heal) + " ❤"
        elif self.addpower != 0:
            user.addpower(self.addpower)
            message = str(self.addpower) + " 💪"
        elif self.adddefence != 0:
            user.defence += self.adddefence
            message = str(self.adddefence) + " 🛡"
        self.count -= 1
        if user.items[self.name].count == 0:
            user.items.pop(self.name)
        return message

    def __repr__(self):  # для инвентаря
        return "{0} ({1} общей ценой {2} 💵) :\n{3}\n\n". \
            format(self.name, self.count, self.count * self.price, self.description)

    def shop(self):  # для магазина
        return "{0}\nЦена: {1} 💵 :\n{2}\n\n".format(self.name, self.price, self.description)