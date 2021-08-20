from models import Player, Enemy
from exceptions import GameOver, EnemyDown
from settings import ALLOWED_ATTACKS


def play():
    """method play game"""
    name_player = input('Please enter name: ')
    start = input('Please enter START: ')
    if start == 'START':

        player = Player(name=name_player, allowed_attacks=ALLOWED_ATTACKS)
        level_game = 1
        enemy = Enemy(level_game)
        while True:
            try:
                player.attack(enemy)
                player.defence()

            except EnemyDown:
                player.score += 5
                print("You have " + str(player.score) + " score")
                level_game += 1
                print("You level: " + str(level_game))
                enemy = Enemy(level_game)


    else:
        print('ERROR')
        play()


if __name__ == '__main__':
    try:
        play()

    except GameOver:
        print("GameOver")

    except KeyboardInterrupt:
        pass

    finally:
        print('Good bye')
