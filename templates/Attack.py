class character:
	def __init__(self,name,race):
		self.name = name
		self.race = race
	damage = 25
	health = 100
	def attack(self,enemy):
		enemy.hit(self.damage)
		self.damage += 10
		def hit(self,damage):
			self.health -= damage
player = character("Петя","Эльф")
org = character("Карл","орг")
player.attack(org)
print(org.health)

		