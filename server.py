from flask import Flask
import random

guess_gif='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWZ3and0NngzNXYxeGtramZkOXdobjUydGsxNGFkYTB4MjFxdjIwNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rs2QPsshsFI9zeT4Kn/giphy.gif'
too_high_gif='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
too_low_gif='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
about_right_gif='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

random_number = random.randint(0,10)

app = Flask(__name__)

@app.route('/')
def guess():
    return ("<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"
            f"<center><img style='text-align: center' width='200px' src={guess_gif}></center>")

@app.route('/<int:number>')
def user_guess(number):
    if number > random_number:
        return f"<b><h1 style='color: red; text-align: center'>Too high! Try again</h1></b>\n<center><img src='{too_high_gif}'></center>"
    elif number < random_number:
        return f"<b><h1 style='color: lightblue; text-align: center'>Too Low! Try again</h1></b>\n<center><img src='{too_low_gif}'></center>"
    elif number == random_number:
        return f"<b><h1 style='color: orange; text-align: center'>You found me!!!</h1></b>\n<center><img src='{about_right_gif}'></center>"

if __name__ == "__main__":
# Run app in debug mode
    app.run(debug=True)
