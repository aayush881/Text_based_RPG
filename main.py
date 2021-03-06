from classes.game import bcolors, Person
from classes.magic import spell
from classes.inventory import Item
import random
import sys

# Create black magic
fire = spell("Mocktail", 20, 300, "black")
thunder = spell("Grenade", 25, 350, "black")
blizzard = spell("Blizzard", 30, 520, "black")
meteor = spell("Meteor", 40, 560, "black")
quake = spell("Quake2", 14, 110, "black")

# Create white magic
cure = spell("Bandage", 25, 100, "white")
cura = spell("First Aid", 32, 750, "white")
curaga = spell("Health-Kit", 50, 1250, "white")

# Create some items
potion = Item("Energy drink", "potion", "Heals 250 HP", 250)
superpotion = Item("Adrenaline", "potion", "Heals 850 HP", 850)
elixer = Item("Elixer", "elixer", "Fully restores HP and MP of one party member.", 9999)
hielixer = Item("Mega elixer", "elixer", "Fully restores party's HP.", 9999)
grenade = Item("Missile", "attack", "Deals upto 1500 of splash damage.", 1500)

# Create spells
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
enemy_spells = [fire, meteor, curaga]
player_items = [{"item": potion, "quantity": random.randrange(1, 5)},
                {"item": superpotion, "quantity": random.randrange(0, 3)},
                {"item": elixer, "quantity": random.randrange(0, 3)},
                {"item": hielixer, "quantity": random.randrange(0, 2)},
                {"item": grenade, "quantity": random.randrange(1, 3)}]

# The beginning of execution of the game
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD +
      "!!! A Text Based Role Play Game !!!" + bcolors.ENDC)
user = input(bcolors.OKGREEN + "Enter your name: " + bcolors.ENDC)
user = user[:14] if len(user) > 13 else user
print(bcolors.BOLD + "Hello " + str(user) +
      " Welcome to my text based Role play game. Hope you enjoy it." + bcolors.ENDC)
while True:
    instructions = input("Press I to get instructions and P to play: ")
    if instructions.upper() == "I":
        print("\n\nThis is a very firece war game. You can have upto 4 squad members to support you. When you die, the game is over.\nAll the players get chance to attack enemies first and then all the enemies will attack the players.\nYou can use"+bcolors.FAIL + " ATTACK"+bcolors.ENDC+bcolors.OKBLUE+" MAGIC"+bcolors.ENDC+" and"+bcolors.OKGREEN + " ITEMS"+bcolors.ENDC +
              "\nEach players have their own hitpoints, defensive abilities and magic points.\nThe items are shared by all the group members.\n\n"+bcolors.BOLD+bcolors.OKBLUE+"Use your war strategies\n"+bcolors.ENDC+bcolors.BOLD+bcolors.FAIL+"Defeat all enemies !!!" + bcolors.ENDC+"\nChoose your options using the numbers as per listed." + bcolors.BOLD+bcolors.OKGREEN + "\nEnjoy !!!" + bcolors.ENDC + "\nEnter Q anytime to quit.")
        hold = input("Press Enter to continue: ")
        break
    elif instructions.upper() == "P":
        break
while True:
    player_squad = input(
        "Choose the number of players in your squad(1 to 4): ")
    if player_squad.upper() == "Q":
        print(bcolors.FAIL + bcolors.BOLD +
              "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
        sys.exit(0)
    if player_squad.isdigit() and (int(player_squad) >= 1 and int(player_squad) <= 4):
        break

# Instantiate people  (name,health,magic,attack,defense)
player1 = Person(user, 1250, 120, 288, 150, player_spells, player_items)
player2 = Person("Player1", 1250, 120, 288, 150, player_spells, player_items)
player3 = Person("Player2", 1250, 120, 288, 150, player_spells, player_items)
player4 = Person("Player3", 1250, 120, 288, 150, player_spells, player_items)

# Instantiate enemies
general1 = Person("General1",  1250, 120, 288, 150, enemy_spells, [])
general2 = Person("General2",  1250, 120, 288, 150, enemy_spells, [])
general3 = Person("General3",  1250, 120, 288, 150, enemy_spells, [])
general4 = Person("General4",  1250, 120, 288, 150, enemy_spells, [])

monster1 = Person("Monster1", 2400, 207, 285, 125, enemy_spells, [])
monster2 = Person("Monster2", 2400, 207, 285, 125, enemy_spells, [])
monster3 = Person("Monster3", 2500, 207, 285, 125, enemy_spells, [])
monster4 = Person("Monster4", 2500, 207, 285, 125, enemy_spells, [])


players = [player1, player2, player3, player4]
enemies1 = [general1, general2, general3, general4]
enemies2 = [monster1, monster2, monster3, monster4]
enemies = [monster1]

for number in range((4 - int(player_squad))):  # Managing players list as per input
    players.pop(-1)

for number in range((int(player_squad)-1)//2):  # Use of strong enemies
    enemies.append(enemies2[number + 1])

for number in range(len(players)-1):  # Use of basic enemies
    enemies.append(enemies1[number])

while running:  # Program attack loop begins
    print("="*80)

    print("\n")
    print("NAME\t\t\t\tHP\t\t\t\tMP")
    for player in players:
        player.get_stats()  # Display the HP and MP bars of players
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()  # Display the HP of enemies

    for player in players:
        player.choose_action()  # Choice among Attack, Magic and Items
        try:
            while True:
                index = input("\tChoose your action: ")
                if index.upper() == "Q":
                    print(bcolors.FAIL + bcolors.BOLD +
                          "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                    sys.exit(0)
                index = int(index) - 1
                if index >= 0 and index <= 2:
                    break
                else:
                    print(bcolors.BOLD + bcolors.FAIL +
                          "\tThere's no option such as " + str(index + 1) + bcolors.ENDC)
        except ValueError:
            print(
                bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
            continue

        if index == 0:  # Player chose attack
            dmg = player.generate_damage()
            player.choose_target(enemies)
            try:
                while True:
                    enemy = input("\t\tYour choice: ")
                    if enemy.upper() == "Q":
                        print(bcolors.FAIL + bcolors.BOLD +
                              "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)
                    enemy = int(enemy) - 1
                    if enemy >= 0 and enemy < len(enemies):
                        break
                    else:
                        print(bcolors.BOLD + bcolors.FAIL +
                              "\tThere's no enemy such as " + str(enemy + 1) + bcolors.ENDC)
            except ValueError:
                print(
                    bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
                continue
            defence = enemies[enemy].defence()
            enemies[enemy].take_damage(dmg - defence)
            print("You attacked " +
                  enemies[enemy].name.replace(" ", "")+" for", dmg - defence, "points.")

            if enemies[enemy].get_hp() == 0:  # The enemy died
                print(
                    bcolors.OKGREEN + enemies[enemy].name.replace(" ", "") + " has died !!" + bcolors.ENDC)
                del enemies[enemy]
                if len(enemies) == 0:  # all enemies died
                    print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                    sys.exit(0)

        elif index == 1:  # Player chose Magic
            player.choose_magic()  # Lists of magics along with cost is displayed
            try:
                while True:
                    magic_choice = input("\tChoose a magic: ")
                    if magic_choice.upper() == "Q":
                        print(bcolors.FAIL + bcolors.BOLD +
                              "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)
                    magic_choice = int(magic_choice) - 1
                    if magic_choice >= 0 and magic_choice <= 6:
                        spell = player.magic[magic_choice]
                        magic_dmg = spell.generate_damage()
                        if spell.cost <= player.get_mp():
                            break
                        else:
                            print(bcolors.FAIL + bcolors.BOLD +
                                  "Not enough MP !!" + bcolors.ENDC)
                    else:
                        print(bcolors.BOLD + bcolors.FAIL + "\tThere's no option such as " +
                              str(magic_choice + 1) + bcolors.ENDC)
            except ValueError:
                print(
                    bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
                continue

            # Magic Points deduction of the player as per cost
            player.reduce_mp(spell.cost)

            if spell.type == 'white':  # White magic heals the player
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name +
                      " heals for ", str(magic_dmg), "HP" + bcolors.ENDC)

            elif spell.type == "black":  # Black magic attacks the enemy
                player.choose_target(enemies)
                try:
                    while True:
                        enemy = input("\t\tYour choice: ")
                        if enemy.upper() == "Q":
                            print(bcolors.FAIL + bcolors.BOLD +
                                  "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                            sys.exit(0)
                        enemy = int(enemy) - 1
                        if enemy >= 0 and enemy < len(enemies):
                            break
                        else:
                            print(bcolors.BOLD + bcolors.FAIL +
                                  "\tThere's no enemy such as " + str(enemy + 1) + bcolors.ENDC)
                except ValueError:
                    print(
                        bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
                    continue

                defence = enemies[enemy].defence()
                enemies[enemy].take_damage(magic_dmg-defence)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg - defence),
                      "points of damage to "+enemies[enemy].name.replace(" ", "") + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:  # Enemy dies
                    print(
                        bcolors.OKGREEN + enemies[enemy].name.replace(" ", "") + " has died !!" + bcolors.ENDC)
                    del enemies[enemy]
                    if len(enemies) == 0:  # All enemies die
                        print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                        sys.exit(0)

        elif index == 2:  # Player chooses Items
            player.choose_items()
            try:
                while True:
                    item_choice = input("\tChoose an item: ")
                    if item_choice.upper() == "Q":
                        print(bcolors.FAIL + bcolors.BOLD +
                              "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                        sys.exit(0)
                    item_choice = int(item_choice) - 1
                    if item_choice >= 0 and item_choice <=4:
                        if player.items[item_choice]["quantity"] > 0:
                            item = player.items[item_choice]["item"]
                            player.items[item_choice]["quantity"] -= 1
                            break
                        else:
                            print("\n"+bcolors.FAIL + "\tNo " +
                                  item.name + " remaining." + bcolors.ENDC)
                    else:
                        print(bcolors.BOLD + bcolors.FAIL + "\tThere's no option such as " +
                              str(item_choice + 1) + bcolors.ENDC)
            except ValueError:
                print(
                    bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
                continue

            if item.type == "potion":  # Potions heal the player/s
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name +
                      " heals for ", str(item.prop), "HP" + bcolors.ENDC)

            elif item.type == "elixer":  # Heals the player using it and gives max MP

                if item.name == "Mega elixer":  # Heals every alive player in squad and gives max MP
                    for i in players:
                        i.hp = i.maxhp
                        print(bcolors.OKGREEN + "\n" + item.name +
                        " fully restores HP." + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name +
                      " fully restores HP/MP." + bcolors.ENDC)

            elif item.type == "attack":  # Attacks the enemies
                player.choose_target(enemies)

                try:
                    while True:
                        enemy = input("\t\tYour choice: ")
                        if enemy.upper() == "Q":
                            print(bcolors.FAIL + bcolors.BOLD +
                                  "\nYou forfeited. LOSER !!!" + bcolors.ENDC)
                            sys.exit(0)
                        enemy = int(enemy) - 1
                        if enemy >= 0 and enemy < len(enemies):
                            break
                        else:
                            print(bcolors.BOLD + bcolors.FAIL +
                                  "\tThere's no enemy such as " + str(enemy + 1) + bcolors.ENDC)
                except ValueError:
                    print(
                        bcolors.FAIL + "You needed to choose a number. Chance missed !!" + bcolors.ENDC)
                    continue

                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deals ", str(item.prop),
                      " points of damage to " + enemies[enemy].name + bcolors.ENDC)
                

                # The enemies above or below the main target are also affected by the grenade.
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN +
                          enemies[enemy].name + " has died !!" + bcolors.ENDC)
                    del enemies[enemy]
                
                if len(enemies) == 0:
                    print(bcolors.OKGREEN + "You Win!!" + bcolors.ENDC)
                    sys.exit(0)

    
    print("\n")
    for enemy in enemies:  # Enemies attack sequence begins
        a = True
        while a:
            # No Items for enemies. 0 = Attack, 1 = Magic
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:  # Enemy attacks
                # Enemy chooses a target
                target = random.randrange(0, len(players))
                enemy_dmg = enemy.generate_damage()

                defence = players[target].defence()
                players[target].take_damage(enemy_dmg - defence)
                if players[target].name == user:
                    name = "You"
                else:
                    name = players[target].name
                print(enemy.name.replace(" ", "") + " attacked " +
                      name + " for", enemy_dmg - defence)
                a = False
                if players[target].get_hp() == 0:
                    if players[target].name == user:
                        name = "You"
                    else:
                        name = players[target].name
                    print(bcolors.FAIL + name + " died !!" + bcolors.ENDC)
                    del players[target]
                    if len(players)==0:  # If the all your team members die, GAME is OVER
                        print(bcolors.FAIL + bcolors.BOLD +
                              "You Lose!!!\n You have been defeated by your enemies!!!" + bcolors.ENDC)
                        sys.exit(0)

            elif enemy_choice == 1:  # Enemy uses magic
                spell, magic_dmg = enemy.choose_enemy_spell()  # Enemy chooses the spell
                if spell == "":
                    continue
                else:
                    enemy.reduce_mp(spell.cost)

                    if spell.type == 'white':  # Enemy heals itself with white spell
                        enemy.heal(magic_dmg)
                        print(bcolors.OKBLUE + spell.name + " heals "+enemy.name.replace(
                            " ", "")+" for ", str(magic_dmg), "HP" + bcolors.ENDC)

                    elif spell.type == "black":  # Enemy attacks with black spell
                        target = random.randrange(
                            0, len(players))  # Enemy chooses target
                        defence = players[target].defence()
                        players[target].take_damage(magic_dmg - defence)
                        if players[target].name == user:
                            name = "You"
                        else:
                            name = players[target].name
                        print(bcolors.OKBLUE + enemy.name.replace(' ', '') + "'s "+spell.name +
                              " deals", str(magic_dmg - defence), "points of damage to "+name + bcolors.ENDC)

                        if players[target].get_hp() == 0:
                            print(bcolors.FAIL + name +
                                  " died !!" + bcolors.ENDC)
                            del players[target]
                            if len(players)==0:
                                print(bcolors.FAIL + bcolors.BOLD +
                                      "You Lose!!!\n You have been defeated by your enemies!!!" + bcolors.ENDC)
                                sys.exit(0)
                    a = False
