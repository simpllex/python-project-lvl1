from random import randint
import prompt


def rules_game():
    print('Welcome to the Brain Games!')
    print('Find the greatest common divisor of given numbers.')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def gcd_evclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def gcd(name):
    count_answer = 0
    while count_answer < 3:
        first_random_number = randint(0, 100)
        second_random_number = randint(0, 100)
        print("Question: {} {}".format(first_random_number,
                                       second_random_number))
        correct_answer = gcd_evclid(first_random_number, second_random_number)
        user_answer = prompt.integer('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count_answer += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!".format(user_answer,
                                                correct_answer, name))
            break
    if count_answer == 3:
        print("Congratulations, {}!".format(name))
