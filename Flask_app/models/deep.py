import json, random
with open("data2.json", "r") as d:
	data = json.load(d)

class Killer:
	def __init__(self, Name, Perks, Perk_Descriptions, Add_ons):
		self.Name = Name
		self.Perks = Perks
		self.Perk_Descriptions = Perk_Descriptions
		self.Add_ons = Add_ons
	
	def GetKillerPerks(killer_num, perk_num):
		Killer_perks_list = []
		Killer_perk = data["Players"]["Killers"][killer_num]["Perks"][perk_num]
		Killer_perks_list = Killer_perk
		return Killer_perks_list
	def GetKillerPerkDesc(killer_num, perk_num):
		Killer_perkdesc_list = []
		Killer_perksdesc = data["Players"]["Killers"][killer_num]["Perk_Descriptions"][perk_num]
		Killer_perkdesc_list = Killer_perksdesc
		return Killer_perkdesc_list

class Survivor:
	def __init__(self, Name, Perks, Perk_Descriptions):
		self.Name = Name
		self.Pekrs = Perks
		self.Perk_Description = Perk_Descriptions

	def GetSurvivorPerks(Surv_num, perk_num):
		Survivor_perk_list = []
		Survivor_perk = data["Players"]["Survivors"][Surv_num]["Perks"][perk_num]
		Survivor_perk_list = Survivor_perk
		return Survivor_perk_list
	def GetSurvivorDesc(Surv_num, perk_num):
		Survior_perkdesc_list = []
		Survivor_perksdesc = data["Players"]["Survivors"][Surv_num]["Perk_Descriptions"][perk_num]
		Survior_perkdesc_list = Survivor_perksdesc
		return Survior_perkdesc_list