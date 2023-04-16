import json
with open("data2.json", "r") as d:
	data = json.load(d)

class Killer:
	def __init__(self, Name, Perks, Perk_Descriptions, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_Descriptions = Perk_Descriptions
		self.Add_ons = Add_ons
	
	def GetKillerPerks(killer_num, perk_num):
		m = []
		perk = data["Players"]["Killers"][killer_num]["Perks"][perk_num]
		m = perk
		return m
	def GetKillerPerkDesc(killer_num, perk_num):
		a = []
		perks = data["Players"]["Killers"][killer_num]["Perk_Descriptions"][perk_num]
		a = perks
		return a

class Survivor:
	def __init__(self, Name, Perks, Perk_Descriptions):
		self.Name = Name
		self.Pekrs = Perks
		self.Perk_Description = Perk_Descriptions

	def GetSurvivorPerks(Surv_num, perk_num):
		m = []
		perk = data["Players"]["Survivors"][Surv_num]["Perks"][perk_num]
		m = perk
		print(m)
		return m

	def GetSurvivorDesc(Surv_num, perk_num):
		a = []
		perks = data["Players"]["Survivors"][Surv_num]["Perk_Descriptions"][perk_num]
		a = perks
		return a