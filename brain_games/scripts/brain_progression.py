from brain_games.games import progression


def main():
    name = progression.rules_game()
    progression.quest(name)


if __name__ == '__main__':
    main()
