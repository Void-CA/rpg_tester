from rpg import Character

def test_spawn():
    hero = Character()

    assert hero.hp == 1000
    assert hero.lvl == 1
    assert hero.state == 'alive'

def test_survive_attack():
    hero = Character()
    monster = Character()

    hero.attack(monster, 200)

    assert monster.hp == 800
    assert monster.state == 'alive'

def test_die_from_attack():
    hero = Character()
    monster = Character()

    hero.attack(monster, 1200)

    assert monster.hp == 0
    assert monster.state == 'dead'

def test_heal_alive_character():
    knight = Character()
    healer = Character()

    knight.hp = 500
    healer.heal(knight, 300)

    assert knight.hp == 800
    assert knight.state == 'alive'