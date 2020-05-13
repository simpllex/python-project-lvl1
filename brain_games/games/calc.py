from brain_games.common import welcome_user, count_answer
from random import randint


def game():
    first_random_number = randint(0, 100)
    second_random_number = randint(0, 100)
    random_operation = randint(1, 3)
    if random_operation == 1:
        q = "Question: {} + {}"
        correct_answer = (first_random_number + second_random_number)
    elif random_operation == 2:
        q = "Question: {} - {}"
        correct_answer = (first_random_number - second_random_number)
    else:
        q = "Question: {} * {}"
        correct_answer = (first_random_number * second_random_number)
    return (q.format(first_random_number, second_random_number),
            str(correct_answer))


def start():
    name = welcome_user('What is the result of the expression?')
    list_correct_answer = []
    for i in range(3):
        list_correct_answer.append(game())
    count_answer(name, list_correct_answer)
