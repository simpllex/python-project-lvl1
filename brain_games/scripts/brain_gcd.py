from brain_games.games import gcd
from brain_games.common import launch


def main():
    launch(gcd.GAME_DESCRIPTION, gcd)


if __name__ == '__main__':
    main()
