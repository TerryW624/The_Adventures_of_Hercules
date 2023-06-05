from random import choices
#"pygames" ===> This is for testing creating a visual environment and should be done after project completion
class Character:
    def __init__(self, name, health):
        # should have a collision event (pygames)
        # should have armor
        # should have abilities
        # Should have inventory
        #   If not hercules inventory should be 1 item
        #   that one item should be dropped on death
        # Should have levels
        # Should have 2 turn locked attacks and one basic attack
        # For Hercules:
        #   Turn locked attacks should increment with levels
        #   Basic attacks should increment OR decrement depending on gear
        self.name = name
        self.weights = [0.10, 0.90]
        self.health = health
    
    def attack_enemy(self):
        attack_or_miss = ["Missed", "Attack"]
        attack_chance = choices(attack_or_miss, self.weights, k=10)
        return attack_chance
    
class Hercules(Character):
    def __init__(self, name, health):
        super().__init__(name, health)

class Entity(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
    # Should drop inventory on death
    pass

class Mobs(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Margwa(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class NemeanLion(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class LernaeanHydra(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
        # two heads are better than one
        #   every 2 rounds regains half of the lost health

class StymphalianBird(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Diomedes(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    #you can slay diomedes and his men and use them for horse bait or
    #Group fight (Attacked 3 times every turn)
    #No giant Horse fight
    #missed attack up 12.5%
    
    def rebalancing_player_missed_rate(self):
        while True:
            previous_weights = [0.10, 0.90]
            Hercules.weights = previous_weights
            if Diomedes.health > 0:
                Hercules.weights[0] += 0.125
                Hercules.weights[1] -= 0.125
            else:
                Hercules.weights = previous_weights
                return

class GiantHorses(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    #you can fight the giant horses and capture them injured
    #Horses will have higher health and armor missed attack up 25% will be higher
    
    def rebalancing_player_missed_rate():
        while True:
            previous_weights = [0.10, 0.90]
            Hercules.weights = previous_weights
            if GiantHorses.health > 0:
                Hercules.weights[0] += 0.25
                Hercules.weights[1] -= 0.25
            else:
                Hercules.weights = previous_weights
                return

class Hippolyta(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Geryon(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Ladon(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Cerberus(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class KingAugeus(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    # Killing Augeus nets leather armor +4 armor

class KingEurystheus(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)

class Helios(Entity):
    def __init__(self, name, health):
        super().__init__(name, health)
    #If you let Augeus live Helios grants you a Shining Sword for +6 attack or increment to ability

Person = Character("Argos")
print(Person.attack_enemy())