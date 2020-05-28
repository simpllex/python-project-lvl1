from random import randint

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def prepare_question_and_answer():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = "{} {}".format(first_number, second_number)
    correct_answer = find_gcd(first_number, second_number)
    return (question, str(correct_answer))
