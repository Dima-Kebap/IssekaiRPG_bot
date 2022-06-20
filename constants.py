from items import *
from config import TELEGRAM_TOKEN
from telebot import *

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# # # # # # # # # #   Действия   # # # # # # # # # #
RUN = "Сбежать 🏃‍♂"
START_NEW_GAME = "Начать свое приключение 🕹"
SUPPORT = "Поддержка ☎"
SHOP = "Магазин 🏪"
GO_AHEAD = "Продолжить путь 🚶‍♂"
TO_DAMAGE = "Нанести урон 💥"
CONTINUE_GAME = "Продолжить приключение 🕹"
STATISTICS = "Статистика 👤"
ADD_POWER = "Сила 💪 +2"
ADD_DEFENCE = "Защита 🛡 +2"
ADD_CRIT = "Шанс крита 🎯 +1"
ADD_HP = "Максимальное ХП ❤ +10"
BACK = "◀ Назад ◀"
INVENTORY = "Инвентарь 🎒"
NEXT_PAGE = "▶Следующая страничка▶"
BACK_PAGE = "◀Предидущая страничка◀"
# # # # # # # # # #   меню игрока   # # # # # # # # # #
MAIN_MENU = "◀ В главное меню ◀"
GAME_MENU = 1
FIGHT_MENU = 2
DEATH = 3
NEW_LVL = 4
EVENTS_MENU = 5
SHOP_MENU = 6
INVENTORY_MENU = 7

# предметы которые продаются в магазине
SHOP_ITEMS = {"Свиток силы": Scroll(SCROLL_OF_POWER),
              "Свиток защиты": Scroll(SCROLL_OF_DEFENCE),
              "Свиток крита": Scroll(SCROLL_OF_CRIT),
              "Малое зелье хп": HealItem(SMALL_HP_POTION),
              "Среднее зелье хп": HealItem(MEDIUM_HP_POTION),
              "Большое зелье хп": HealItem(BIG_HP_POTION),
              "🍌": HealItem(BANANA),
              "Лом": Weapon(SCRAP),
              "🧦": Item(SOCK),
              "🍬": HealItem(CANDY),
              "🥔": HealItem(POTATO),
              "Мидии": HealItem(MUSSELS),
              "Световой меч": Weapon(LIGHTSABER),
              "Экскалибур": Weapon(EXCALIBUR),
              "Яростный меч": Weapon(FURIOUS_SWORD),
              "Золотой меч": Weapon(GOLDEN_SWORD),
              "Железный меч": Weapon(IRON_SWORD)}

# лут с мобов
LOOT = {"Клык": Item(FANG),
        "Кольцо всевластия": Item(RING_OF_OMNIPOTENCE),
        "Мясо 🥩": Item(MEAT),
        "Большой глаз 👁": Item(BIG_EYE),
        "Золотая кнопка ютуба": Item(GOLDEN_YTB),
        "Серебряная кнопка ютуба": Item(SILVER_YTB),
        "Шерсть": Item(WOOL),
        "Рог": Item(HORN),
        "Белая майка": Item(WHITE_SHIRT),
        "Солнцезащитные очки": Item(SUNGLASSES),
        "Щупальце": Item(TENTACLE),
        "Стрела для стэндов": Item(STAND_ARROW),
        "Фуражка полицая": Item(POLICE_CAP),
        "Ремень Билли": Item(BELT_BILLY),
        "Панцырь большой черепахи": Item(TURTLE_SHELL),
        "Кадык": Item(ADAMS_APPLE),
        "🍬": HealItem(CANDY),
        "Мидии": HealItem(MUSSELS),
        "🥔": HealItem(POTATO)}
