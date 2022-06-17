from enemys import *
from constants import *
from enemys.enemy import *


def bot_fight(user, msg):
    if user.enemy.escape():  # если враг сбежал
        bot.send_message(user.id, user.enemy.name + " сбежал, ну не знаю мог бы его и догнать, "
                                                    "но раз тебе лень то ладно")
        user.enemy = None
        return True
    else:
        is_crit = ""
        if msg == TO_DAMAGE:  # если игрок ударил без оружия
            if user.crit >= random.randint(1, 100):  # если критический
                dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None) * 2)
                is_crit = "критические "
            else:
                dmg_to_enemy = user.enemy.take_damage(user.to_damage(False, None))
        else:  # если игрок использовал оружие
            dmg_to_enemy = user.enemy.take_damage(user.to_damage(True, msg))
        if user.enemy.hp > 0:  # если враг жив
            dmg_to_user = user.take_damage(user.enemy.to_damage())
            if user.hp > 0:  # если пользователь жив
                bot.send_message(user.id, "Ты нанес: {0}{1} 💥\nУ {2} осталось: {3} ❤\n\n"
                                          "{2} ударил: {4} 💥\nУ тебя осталось: {5} ❤".
                                 format(is_crit, dmg_to_enemy, user.enemy.name,
                                        user.enemy.hp, dmg_to_user, user.hp))
            else:  # Если умрет пользователь
                bot.send_message(user.id, "Ты вмэр 💀\n\nПричина смерти: {0}\n\nТвоя статистика:\n".
                                 format(user.enemy.name) + repr(user),
                                 reply_markup=types.ReplyKeyboardMarkup().add('/start'))
                bot.send_sticker(user.id, "CAACAgIAAxkBAAEEms1ibridDAOemzBFkVXyS8LUmExOVgACRxcAAvuxcEvbmQyQSCSazyQE")
                user.menu = DEATH
        else:  # если умрет враг
            enemy = user.enemy
            bot.send_message(user.id, enemy.enemy_loot(user))
            user.enemy = None

            if not (user.add_xp(enemy.xp)):  # если игрок неполучил новый уровень
                return True


def enemy_create(user):  # Генерация мобов
    enemys = [RAT, RAD_COCKROACH, SLIME, ZOMBIE, GOBLIN, GOLLUM, GRASS, CARAVAN]
    if user.lvl >= 5:
        enemys += [BANDIT, CACODEMON, CJ, GORDON, LUKASHENKO, MASTER, NEZUKO, ORK, SUPER_SUS, WEREWOLF]
    if user.lvl >= 15:
        enemys += [DARK_NIGHT, DIO, AGENT_SMITH, OROCHIMARU, KANEKI, DAVY_JONES, BOWSER, DUNGEON_MASTER, LIGHT_YAGAMI]
    user.enemy = Enemy(random.choice(list(enemys)))
    # Описание моба при первой встрече
    return user.enemy
