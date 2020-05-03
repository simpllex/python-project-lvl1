from random import randint
import math
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def isPrime(number):
    if number < 2:
        return "no"
    if number == 2:
        return "yes"
    limit = int(math.sqrt(number))
    i = 2
    while i <= limit:
        if number % i == 0:
            return "no"
        i += 1
    return "yes"


def play_game(name):
    answer_count = 0
    while answer_count < 3:
        random_number = randint(0, 100)
        correct_answer = isPrime(random_number)
        user_answer = prompt.string("Question: {} ".format(random_number))
        user_answer = user_answer.lower()
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
