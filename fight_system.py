import types
import random

from Enemys import *
from constants import *
from telebot import *


def bot_fight(user_id, user, enemys, bot, menu, newlvl):
    if user_id not in enemys.keys():  # создание нового моба, если бот крашнулся посреди боя
        enemy_create(user_id, enemys)
    enemy = enemys[user_id]
    dmg_to_enemy = enemy.take_damage(user.to_damage()) # получение мобом урона от пользователя
    if enemy.hp > 0:  # если враг жив
        dmg_to_user = user.take_damage(enemy.to_damage())
        if user.hp > 0:  # если пользователь жив
            bot.send_message(user_id, "Ты нанес: " + str(dmg_to_enemy) +
                             " 💥\nУ врага осталось:" + str(enemy.hp) +
                             " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                             " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
        else:  # Если умрет пользователь
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            restart = types.KeyboardButton('/start') # предложение игроку начать игру заново
            markup.add(restart)
            bot.send_message(user_id, user.death_msg(), reply_markup=markup)
            bot.send_sticker(user_id, DEATH_STICKER)
            user.menu = DEATH 
    else:  # если умрет враг
        user.money += enemy.money # получение денег с моба
        bot.send_message(user_id, enemy.death + "\n\n" +
                         "За победу над врагом ты получил {0}⭐ и {1}💵".format(enemy.xp, enemy.money))
        user.enemy_count += 1 # счетчик мобов
        user.xp += enemy.xp # получение хр от моба
        enemys.pop(user_id)
        if user.next_lvl(): # проверка условия достиг ли игрок нового уровня
            newlvl(user_id, NEW_LVL) # выдача нового уровня
        else:
            menu(user_id, GAME_MENU)  # показывается игровое меню


def enemy_create(user_id, enemys):  # Генерация мобов
    if user_id not in enemys.keys(): # если игрок не дерется с мобом
        enm = random.randint(1, 4) # генерируем определенного моба на условии того какое число выпадет
        if enm == 1:
            enemys[user_id] = GiantCockroach.GiantCockroach()
        elif enm == 2:
            enemys[user_id] = Rat.Rat()
        elif enm == 3:
            enemys[user_id] = Slime.Slime()
        elif enm == 4:
            enemys[user_id] = Goblin.Goblin()
    # Описание моба при первой встерече
    return enemys[user_id].description + "\n\nХарактеристики врага:\n" + repr(enemys[user_id])

