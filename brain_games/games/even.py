from brain_games.common import launch, NUMBER_OF_ROUNDS
from random import randint


GAME_RULES = 'Answer "yes" if number even otherwise answer "no".'

def play():
    num = randint(1, 1000)
    q = "Question: {}".format(num)
    if num % 2 == 1:
        return (q, "no")
    else:
        return (q, "yes")


def list_correct():
    list_correct_answer = []
    for i in range(NUMBER_OF_ROUNDS):
        list_correct_answer.append(play())
    return list_correct_answer


def start():
    launch(GAME_RULES,
           list_correct())
