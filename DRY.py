import random
import PySimpleGUI as sg

# Функція для гри "Вгадай число"
def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    layout = [
        [sg.Text("Вгадайте число від 1 до 100.")],
        [sg.InputText(key='-GUESS-')],
        [sg.Button("Вгадати")],
        [sg.Text("", size=(30, 1), key='-RESULT-')],
    ]

    window = sg.Window("Гра 'Вгадай число'", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        if event == "Вгадати":
            guess = get_guess(values)
            attempts += 1

            if compare_guesses(guess, secret_number):
                window['-RESULT-'].update(f"Ви вгадали число {secret_number} за {attempts} спроб.")
                break
            else:
                window['-RESULT-'].update(get_result(guess, secret_number))

    window.close()

# Функція для отримання введення гравця
def get_guess(values):
    try:
        return int(values['-GUESS-'])
    except ValueError:
        raise ValueError("Будь ласка, введіть ціле число.")

# Функція для порівняння введення гравця з загаданим числом
def compare_guesses(guess, secret_number):
    return guess == secret_number

# Функція для відображення результату гри
def get_result(guess, secret_number):
    if guess < secret_number:
        return "Загадане число більше."
    elif guess > secret_number:
        return "Загадане число менше."
    else:
        raise ValueError("Ви вже вгадали число.")

if __name__ == "__main__":
    guess_the_number()

