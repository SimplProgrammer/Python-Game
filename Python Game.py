import os
import random
import time


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class Dice:
    def die(number):
        die = random.randint(1, number)
        return die


class Characters:
    def __init__(self, name, level, health, stamina, inventory):
        self.name = name
        self.level = level
        self.health = health
        self.stamina = stamina
        self.inventory = inventory


class Player(Characters):
    def __init__(self):
        super().__init__(name=input("What is your name: "), level=1,
                         health=50, stamina=60, inventory={"Coins": 0})


class Skeleton(Characters):
    def __init__(self):
        super().__init__(name="Skeleton", level=1, health=20,
                         stamina=40, inventory={"Coins": random.randint(1, 100)})


class Ghoul(Characters):
    def __init__(self):
        super().__init__(name="Ghoul", level=1, health=25,
                         stamina=38, inventory={"Coins": random.randint(1, 100)})


def random_enemies():
    roll = Dice.die(3)
    if roll == 1:
        enemy1 = Ghoul()
    else:
        enemy1 = Skeleton()
    return enemy1


def start():
    print("Welcome to Dungeon Sweepers! ")
    print("Press (x) to start and press (z) to Exit")
    start_question = input(">>> ")
    if start_question == "x":
        print("Welcome! ")
    elif start_question == "z":
        print("Goodbye.")
        exit()
    else:
        cls()
        print("This isn't the demanded value :(")
        start()


def mob_refresh():
    if enemy1 == Skeleton():
        enemy1.level = enemy1.level + 1
        enemy1.health = enemy1.level*20
        enemy1.inventory = {"Coins": Dice.die(100)}
    else:
        enemy1.level = enemy1.level + 1
        enemy1.health = enemy1.level*25
        enemy1.inventory = {"Coins": Dice.die(100)}


def player_options():
    while True:
        if hero1.health <= 0:
            print("You are dead!")
            print("Game Over")
            exit()
        elif enemy1.health <= 0:
            print("Your enemy is dead!")
            print(f"You have gained {enemy1.inventory} coins")
            gain = hero1.inventory["Coins"] + enemy1.inventory["Coins"]
            hero1.inventory["Coins"] = gain
            mob_refresh()
            wilderness()
            break

        print("                                Stats                                    ")
        print(f"Enemy name: {enemy1.name} // Run(r) Attack(a)")
        print(f"Enemy health: {enemy1.health} // Your health: {hero1.health}")
        print(
            f"Enemy inventory: {enemy1.inventory} // Your inventory: {hero1.inventory}")
        choice = input(">>> ")
        if choice == "r":
            if enemy1.stamina < hero1.stamina:
                print("You have escaped! ")
                hero1.stamina = hero1.stamina-enemy1.stamina
                wilderness()
                break
            else:
                print("You cannot escape !")
                player_options()
        elif choice == "a":
            roll = Dice.die(10)
            if roll == 1:
                print("Critical hit! ")
                enemy1.health = enemy1.health - hero1.level * 0.5
                player_options()
            elif roll == 3:
                print("Ineffective")
                hero1.health = hero1.health - (enemy1.health*1.5)
                print("Enemy critical hit!")
            elif roll == 2 or roll == 4 or roll == 5 or roll == 6:
                turn_damage = hero1.health*0.25
                print(f"You hit the enemy for {turn_damage} damage!")
                enemy1.health = enemy1.health - turn_damage
            else:
                enemydmg = enemy1.health*0.25
                print(f"{enemy1.name} has hit you for {enemydmg}")
                hero1.health = hero1.health - enemydmg


def shop():
    productions = {
        "Health Boost": hero1.health * 0.5,
        "Level Up": 1,
        "Stamina": 10
    }
    print(
        f"You have {hero1.inventory}, HP: {hero1.health}, LEVEL: {hero1.level}, STAMINA: {hero1.stamina}")
    print("""
    Health Boost(H): 10 coins
    Level Up(L): 50 coins
    Stamina(S): 10 coins
    Exit(E)""")
    player_shop = input(">>> ")
    if player_shop == "H":
        if hero1.inventory["Coins"] >= 10 and hero1.health < 200:
            hero1.health = hero1.health + productions["Health Boost"]
            hero1.inventory["Coins"] = hero1.inventory["Coins"] - 10
            print(f"You bought a Health Boost, your HP is now {hero1.health}")
            shop()
        elif hero1.inventory["Coins"] < 10 or hero1.health >= 200:
            print("Insuffisant funds or Hero at max health")
            shop()
    elif player_shop == "L":
        if hero1.inventory["Coins"] >= 50 and hero1.level < 20:
            hero1.level = hero1.level + productions["Level Up"]
            hero1.inventory["Coins"] = hero1.inventory["Coins"] - 50
            print(f"You bought a Level Up, you are now level {hero1.level} ")
            shop()
        elif hero1.inventory["Coins"] < 50 or hero1.level >= 20:
            print("Insuffisant funds or Hero at max level")
            shop()
    elif player_shop == "S":
        if hero1.inventory["Coins"] >= 10:
            hero1.stamina = hero1.stamina + productions["Stamina"]
            hero1.inventory["Coins"] = hero1.inventory["Coins"] - 10
            print(
                f"You bought Stamina, your stamina is now at {hero1.stamina}")
            shop()
        elif hero1.inventory["Coins"] < 10:
            print("Insuffisant funds!")
            shop()
    elif player_shop == "E":
        print("Exiting Shop! Goodbye adventurer.")
        time.sleep(2)
        cls()
        wilderness()
    else:
        print("This isn't a valid answer! ")
        shop()


def wilderness():
    time.sleep(2)
    cls()
    print("""
    What do you want to do?
    (D) to enter the dungeon
    (S) to enter the shop
    (E) to quit game
    (I) to print inventory""")
    wilderness_input = input(">>> ").upper()
    if wilderness_input == "D":
        print("Good luck dungeoneer . . .")
        time.sleep(2)
        cls()
        player_options()
    elif wilderness_input == "S":
        print("I hope you brought your mom's credit card.")
        time.sleep(2)
        cls()
        shop()
    elif wilderness_input == "E":
        print("Already?")
    elif wilderness_input == "I":
        print(f"You have {hero1.inventory}")
        wilderness()
    else:
        print("This isn't the demanded value.")
        wilderness()


start()
hero1 = Player()
enemy1 = random_enemies()
time.sleep(1)
cls()
player_options()
print("This got modified by me...")
