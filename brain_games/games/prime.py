from random import randint
import math

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.'\
                   'Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    limit = int(math.sqrt(number))
    i = 2
    while i <= limit:
        if number % i == 0:
            return False
        i += 1
    return True


def prepare_question_and_answer():
    question = randint(0, 100)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question, correct_answer)
