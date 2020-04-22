from random import randint

advantage = {"Fire": "Grass", "Grass": "Water", "Water": "Fire"}

def get_disadvantage(val):
	for type, advantage_type in advantage.items():
		if val == advantage_type:
			return type

class Pokemon:
	def __init__(self, name, level, type):
		self.name = name
		self.level = level
		self.type = type
		self.maximum_health = level * 20
		self.current_health = self.maximum_health
		self.ko = False
		self.xp = 0

	def take_hit(self, damage):
		self.current_health -= damage
		self.xp += self.level * damage/2
		if self.current_health <= 0:
			self.ko = True
			print(self.name + " took a debilitating blow and was knocked out. :(")
		else:
			print("Ouch! " + self.name + " took a hit and now has " + str(self.current_health) + " health.")
		self.level_up()

	def regain_health(self, health):
		self.current_health += health
		self.xp += self.level * 10
		return self.name + " was healed and now has " + str(self.current_health) + " health."

	def attack(self, pokemon):
		if self.ko == True:
			print(self.name + " cannot attack he's knocked out.")
		else:
			damage = randint(1, pokemon.maximum_health/2)
			self.xp += self.level * damage
			if advantage.get(self.type) == pokemon.type:
				damage *= 2
				print(self.name + " taking hit with advantage at " + pokemon.name)
				pokemon.take_hit(damage)
			elif get_disadvantage(self.type) == pokemon.type:
				damage %= 2
				print(self.name + " taking hit with disadvantage at " + pokemon.name)
				pokemon.take_hit(damage)
			else:
				print(self.name + "is attacking " + pokemon.name)
				pokemon.take_hit(damage)
			self.level_up()

	def level_up(self):
		if self.xp >= self.level * 100:
			self.level += 1
			print(self.name + " leveled up and is now a level " + str(self.level) + " Pokemon!")

class Trainer:
	def __init__(self, name, number_of_potions):
		self.name = name
		self.number_of_potions = number_of_potions
		self.pokemon = []
		self.active_pokemon = 0

	def use_potion(self):
		active_pokemon = self.pokemon[self.active_pokemon]
		health_max = active_pokemon.maximum_health - active_pokemon.current_health

		if health_max == 0:
			print("Can't use potion. " + active_pokemon.name + "'s health is already full.")
		else:
			active_pokemon.current_health += randint(1, health_max)
			print(active_pokemon.name + "'s health has been restored to " + str(active_pokemon.current_health))


	def add_pokemon(self, pokemon):
		self.pokemon.append(pokemon)
		print(self.name + " picked up " + pokemon.name)

	def attack_trainer(self, trainer):
		self.pokemon[self.active_pokemon].attack(trainer.pokemon[trainer.active_pokemon])
		# if trainer.pokemon[trainer.active_poke


	def change_active_pokemon(self, pokemon):
		if pokemon in self.pokemon:
			index = self.pokemon.index(pokemon)
			if index == self.active_pokemon:
				print(pokemon.name + " is already " + self.name + "'s active pokemon.")
			elif pokemon.ko:
				print("Cannot change active pokemon to " + pokemon.name + ", this pokemon is knocked out.")
			else:
				print("Changing " + self.name + "'s active pokemon to " + self.pokemon[index].name)
				self.active_pokemon = index
		else:
			print(self.name + " does not have a " + pokemon.name)




ash = Trainer("Ash", 1)
rando = Trainer("Some Random Guy", 1)
pikachu = Pokemon("Pikachu", 1, "Grass")
bulbasaur = Pokemon("Bulbasaur", 1, "Water")
charmander = Pokemon("Charmander", 2, "Fire")

ash.add_pokemon(pikachu)
ash.add_pokemon(charmander)
rando.add_pokemon(bulbasaur)

ash.attack_trainer(rando)

ash.change_active_pokemon(charmander)
ash.attack_trainer(rando)
rando.attack_trainer(ash)
ash.change_active_pokemon(pikachu)
print(pikachu.xp)
print(charmander.xp)
