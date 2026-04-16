class Character:
    max_hp = 1000
    def __init__(self):
        self.hp = self.max_hp
        self.lvl = 1
        self.state = 'alive'


    def attack(self,  target, damage):
        if self.state == 'dead':
            return
        
        target.hp -= damage
        if target.hp <= 0:
            target.state = 'dead'
            target.hp = 0

    def heal(self, target, heal_amount):
        if self.state == 'dead':
            return
        
        if target.state == 'dead':
            return
        
        target.hp += heal_amount
        if target.hp > target.max_hp:
            target.hp = target.max_hp