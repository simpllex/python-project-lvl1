from brain_games.games import gcd


def main():
    name = gcd.rules_game()
    gcd.gcd(name)


if __name__ == '__main__':
    main()
