from random import randint
import prompt


LENGHT_PROGRESSION = 10


def rules_game():
    print('Welcome to the Brain Games!')
    print('What number is missing in the progression?')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def progress():
    number_start_proggression = randint(0, 100)
    number_step_progression = randint(0, 25)
    quest_progression = list(range(number_start_proggression,
                                   number_start_proggression +
                                   LENGHT_PROGRESSION *
                                   number_step_progression + 1,
                                   number_step_progression))
    return quest_progression


def missing_number():
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


def quest(name):
    count_answer = 0
    while count_answer < 3:
        progression = progress()
        m_number = missing_number()
        correct_answer = progression[m_number]
        user_answer = prompt.integer("Question: {}".
                                     format(missing(progression, m_number)))
        if user_answer == correct_answer:
            print('Correct!')
            count_answer += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!".format(user_answer,
                                                correct_answer, name))
            break
    if count_answer == 3:
        print("Congratulations, {}!".format(name))
