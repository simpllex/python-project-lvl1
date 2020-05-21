from brain_games.games import calc
from brain_games.common import launch


def main():
    launch(calc.GAME_DESCRIPTION, calc)


if __name__ == '__main__':
    main()
