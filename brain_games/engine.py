import prompt


NUMBER_OF_ROUNDS = 3


def ask_name():
    name = prompt.string('May I have your name? ')
    return name


def play_game(name, game):
    for i in range(NUMBER_OF_ROUNDS):
        question, correct_answer = game.prepare_question_and_answer()
        print("Question: ", question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print("Congratulations, {}!".format(name))


def launch(game):
    print('Welcome to the Brain Games!')
    print(game.GAME_DESCRIPTION)
    name = ask_name()
    print("Hello, {}!".format(name))
    play_game(name, game)
