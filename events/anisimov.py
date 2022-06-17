import random
from events.active_event import ActiveEvent
from constants import bot


class Anisimov(ActiveEvent):
    def __init__(self):
        answers = {"В чем измеряется сила?": ["В любви", "Дж", "Н"],
                   "Чему равно ускорение свободного падения?": ["10,3", "9,8", "10"],
                   "Что из этого самое тяжелое?": ["Вода", "Лед", "Пар"],
                   "Примерная скорость движения света?": ["300000 км/с", "300000 м/с", "300000 см/с"],
                   "Формула скорости?": ["v/t", "l/t", "t/l"]}
        question = random.choice(list(answers.keys()))
        stats = ["Анисимов",
                 "Вы попали на экзамен к физику Анисимову А.В.\n\nОтветиш верно: +100💵, неверно: -200💵\n\nВнимание: "
                 "вопрос! \n" + question, answers[question]]
        super().__init__(stats)

    def active_action(self, user, msg):
        if msg in ["Н", "9,8", "Вода", "300000 км/с", "l/t"]:
            user.money += 100
            bot.send_message(user.id, "🎉Молодец, правильно🎉\nВот твои 100 💵")
        elif msg in ["В любви", "Дж", "10,3", "10", "Лед", "Пар", "300000 м/с", "300000 см/с", "v/t", "t/l"]:
            val = 200
            if user.money < 200:
                val = user.money
            bot.send_message(user.id, "Неверно! Теперь " + str(val) + " твоих 💵 мои!!!")
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE7MZini34iaGG7nqav_UbdVmTIJbF6wACAgADNpB7Ot2m94b8xdNVJAQ")
            user.minusmoney(val)
