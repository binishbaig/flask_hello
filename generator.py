from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, World! We are so cool now!'

@app.route('/binish')
def myroute():
	return 'Hey, My name is Binish. Thanks for visiting my website!'
@app.route('/jimmy')
def jimmyroute():
	return "Hello, my name is Jimmy and this is my website"

if __name__ == '__main__':
	app.run(port=8000)