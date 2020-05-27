from random import randint


LENGHT_PROGRESSION = 10
GAME_DESCRIPTION = 'What is the result of the expression?'


def generation_members():
    initial_member = randint(0, 100)
    step_member = randint(0, 25)
    end_member = (initial_member + LENGHT_PROGRESSION * step_member + 1)
    return initial_member, end_member, step_member


def make_progression(start, end, step):
    progression = list(range(start, end, step))
    return progression


def prepare_question_and_answer():
    start, end, step = generation_members()
    progression = make_progression(start, end, step)
    hidden_index = randint(0, LENGHT_PROGRESSION)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(str(x) for x in progression)
    return (question, str(correct_answer))
