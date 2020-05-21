from random import randint, choice
import operator


GAME_DESCRIPTION = 'What is the result of the expression?'


OPERATIONS = {'add': '+',
              'sub': '-',
              'mul': '*'}


def prepare_question_and_answer():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operation = choice(list(OPERATIONS.keys()))
    calculation = operator.methodcaller(operation, first_number, second_number)
    correct_answer = calculation(operator)
    question = "{} {} {}".format(first_number, OPERATIONS.get(operation),
                                 second_number)
    return (question, str(correct_answer))
