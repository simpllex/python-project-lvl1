from brain_games.common import launch
from random import randint


def find_gcd_evclid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def game():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    q = "Question: {} {}".format(first_random_number, second_random_number)
    correct_answer = find_gcd_evclid(first_random_number, second_random_number)
    return (q, str(correct_answer))


def list_correct():
    list_correct_answer = []
    for i in range(3):
        list_correct_answer.append(game())
    return list_correct_answer


def start():
    launch('Find the greatest common divisor of given numbers.',
           list_correct())
