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
            try:
                guess = int(values['-GUESS-'])
                attempts += 1

                if guess < secret_number:
                    window['-RESULT-'].update("Загадане число більше.")
                elif guess > secret_number:
                    window['-RESULT-'].update("Загадане число менше.")
                else:
                    window['-RESULT-'].update(f"Ви вгадали число {secret_number} за {attempts} спроб.")
                    break
            except ValueError:
                window['-RESULT-'].update("Будь ласка, введіть ціле число.")

    window.close()

if __name__ == "__main__":
    guess_the_number()
