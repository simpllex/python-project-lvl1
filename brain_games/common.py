import prompt


def welcome_user(game_name):
    print('Welcome to the Brain Games!')
    print(game_name)
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def count_answer(name, list_correct_answer):
    answer_count = 0
    for i in range(len(list_correct_answer)):
        print(list_correct_answer[i][0])
        correct_answer = list_correct_answer[i][1]
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            answer_count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!".format(user_answer,
                                                correct_answer, name))
            break
    if answer_count == 3:
        print("Congratulations, {}!".format(name))


def launch(game_name, list_correct_answer):
    name = welcome_user(game_name)
    count_answer(name, list_correct_answer)
