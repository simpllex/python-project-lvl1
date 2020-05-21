from brain_games.games import even
from brain_games.common import launch


def main():
    launch(even.GAME_DESCRIPTION, even)


if __name__ == '__main__':
    main()
