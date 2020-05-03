from brain_games.games import calc


def main():
    name = calc.rules.welcome_user()
    calc.play_game(name)


if __name__ == '__main__':
    main()
