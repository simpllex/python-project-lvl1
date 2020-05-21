from brain_games.common import launch, NUMBER_OF_ROUNDS
from random import randint
import math

GAME_DESCRIPTION = 'Answer "yes" if given number is prime.'\
                   'Otherwise answer "no".'


def isPrime(number):
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
    random_number = randint(0, 100)
    if isPrime(random_number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (random_number, correct_answer)


def compile_list():
    list_correct_answer = []
    for i in range(NUMBER_OF_ROUNDS):
        list_correct_answer.append(prepare_question_and_answer())
    return list_correct_answer


def start():
    launch(GAME_DESCRIPTION,
           compile_list())
