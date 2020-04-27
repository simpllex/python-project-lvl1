from random import randint
import prompt


def rules_game():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def random_num():
    num = randint(1, 1000)
    print("Question: {}".format(num))
    if num % 2 == 1:
        return "no"
    else:
        return "yes"


def even_game(name):
    count_answer = 0
    while count_answer < 3:
        random_even = random_num()
        answer = prompt.string('Your answer: ')
        if answer == random_even:
            print("Correct!")
            count_answer += 1
        else:
            print("'{}' is wrong answer ;(."
                  "Correct answer was 'no'.".format(answer))
            print("Let's try again, {}!".format(name))
            break
    if count_answer == 3:
        print("Congratulations, {}!".format(name))

        
