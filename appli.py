from flask import Flask
from flask import render_template
app = Flask(__name__)
Port = 8080
Host = '0.0.0.0'
Debug = True

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

if __name__ == ("__main__"):
	app.run(port=Port,host=Host,debug=Debug)
