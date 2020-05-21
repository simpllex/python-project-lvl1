from brain_games.games import prime
from brain_games.common import launch


def main():
    launch(prime.GAME_DESCRIPTION, prime)


if __name__ == '__main__':
    main()
