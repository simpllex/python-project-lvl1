from random import randint


LENGHT_PROGRESSION = 10
GAME_DESCRIPTION = 'What is the result of the expression?'


def make_progression():
    start_progression = randint(0, 100)
    step_progression = randint(0, 25)
    end_progression = (start_progression
                       + LENGHT_PROGRESSION
                       * step_progression + 1)
    quest_progression = list(range(start_progression,
                                   end_progression,
                                   step_progression))
    return quest_progression


def prepare_question_and_answer():
    progression = make_progression()
    hidden_index = randint(0, LENGHT_PROGRESSION)
    correct_answer = progression[hidden_index]
    question = progression[:]
    question[hidden_index] = '..'
    return (' '.join(str(x) for x in question), str(correct_answer))
