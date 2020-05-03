from brain_games.games import gcd


def main():
    name = gcd.welcome_user()
    gcd.gcd(name)


if __name__ == '__main__':
    main()
