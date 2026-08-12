class GameCharacter:
    def __init__(self,name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self,new_health):
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self,new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1 
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {new_level}!")

    def __str__(self):
        ret = []
        ret.append(f"Name: {self.name}")
        ret.append(f"Level: {self.level}")
        ret.append(f"Health: {self.health}")
        ret.append(f"Mana: {self.mana}")
        return '\n'.join(ret)

hero = GameCharacter('Kratos') 
print(hero) 

hero.health -= 130 
hero.mana -= 100   
print(hero)  

hero.level_up() 
print(hero)
