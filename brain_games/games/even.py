from brain_games.common import welcome_user, count_answer
from random import randint


def game():
    num = randint(1, 1000)
    q = "Question: {}".format(num)
    if num % 2 == 1:
        return (q, "no")
    else:
        return (q, "yes")


def start():
    name = welcome_user('Answer "yes" if number even otherwise answer "no".')
    list_correct_answer = []
    for i in range(3):
        list_correct_answer.append(game())
    count_answer(name, list_correct_answer)
