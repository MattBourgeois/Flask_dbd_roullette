import json
with open("data2.json", "r") as d:
	data = json.load(d)

class Killer:
	def __init__(self, Name, Perks, Perk_Description, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_description = Perk_Description
		self.Add_ons = Add_ons
	
	def GetKillerPerks(killer_num ,perk_num):
		print(data["Players"]["Killers"][killer_num]["Perks"][perk_num])
		return data["Players"]["Killers"]["0"]["Perk_Description"][perk_num]
		return data["Players"]["Killers"][killer_num]["Perks"][perk_num]