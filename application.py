from flask import request
from flask import Flask,render_template
import os
import fetch
application = Flask(__name__)
@application.route('/', methods=['POST', 'GET'])
def index(tweets=None):
	error=None
	if request.method=='POST':
		key=request.form['keyword']
		# os.system('python loadfetch.py '+key)
		list_of_tweets=fetch.fetch(key)
		return render_template('home.html',tweets=list_of_tweets, keyword=key)
	return render_template('home.html',tweets=None)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
