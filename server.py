from flask import Flask
import random

low_kitti = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnRsdzgwZnN3M3JydGI5YmQwNndvdTQ5dGF2NDB4MGJ3NGpwcDdqaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g7YDlrD5YLqfe/giphy.gif"
high_kitti = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHQzdGM0dW52ZHNiazgxZnZ3NHExaXBjOGozdWVmM3psZjhyMWFuZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VxbvpfaTTo3le/giphy.gif"
right_number="https://giphy.com/gifs/viralhog-3oxHQfvDzo7VhSRy8M"
app = Flask(__name__)

random_number = random.randint(0,9) 
print(random_number)
@app.route("/")
def home_route():

    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWYxcTFmOTd5bHJjdThwZzFnOHE1YzRxZTA1bzExYXNqYWN6eTgwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8rN9VXNb7dfU792YQt/giphy.gif" width=200>'

               )
@app.route("/<int:number>")       
def check_number(number):
    if number > random_number:
        return ('<h1 style="color: red;">This number is too high</h1>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHQzdGM0dW52ZHNiazgxZnZ3NHExaXBjOGozdWVmM3psZjhyMWFuZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VxbvpfaTTo3le/giphy.gif" width=200>'
        )
    if number<random_number:
        return ('<h1 style="color: blue;">This number is too low</h1>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnRsdzgwZnN3M3JydGI5YmQwNndvdTQ5dGF2NDB4MGJ3NGpwcDdqaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/g7YDlrD5YLqfe/giphy.gif" width=200>'
        )
            

    else:
        return ('<h1 style="color: gold;">This number is just right</h1>'
                '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc21zdmM5cHB3YXZ3MjFvZnoydDlzZmpnbWRxa2Q3dXQ3OTAwMjIwdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oxHQfvDzo7VhSRy8M/giphy.gif" width=200>'
           )


    
if __name__ == '__main__':
    app.run(debug=True)