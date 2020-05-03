from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def play_game(name):
    answer_count = 0
    while answer_count < 3:
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        random_operation = randint(1, 3)
        if random_operation == 1:
            print("Question: {} + {}".format(first_random_number,
                                             second_random_number))
            correct_answer = first_random_number + second_random_number
        elif random_operation == 2:
            print("Question: {} - {}".format(first_random_number,
                                             second_random_number))
            correct_answer = first_random_number - second_random_number
        else:
            print("Question: {} * {}".format(first_random_number,
                                             second_random_number))
            correct_answer = first_random_number * second_random_number
        user_answer = prompt.integer('Your answer: ')
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
