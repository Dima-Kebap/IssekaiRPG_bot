import types
import random
from Enemys import *
from constants import *
from telebot import *


def bot_fight(user_id, user, enemys, bot, menu):
    if user_id not in enemys.keys():  # создание нового моба, если бот крашнулся посреди боя
        enemy_create(user_id, enemys)
    enemy = enemys[user_id]
    dmg_to_enemy = enemy.take_damage(user.to_damage())
    dmg_to_user = user.take_damage(enemy.to_damage())
    if user.hp > 0:  # если пользователь жив
        if enemy.hp > 0:  # если враг жив
            bot.send_message(user_id, "Ты нанес: " + str(dmg_to_enemy) +
                                      " 💥\nУ врага осталось:" + str(enemy.hp) +
                                      " ❤\n\nВраг ударил: " + str(dmg_to_user) +
                                      " 💥\nУ тебя осталось:" + str(user.hp) + " ❤")
        else:  # если умрет моб
            user_reward_money = enemy.reward_money()
            user.money += user_reward_money
            bot.send_message(user_id, enemy.death + "\n\n" + "ты получил {0}💵".format(user_reward_money))
            enemys.pop(user_id)
            menu(user_id)  # показывается игровое меню
    else:  # Если умрет пользователь
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        restart = types.KeyboardButton('/start')
        markup.add(restart)
        bot.send_message(user_id, user.death(), reply_markup=markup)
        bot.send_sticker(user_id, DEATH_STICKER)


def enemy_create(user_id, enemys):  # Генерация мобов
    if user_id not in enemys.keys():
        enm = random.randint(1, 2)
        if enm == 1:
            enemys[user_id] = GiantCockroach.GiantCockroach()
        elif enm == 2:
            enemys[user_id] = Rat.Rat()
    # Описание моба при первой встерече
    return enemys[user_id].description + "\n\nХарактеристики врага:\n" + repr(enemys[user_id])
