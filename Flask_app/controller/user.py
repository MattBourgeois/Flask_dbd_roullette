from Flask_app import app
from flask import render_template, request, redirect
from Flask_app.models.deep import Killer, Survivor
import json, random

with open("data2.json", "r") as d:
	data = json.load(d)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/data')
def all_info():
	return data["Players"]

@app.route('/random_killer')
def killer_random():
	c = []
	for i in range(1, 5, 1):
		x = random.randint(0, 32)
		a = Killer.GetKillerPerkDesc(f"{x}", 0)
		c.append(Killer.GetKillerPerks(f"{x}", 0))
		c.append(Killer.GetKillerPerkDesc(f"{x}", 0))
	return render_template('data.html', a = a, c=c)

@app.route('/random_surv')
def Surv_random():
	c = []
	for i in range(1, 5, 1):
		x = random.randint(0, 36)
		a = Survivor.GetSurvivorDesc(f"{x}", 0)
		c.append(Survivor.GetSurvivorPerks(f"{x}", 0))
		c.append(Survivor.GetSurvivorDesc(f"{x}", 0))
	return render_template('Sur.html', a = a, c=c)

