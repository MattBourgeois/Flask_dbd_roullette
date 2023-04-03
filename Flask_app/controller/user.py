from Flask_app import app
from flask import render_template, request, redirect
from Flask_app.models.deep import Killer
import json, random

with open("data2.json", "r") as d:
	data = json.load(d)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def all_info():
	return data["Players"]

@app.route('/random_killer')
def killer_random():
	x = random.randint(0, 32)
	m = Killer.GetKillerPerks(f"{x}", 0)
	return render_template('data.html', m = m)