from random import randint


import exceptions as ex


import settings as set


class Enemy:
    def __init__(self, level=1):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """return random numbers"""
        return randint(1, 3)

    def decrease_lives(self):
        """decrease lives enemy"""
        self.lives -= 1
        print("Enemy have lives: " + str(self.lives))

        if self.lives == 0:
            raise ex.EnemyDown

class Player:
    def __init__(self, name, allowed_attacks=set.ALLOWED_ATTACKS, lives=set.LIVES_PLAYER, score=0):
        self.name = name
        self.allowed_attacks = allowed_attacks

    @staticmethod
    def fight(attack, defense):
        """returns the result of the round """
        if attack == 1 and defense == 2:  # а==1 д ==2 || а==2 д==3
            return 1
        elif attack == 1 and defense == 3:
            return -1
        elif attack == 2 and defense == 1:
            return -1
        elif attack == 2 and defense == 3:
            return 1
        elif attack == 3 and defense == 1:
            return 1
        elif attack == 3 and defense == 2:
            return -1
        elif attack == defense:
            return 0

    def decrease_lives(self):
        """decrease lives player"""
        self.lives -= 1
        print("You have lives: " + str(self.lives))
        if self.lives == 0:
            raise ex.GameOver(self.name, self.score)

    def attack(self, enemy_obj):
        """attack"""
        player_class = None
        while player_class not in self.allowed_attacks:
            try:
                player_class = int(
                    input('Choose who to attack : 1-Wizard, 2-Warrior, 3-Rogue.'
                          ' Please enter number: '))
                if player_class not in self.allowed_attacks:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")
        enemy_class = Enemy.select_attack()
        result = Player.fight(player_class, enemy_class)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You attacked successfully!")
            self.score += 1
            print("Score: " + str(self.score))
            enemy_obj.decrease_lives()
        else:
            print("You missed!")

    def defence(self):
        """defence"""
        player_class = None
        while player_class not in self.allowed_attacks:
            try:
                player_class = int(
                    input('Choose by whom you defend  : 1-Wizard, 2-Warrior, 3-Rogue.'
                          ' Please enter number: '))
                if player_class not in self.allowed_attacks:
                    raise ValueError
            except ValueError:
                print("Incorrect input!")
        enemy_class = Enemy.select_attack()
        result = Player.fight(enemy_class, player_class)
        if result == 0:
            print("It's a draw!")
        elif result == 1:
            print("You missed!")
            self.decrease_lives()
        else:
            print("You defended yourself!")