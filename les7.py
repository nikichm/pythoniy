import random
import sys
class card(list):

    def __init__(self):
        self.modules = []
        self.modules_p = []
        self.modules_b = []



    def player_cards(self):

        print("=======Your card======== \n")

        for i in range(3):

            self.modules = [ random.randint(1, 90) for _ in range(4)]
            while self.modules.count(" ") < 5:
                c = random.randint(1, 9)
                self.modules.insert(c, " ")
            self.modules_p.append(self.modules)

            print(self.modules, "\n")

    def bot_cards(self):

        print("=======Bot card======== \n")

        for i in range(3):

            self.modules = [ random.randint(1, 90) for _ in range(4)]
            while self.modules.count(" ") < 5:
                c = random.randint(1, 9)
                self.modules.insert(c, " ")
            self.modules_b.append(self.modules)

            print(self.modules, "\n")
    # вывод ровные еще доделать

    def game(self):
        while True:
            box = random.randint(1, 90)
            print("Выпал бочонок", box)
            c = input(" Зачеркнуть или продолжить? Y/N, выйти 0 ")
            if c == "Y":
                y = 0
                for i in self.modules_p:
                    for j in i:
                        if j == box:
                            j = " "
                            y += 1
                if y == 0:
                    print("Ошибка! Проиграли")
                    for i in self.modules_p:
                        print(i, "\n")
                    sys.exit()

            if c == "N":
                for i in self.modules_p:
                    for j in i:
                        if j == box:
                            print("Ошибка! Проиграли")
                            sys.exit()

            if c == "0":
                sys.exit()

            elif c != "0" and c != "N" and c != "Y":
                print("Неверный ввод. Еще раз выберети из пункта меню")


            for i in self.modules_b:
                for j in i:
                    if j == box:
                        j = " "












a = card()
a.player_cards()
a.bot_cards()
a.game()







