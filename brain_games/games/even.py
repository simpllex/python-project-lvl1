from brain_games.common import launch
from random import randint


def game():
    num = randint(1, 1000)
    q = "Question: {}".format(num)
    if num % 2 == 1:
        return (q, "no")
    else:
        return (q, "yes")


def list_correct():
    list_correct_answer = []
    for i in range(3):
        list_correct_answer.append(game())
    return list_correct_answer


def start():
    launch('Answer "yes" if number even otherwise answer "no".',
           list_correct())
