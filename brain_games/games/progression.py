from brain_games.common import launch, NUMBER_OF_ROUNDS
from random import randint


LENGHT_PROGRESSION = 10
GAME_RULES = 'What is the result of the expression?'


def make_progression():
    number_start_proggression = randint(0, 100)
    number_step_progression = randint(0, 25)
    quest_progression = list(range(number_start_proggression,
                                   number_start_proggression +
                                   LENGHT_PROGRESSION *
                                   number_step_progression + 1,
                                   number_step_progression))
    return quest_progression


def skip_number():
    return randint(0, LENGHT_PROGRESSION)


def missing(quest_progression, number):
    missed_number = number
    string_progression = ""
    for i in range(0, LENGHT_PROGRESSION):
        if i != missed_number:
            string_progression += str(quest_progression[i]) + " "
        else:
            string_progression += ".. "
    return string_progression


def play():
    progression = make_progression()
    missed_number = skip_number()
    correct_answer = progression[missed_number]
    q = missing(progression, missed_number)
    return (q, str(correct_answer))


def list_correct():
    list_correct_answer = []
    for i in range(NUMBER_OF_ROUNDS):
        list_correct_answer.append(play())
    return list_correct_answer


def start():
    launch(GAME_RULES, list_correct())
