import prompt
def welcome_user():
    name = prompt.string('May I have your name? ')
    template = "Hello, {}!"
    print("Hello, {}!".format(name))