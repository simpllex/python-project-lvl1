from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def check_random_number():
    num = randint(1, 1000)
    print("Question: {}".format(num))
    if num % 2 == 1:
        return "no"
    else:
        return "yes"


def play_game(name):
    answer_count = 0
    while answer_count < 3:
        quest = check_random_number()
        answer = prompt.string('Your answer: ').lower()
        if answer == quest:
            print("Correct!")
            answer_count += 1
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was 'no'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
    if answer_count == 3:
        print("Congratulations, {}!".format(name))
