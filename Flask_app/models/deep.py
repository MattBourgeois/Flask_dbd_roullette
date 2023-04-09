import json
with open("data2.json", "r") as d:
	data = json.load(d)

class Killer:
	def __init__(self, Name, Perks, Perk_Description, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_description = Perk_Description
		self.Add_ons = Add_ons
	
	def GetKillerPerks(killer_num, perk_num):
		m = []
		perk = data["Players"]["Killers"][killer_num]["Perks"][perk_num]
		m = perk
		return m
	def GetKillerPerkDesc(killer_num, perk_num):
		a = []
		print(perk_num)
		perks = (data["Players"]["Killers"][killer_num]["Perk_Descriptions"][perk_num])
		a = perks
		return a
