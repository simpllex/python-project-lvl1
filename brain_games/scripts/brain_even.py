from brain_games.games import even


def main():
    name = even.welcome_user()
    even.play_game(name)


if __name__ == '__main__':
    main()
