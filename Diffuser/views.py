from Diffuser import app
from flask import (request, url_for, redirect, render_template, flash,
                   session, g, json, Blueprint, make_response, Flask)


@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		print "GET happened"
		return render_template('index.html')
	elif request.method == 'POST':
		print "POST happened"
		print request.form
		return render_template('index.html')




    
