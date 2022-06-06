from Events.Event import Event


class Tavern(Event):
    def __init__(self):
        super().__init__()
        self.description = "Вы заходите в таверну бурную жизни, хотя кто бы мог подумать что у " \
                           "людей в этом захалустье есть деньги хоть на что-то." \
                           " День прошел также хорошо а кошелёк полегчал "

    def action(self, user):
        if user.money != 0:
            result = min(30, user.money)
            user.minusmoney(result)
            return "-" + str(result) + " 💵"
        else:
            result = min(20, user.hp-1)
            user.take_damage(result)
            return "Так как у вас не нашлось денег заплатить за те 2 литра выпивки что так легко " \
                   "зашли в вас, то охрана заведения любезно, не без силы конечно, выпнула вас от туда.\n\n" \
                   "-" + str(result) + " ❤"
