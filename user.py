from buttons_generator import buttons_generator
from constants import *
from pets import *


class User:

    def __init__(self, uid):
        self.id = uid  # айди пользователя
        self.money = 200  # деньги
        self.max_hp = 100  # максимальное здоровье
        self.hp = self.max_hp  # здоровье
        self.power = 10  # Сила (урон без предметов)
        self.defence = 1  # защита
        self.enemy_count = 0  # кол-во убитых мобов
        self.go_ahead_count = 0  # кол-во совершеных походов
        self.xp = 0  # опыт
        self.lvl = 1  # уровень
        self.menu = MAIN_MENU  # в каком меню находится пользователь
        self.enemy = None  # с каким мобов бьется игрок
        self.event = None  # ивент
        self.crit = 5  # шанс крит удара
        self.items = {}  # предметы в инвентаре в виде "имя_предмета: [предмет, кол-во]"
        # страничка инвентаря (если делать через отдельный аргумент в методе, то работает не так  как нужно почемуто)
        self.inv_page = 1
        self.pet = Pet([None, None, 1, 1, 1])  # без модификаторов
        self.shop_items = []  # какие игрок может купить товары в магазине
        self.last_msg_time = time.time()

    def __repr__(self):  # Статистика пользователя
        msg = "Уровень: {0}\nХП: {1}/{2} ❤\nДеньги: {3} 💵\nОпыт: {4}/{5} ⭐\nСила: {6} 💪\nШанс крита: " \
              "{7} 🎯\nЗащита: {8} 🛡\nУбито мобов: {9} 👹\nСовершено походов: {10} 🚶‍♂". \
            format(self.lvl, self.hp, self.max_hp, self.money, self.xp, int(100 * (1.2 ** (self.lvl - 1))), self.power,
                   self.crit, self.defence, self.enemy_count, self.go_ahead_count)
        if self.pet.name is not None:  # Статистика пользователя + хар-ки питомца (если он есть)
            msg += "\n\nПитомец:\n" + repr(self.pet)
        return msg

    def to_damage(self, weapon, msg):  # Нанесение урона
        if weapon:  # если используется оружие
            return int(self.items[msg][0].damage * (1 + self.power / 50) * self.pet.damage)
        else:  # если не оружие
            return int(self.power * self.pet.power * self.pet.damage)

    def take_damage(self, received_damage):  # Получение урона
        self.hp -= int(max(received_damage - ((self.defence * self.pet.defence) / 2), 0))
        return received_damage

    def add_xp(self, add):  # получение опыта
        self.xp += add
        self.enemy = None  # так как опыт за моба уже получен, то он удаляется из юзера
        # если хватает опыта до нового уровня и уровень не максимальный(25)
        if self.xp >= int(100 * (1.2 ** (self.lvl - 1))) and self.lvl < 25:
            self.xp -= int(100 * (1.2 ** (self.lvl - 1)))
            self.lvl += 1
            self.menu = NEW_LVL
            bot.send_message(self.id, "🎉Ты получил {0} уровень🎉 {1}"
                                      "\n\nТвои характеристики:\n\n"
                                      "Сила: {2} 💪\nЗащита: {3} 🛡\nШанс крита: {4} 🎯\n"
                                      "Максимальное ХП: {5}❤\n\nВыбери какую хар-ку ты хочешь увеличить:".
                             format(self.lvl, self.get_pet(), self.power, self.defence, self.crit, self.max_hp),
                             reply_markup=buttons_generator([ADD_POWER, ADD_DEFENCE, ADD_CRIT, ADD_HP], True))
            return True

    def heal(self, heal_hp):  # хил
        self.hp = min(self.hp + heal_hp, self.max_hp)  # чтобы хп небыло больше максимального

    def minusmoney(self, minus):  # трата денег
        self.money = max(self.money - minus, 0)

    def add_item(self, item):  # добавление предмета в инвентарь
        if item.name not in self.items.keys():  # если такого предмета еще нету в инвентаре
            self.items[item.name] = [item, 1]
        else:  # если такой предмет уже есть, то его количество +1
            self.items[item.name][1] += 1

    def get_pet(self):  # получение питомца
        if not (self.lvl in [5, 15, 25]):
            return ""
        else:
            if self.lvl == 5:
                self.pet = Pet(PUPPY)
            elif self.lvl == 15:
                self.pet = Pet(WOLF)
            elif self.lvl == 25:
                self.pet = Pet(ALPHA_WOLF)
            return "\n\nИ нового питомца:\n\n" + repr(self.pet)
