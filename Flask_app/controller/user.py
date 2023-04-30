from Flask_app import app
from flask import render_template, request, redirect
from Flask_app.models.deep import Killer, Survivor
import json, random, os

pictures_dir = os.path.join(app.static_folder, 'pictures')
picture_filenames = os.listdir(pictures_dir)

with open("data2.json", "r") as d:
	data = json.load(d)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	pictures_dir = os.path.join(app.static_folder, 'pictures')
	picture_filenames = os.listdir(pictures_dir)
	return render_template('index.html', picture_filenames=picture_filenames)

@app.route('/data')
def all_info():
	return data["Players"]

@app.route('/random_killer')
def killer_random():
	Perk_list = []
	for i in range(1, 5, 1):
		random_num = random.randint(0, 32)
		Perk_list.append(Killer.GetKillerPerks(f"{random_num}", 0))
		Perk_list.append(Killer.GetKillerPerkDesc(f"{random_num}", 0))
	return render_template('data.html', Perk_list=Perk_list)

@app.route('/random_surv')
def Surv_random():
	Perk_list = []
	for i in range(1, 5, 1):
		random_num = random.randint(0, 36)
		Perk_list.append(Survivor.GetSurvivorPerks(f"{random_num}", 0))
		Perk_list.append(Survivor.GetSurvivorDesc(f"{random_num}", 0))
	return render_template('Sur.html', Perk_list=Perk_list)
