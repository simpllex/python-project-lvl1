from brain_games.common import launch, NUMBER_OF_ROUNDS
from random import randint


GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def prepare_question_and_answer():
    random_number = randint(1, 1000)
    if random_number % 2 == 1:
        return (random_number, "no")
    else:
        return (random_number, "yes")


def compile_list():
    list_correct_answer = []
    for i in range(NUMBER_OF_ROUNDS):
        list_correct_answer.append(prepare_question_and_answer())
    return list_correct_answer


def start():
    launch(GAME_DESCRIPTION,
           compile_list())
