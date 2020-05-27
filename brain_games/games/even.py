from random import randint


GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number):
    return (number % 2 == 1)


def prepare_question_and_answer():
    question = randint(1, 1000)
    if is_even(question):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return (question, correct_answer)
