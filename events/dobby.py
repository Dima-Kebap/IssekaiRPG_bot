from events.active_event import ActiveEvent
from constants import bot


class Dobby(ActiveEvent):
    def __init__(self):
        stats = ["Добби",
                 "Добби хочет быть свободен. Даш Добби носок? Добби будет очень благодарен.",
                 ["Дать носок✅", "Не давать носок❌", ""]]
        super().__init__(stats)

    def active_action(self, user, msg):
        if msg == "Не давать носок❌":
            bot.send_message(user.id, "Ты плохой дядя, ты не дал Добби носок")
        elif msg == "Дать носок✅":
            if not ("🧦" in user.items.keys()):
                bot.send_message(user.id, "У тебя нету носка")
                return
            user.money += 200
            user.items["🧦"].use(user)
            bot.send_sticker(user.id, "CAACAgIAAxkBAAEE8utiod5drKCIr9VFeESUDKJbBgJUIgACgxgAAldJEEn8H67si4stVCQE")
            bot.send_message(user.id, "Cпасибо, вот моя тебе благодарность: \n +200 💵")
