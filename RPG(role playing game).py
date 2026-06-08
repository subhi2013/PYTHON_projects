class character:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.xp = 0
        self.level = 1
        self.inventory = []
        self.gold = 0
    def show_status(self):
        print("name:" , self.name)
        print("health:" ,self.health)
        print("level:" , self.level)
        print("xp:" , self.xp)
    def attack(self , enemy):
        damage = 20
        if "sword" in self.inventory:
            damage = 40
        if "shield" in enemy.inventory:
            damage -= 10
            enemy.health -= damage
            print(self.name , "attacked" , enemy.name)
            print("damage:" , damage)
    def is_alive(self):
        if self.health > 0:
            print(self.name , "is alive")
        else:
            print(self.name , "is defeated")
    def heal(self):
        self.health += 10
        print(self.name , "healed")
    def gain_xp(self):
        self.xp += 10
        print(self.name, "gained 10 xp")
    def level_up(self):
        if self.xp >= 50:
            self.level += 1
            self.xp = 0
            print(self.name , "levelled up")
        else:
            print("need more xp")
    def add_item(self, item):
        self.inventory.append(item)
        print(item , "added to inventory")
    def show_inventory(self):
        print("inventory:" , self.inventory)
    def buy_sword(self):
        if self.gold >= 50:
            self.gold -= 50
            self.inventory.append("sword")
            print("sword purchased")
        else:
            print("not enough gold")
    def use_potion(self):
        self.health += 30
        print(self.name, "used a health potion")
    def earn_gold(self):
        self.gold += 50
        print(self.name , "earned 50 gold")
    def defeat_enemy(self,enemy):
        if enemy.health <= 0:
            self.gold += 100
            self.xp += 20
            print(enemy.name , "defeated")
            print("reward: 100 gold and 20 xp")
        else:
            print(enemy.name, "is still alive")
hero = character("kavin" , 100)
dragon = character("dragon" , 150)
hero.show_status()
dragon.show_status()
hero.attack(dragon)
dragon.show_status()
dragon.attack(hero)
hero.show_status()
hero.is_alive()
dragon.is_alive()
hero.heal()
hero.show_status()
for i in range(5):
    hero.gain_xp()
hero.level_up()
hero.show_status()
hero.health = 50
hero.use_potion()
hero.show_status()
boss = character("boss dragon" , 300)
boss.show_status()
hero.attack (boss)
boss.show_status()
hero.earn_gold()
hero.buy_sword()
hero.show_inventory()
print(hero.gold)
boss.add_item("shield")
hero.attack(boss)
boss.show_status()
boss.health = 0
hero.defeat_enemy(boss)
print(hero.gold)
print(hero.xp)