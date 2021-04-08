import flask

app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
		return(flask.render_template('homepage.html'))
@app.route('/covid', methods=['GET', 'POST'])
def covid():

		return (flask.render_template('covid.html'))
@app.route('/sofa')
def sofa():
		return(flask.render_template('homepage.html'))

if __name__ == '__main__':
    app.run(debug=True)