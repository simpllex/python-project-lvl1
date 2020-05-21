from random import randint


GAME_DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def prepare_question_and_answer():
    random_number = randint(1, 1000)
    if random_number % 2 == 1:
        return (random_number, "no")
    else:
        return (random_number, "yes")
