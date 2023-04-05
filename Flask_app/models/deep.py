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
		m = ""
		# for i in range(1, 4, 1):
		# 	x = random.randint(0, 30)
		# 	Killer.GetKillerPerks(f"{x}", perk_num)

		for perk in data["Players"]["Killers"][killer_num]["Perks"]:
			m += perk
		print(m)
		return m
		# return data["Players"]["Killers"]["0"]["Perk_Description"][perk_num]