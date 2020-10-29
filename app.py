from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky'\

# favorite animal
@app.route('/gorilla')
def fav_animal():
    return 'Gorillas are awesome!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

# favorite desert
@app.route('/dessert/<users_dessert>')
def fav_dessert(users_dessert):
    return f"I like {users_dessert} too"

# madlib
@app.route('/madlib/<adjective>/<noun>')
def madlib(adjective, noun):
    return f"Hey there {noun}! You look {adjective}"

# multiply 
@app.route('/multiply/<num1>/<num2>')
def multiply(num1, num2):
    if not(num1.isdigit()) or not(num2.isdigit()):
        return "Invalid inputs. Please input 2 numbers."
    else: 
        num1 = int(num1)
        num2 = int(num2)
        result = num1 * num2
        
        return f"{num1} multiplied by {num2} equals {result}"
    



if __name__ == '__main__':
    app.run(debug=True)        
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
