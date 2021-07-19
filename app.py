# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# @app.route('/')
# def hello_world():
#     # Instead of returning a string,
#     # we'll return the result of the render_template method, passing in the name of our HTML file
#     return render_template('index.html')


@app.route('/time')
def index():
    return render_template("index.html", phrase="hello", times=5)


@app.route('/success')
def success():
    return "success"


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hi, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


@app.route('/dojo')
def dojo():
    return "dojo"


@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    new = ""
    for item in range(int(number)):
        new += word
    return new


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
