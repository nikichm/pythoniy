import random
class Person:
    def __init__(self, healf, max_damage, armor ):
        self.healf = float(healf)
        self.max_damage = float(max_damage)
        self.armor = float(armor)

    def _hit(self, max_damage):
        if self.armor > 0:
            self.armor -= 1
            self.healf = self.healf - ((random.randint(80, 120) / 100) * max_damage) * 0.75

        else:
            self.healf = self.healf - ((random.randint(80, 120) / 100) * max_damage)



class Player(Person):
    pass


class Enemy(Person):
    pass


class Game:
    def StartGame(self, player, enemy):
        while enemy.healf > 0 and player.healf > 0:
            if random.random() >= 0.5 :
                enemy._hit(player.max_damage)
            else:
                player._hit(enemy.max_damage)


        if enemy.healf < 0:
            print("You win")
        if player.healf < 0:
            print("You lose")

Y = Player(100.0, 34.5, 3)
N = Enemy(90.0, 45.4, 0)
c = Game()
c.StartGame(Y,N)








