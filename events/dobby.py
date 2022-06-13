from events.event import Event
from constants import bot


class Dobby(Event):
    def __init__(self):
        super().__init__()
        self.name = "Добби"
        self.description = "Добби хочет быть свободен. Даш Добби носок? Добби будет очень благодарен."
        self.buttons = ["Дать носок✅", "Не давать носок❌", ""]
        self.is_active = True

    def active_action(self, user, msg):
        if msg == "Не давать носок❌":
            bot.send_message(user.id, "Ты плохой дядя, ты не дал Добби носок")
        elif msg == "Дать носок✅":
            if not ("Носок 🧦" in user.items.keys()):
                bot.send_message(user.id, "У тебя нету носка")
                return
            user.money += 200
            user.items["Носок 🧦"].use(user)
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE8utiod5drKCIr9VFeESUDKJbBgJUIgACgxgAAldJEEn8H67si4stVCQE")
            bot.send_message(user.id, "Cпасибо, вот моя тебе благодарность: \n +200 💵")
