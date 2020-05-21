import prompt


NUMBER_OF_ROUNDS = 3


def ask_name():
    name = prompt.string('May I have your name? ')
    return name


def count_answer(name, list_correct_answer):
    for question, answer in list_correct_answer:
        print("Question: ", question)
        correct_answer = answer
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(user_answer, correct_answer))
            print("Let's try again, {}!".format(name))
            return
        print('Correct!')
    print("Congratulations, {}!".format(name))


def launch(game_name, list_correct_answer):
    print('Welcome to the Brain Games!')
    print(game_name)
    name = ask_name()
    print("Hello, {}!".format(name))
    count_answer(name, list_correct_answer)
