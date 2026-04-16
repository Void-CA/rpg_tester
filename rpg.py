class Character:
    max_hp = 1000
    def __init__(self):
        self.hp = self.max_hp
        self.lvl = 1
        self.alive = True


    def attack(self,  target, damage):
        if self.alive == False:
            return
        
        target.hp -= damage
        if target.hp <= 0:
            target.alive = False
            target.hp = 0

    def heal(self, target, heal_amount):
        if self.alive == False:
            return
        
        if target.alive == False:
            return
        
        target.hp += heal_amount
        if target.hp > target.max_hp:
            target.hp = target.max_hp