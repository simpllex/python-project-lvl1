from brain_games.common import welcome_user, count_answer
from random import randint
import math


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


def game():
    random_number = randint(0, 100)
    correct_answer = isPrime(random_number)
    q = "Question: {} ".format(random_number)
    return (q, correct_answer)


def start():
    name = welcome_user('Answer "yes" if given number is prime.'
                        'Otherwise answer "no".')
    list_correct_answer = []
    for i in range(3):
        list_correct_answer.append(game())
    count_answer(name, list_correct_answer)
