from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home_route():
    random_number = random.randint(0,9) 
    print(random_number)
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWYxcTFmOTd5bHJjdThwZzFnOHE1YzRxZTA1bzExYXNqYWN6eTgwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8rN9VXNb7dfU792YQt/giphy.gif"" width=200>'

               )
@app.route("/<int:number>")       
def check_number(number):
    if number > random_number:
        return '<h1>This number is too high</h1>'
    if number<random_number:
        return '<h1>This number is too low</h1>'
    else:
        return '<h1>Bravo ti ga bate</h1>'


    
if __name__ == '__main__':
    app.run(debug=True)