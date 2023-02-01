from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


##Return "Hello World!"
# @app.route('/')
# def hello_world():
#     return 'Hello World!'



##Return "Dojo!"

# @app.route('/dojo')
# def dojo():
#     return 'Dojo!'


##Return HI and whatever name is in the URL after/say/
@app.route('/say/<name>')
def say_hi(name):
    print(name)
    return f"Hi, {name.capitalize()}!"


##Return a given word repeated as many times as specified in the URL
#Takes care of 1st Ninja Bonus
# @app.route('/hello/<string:name>/<int:num>')
# def hello(name, num):
#     return f"Hello {name * num}"


#get it to print on separate lines
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    
    for i in range(0,num):
        output += f'<p>{word}</p>'

    return output

#2nd Ninja Bonus

# @app.route('/hello/<int:num>/<string:name>')
# def hello(num, name):
#     return f"Hello {num * name}"

#3rd Ninja Bonus
# @app.errorhandler(404)
# def page_not_found(mia):
#     return "Sorry! No response. Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

