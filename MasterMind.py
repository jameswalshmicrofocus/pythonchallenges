from random import randint
secret_number = 0
guess = 0
result = 0


def new_game():
    while True:
        new_secret_number()
        guess_count = 0
        while guess_count < 4:
            new_guess()
            parse_guess()
            guess_count = guess_count + 1
            if guess_count == 4:
                global result
                result = 0
                restart_game(result)


def new_secret_number():
    global secret_number
    secret_number = (randint(100, 9999))
    secret_number = ([int(i) for i in str(secret_number)])
    print(secret_number)


def new_guess():
    while True:
        global guess
        guess = input("Take a guess")
        guess = ([int(i) for i in str(guess)])
        if len(guess) == 4:
            break


def parse_guess():
    global guess
    global secret_number
    matches = [i for i, item in enumerate(guess) if item in secret_number]
    matches = len(matches) * "*"
    if len(matches) == 4:
        print("congratulations!!!")
        global result
        result = 1
        restart_game(result)
    else:
        print(matches)


def restart_game(result):
    if result == 0:
        decision = input("Bad Luck! You didn't guess the number, type 'Start' or 'Close'")
    if result == 1:
        decision = input("Well done! You guessed the number, type 'Start' or 'Close'")
    if decision == "Start":
        new_game()
    else:
        exit()

new_game()