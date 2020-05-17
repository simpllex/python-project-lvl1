from brain_games.common import launch, NUMBER_OF_ROUNDS
from random import randint, choice
import operator


GAME_RULES = 'What is the result of the expression?'


def play():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    operation = ['add', 'sub', 'mul']
    oper = choice(operation)
    f = operator.methodcaller(oper, first_random_number, second_random_number)
    correct_answer = f(operator)
    question = "{} {} {}".format(first_random_number, oper, second_random_number)
    return (question, str(correct_answer))


def list_correct():
    list_correct_answer = []
    for i in range(NUMBER_OF_ROUNDS):
        list_correct_answer.append(play())
    return list_correct_answer


def start():
    launch(GAME_RULES, list_correct())
