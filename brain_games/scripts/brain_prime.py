from brain_games.games import prime


def main():
    name = prime.welcome_user()
    prime.play_game(name)


if __name__ == '__main__':
    main()
