from Events.Event import Event


class Test(Event):
    def __init__(self):
        super().__init__()
        self.description = "Вы заходите в таверну бурную жизни, хотя кто бы мог подумать что у " \
                           "людей в этом захалустье есть деньги хоть на что-то." \
                           " День прошел также хорошо а кошелёк полегчал "

    def action(self, user):
        user.minusmoney(5)
        return "-5 💵"