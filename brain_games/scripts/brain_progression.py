from brain_games.games import progression


def main():
    name = progression.welcome_user()
    progression.play_game(name)


if __name__ == '__main__':
    main()
