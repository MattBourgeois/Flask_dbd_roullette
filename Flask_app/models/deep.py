import json
with open("data2.json", "r") as d:
	data = json.load(d)

class Killer:
	def __init__(self, Name, Perks, Perk_Description, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_description = Perk_Description
		self.Add_ons = Add_ons
	
	def GetKillerPerks(killer_num):
		m = []
		perk = data["Players"]["Killers"][killer_num]["Perks"]
		# if perk in data["Players"]["Killers"][killer_num]["Perks"]:
		m += perk
		print(m[0])
		return m
		# return data["Players"]["Killers"]["0"]["Perk_Description"][perk_num]