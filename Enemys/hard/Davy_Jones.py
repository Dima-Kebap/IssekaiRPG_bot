from Items import *
from Enemys.Enemy import Enemy


class Davy_Jones(Enemy):  # Параметры будут меняться
    def __init__(self):
        super().__init__()
        self.max_hp = 180
        self.hp = self.max_hp  # хп противника
        self.damage1 = 9
        self.damage2 = 13
        self.money = 140
        self.xp = 300
        self.name = "Дейви Джонс"
        self.description = 'Тот злодей из фильма Диснея когда они снимали не говно, ну там еще Джони Депп был'
        self.death = "Сегодня салата из кальмаров всем хватит, огурчики б еще найти."
        self.sticker = "CAACAgIAAxkBAAEE-ApipKfArPCY5jj4fl2PgtvRQFXRpgACXxsAAn36KEkdrYfAjn7AwCQE"
        self.loot = [Mussels()]
