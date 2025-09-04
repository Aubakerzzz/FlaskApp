from flask import Flask, render_template
application  = Flask(__name__)

# two decorators, same function
@application .route('/')
@application .route('/index.html')
def index():
    return render_template('index.html', the_title='Tiger Home Page')

@application .route('/symbol.html')
def symbol():
    return render_template('symbol.html', the_title='Tiger As Symbol')

@application .route('/myth.html')
def myth():
    return render_template('myth.html', the_title='Tiger in Myth and Legend')


if __name__ == "__main__":
    application.run(debug=True)
