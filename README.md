# rpg_tester

## Dimension de tests unitarios
Las pruebas unitarias se realizaron en todos los casos previstos de cada metodo de la clase "Character", con el fin de verificar que cada metodo se comportara de la manera esperada, y que no se presentaran errores o comportamientos inesperados.

### Pruebas de la clase "Character"

## Preguntas de reflexión:

### Tests de constructor
Al ser un constructor sencillo, se realizaron pruebas para verificar que los atributos "hp", "lvl" y "alive" se inicializaran correctamente al crear una instancia de la clase "Character". Se verificó que el HP inicial fuera 1000, el nivel inicial fuera 1 y que el personaje estuviera vivo.

```python
def test_spawn():
    hero = Character()

    assert hero.hp == 1000
    assert hero.lvl == 1
    assert hero.alive == True
```

### Metodo de ataque 
Se realizaron pruebas para verificar que el método de ataque funcionara correctamente. Se verificó que al atacar a un objetivo, el HP del objetivo se redujera en la cantidad de daño especificada, y que si el HP del objetivo llegaba a 0 o menos, el personaje se marcara como muerto.
```python
def test_survive_attack():
    hero = Character()
    monster = Character()

    hero.attack(monster, 200)

    assert monster.hp == 800
    assert monster.alive == True
```

```python
def test_die_from_attack():
    hero = Character()
    monster = Character()

    hero.attack(monster, 1200)

    assert monster.hp == 0
    assert monster.alive == False
```

### Metodo de curacion
Se realizaron pruebas para verificar que el método de curación funcionara correctamente. Se verificó que al curar a un objetivo, el HP del objetivo aumentara en la cantidad de curación especificada, pero que no superara el HP máximo. También se verificó que no se pudiera curar a un personaje muerto.

```python
def test_heal_alive_character():
    knight = Character()
    healer = Character()

    knight.hp = 500
    healer.heal(knight, 300)

    assert knight.hp == 800
    assert knight.alive == True
```

```python
def test_heal_dead_character():
    knight = Character()
    healer = Character()

    knight.hp = 0
    knight.alive = False
    healer.heal(knight, 300)
    assert knight.hp == 0
    assert knight.alive == False
```

**Observen el código final de su clase Personaje. ¿Tiene dependencias externas o código inútil?**
El código final de la clase "Character" no tiene dependencias externas ni código inútil. Todos los métodos y atributos son necesarios para el funcionamiento de la clase y no hay código que no se utilice.

**Si en el próximo parche del juego el diseñador decide que los personajes nacen con 2000 HP en lugar de 1000, ¿qué es lo primero que deben modificar?**
Lo primero que se debe modificar es el valor de la variable "max_hp" en la clase "Character", ya que esta variable define el HP máximo que un personaje puede tener. Cambiar este valor a 2000 asegurará que los personajes nazcan con 2000 HP en lugar de 1000. Pero esto deberia reflejarse tambien en los tests escritos.

## Resultados de las pruebas unitarias
Todas las pruebas unitarias se ejecutaron correctamente, lo que indica que los métodos de la clase "Character" funcionan según lo esperado. 