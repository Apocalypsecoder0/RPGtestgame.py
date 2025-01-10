import json
import os
import random

class Player:
    def __init__(self, name, level=1, exp=0, gold=0, weapons=[], armor=[], quests=[]):
        self.name = name
        self.level = level
        self.exp = exp
        self.gold = gold
        self.weapons = weapons
        self.armor = armor
        self.quests = quests

    def __str__(self):
        return f"Name: {self.name}\nLevel: {self.level}\nExp: {self.exp}\nGold: {self.gold}\nWeapons: {self.weapons}\nArmor: {self.armor}\nQuests: {self.quests}"

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= self.level * 100:
            self.level += 1
            self.exp = 0
            print(f"{self.name} has leveled up to level {self.level}!")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        print(f"{self.name} has acquired a new weapon: {weapon['name']}")

    def add_armor(self, armor):
        self.armor.append(armor)
        print(f"{self.name} has acquired new armor: {armor['name']}")

    def add_quest(self, quest):
        self.quests.append(quest)
        print(f"{self.name} has accepted a new quest: {quest['name']}")

class World:
    def __init__(self):
        self.monsters = []
        self.weapons = []
        self.armor = []
        self.quests = []
        self.main_story_quests = []
        self.side_quests = []

    def add_monster(self, monster):
        self.monsters.append(monster)

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_armor(self, armor):
        self.armor.append(armor)

    def add_quest(self, quest):
        self.quests.append(quest)
        if quest['type'] == 'main':
            self.main_story_quests.append(quest)
        else:
            self.side_quests.append(quest)

def create_new_game():
    name = input("Enter your character's name: ")
    player = Player(name)
    print("Welcome, adventurer! Your journey begins now!")
    save_game(player)
    return player

def load_game():
    while True:
        file_name = input("Enter the name of the save file to load: ")
        if os.path.exists(file_name + ".json"):
            with open(file_name + ".json", "r") as f:
                player_data = json.load(f)
            player = Player(player_data['name'], player_data['level'], player_data['exp'], player_data['gold'], player_data['weapons'], player_data['armor'], player_data['quests'])
            print(f"Game loaded successfully. Welcome back, {player.name}!")
            return player
        else:
            print("Invalid save file name. Please try again.")

def save_game(player):
    while True:
        file_name = input("Enter the name of the save file: ")
        if file_name:
            with open(file_name + ".json", "w") as f:
                json.dump(player.__dict__, f)
            print("Game saved successfully.")
            break
        else:
            print("Invalid save file name. Please try again.")

def display_menu():
    print("\n--- RPG Game ---")
    print("1. New Game")
    print("2. Continue Game")
    print("3. Load Game")
    print("4. Settings")
    print("5. Exit")

def main():
    world = World()
    # Initialize the world with monsters, weapons, armor, and quests
    # ... (Add monster, weapon, armor, and quest creation logic here)
    # Initialize the world with monsters, weapons, armor, and quests
    world.add_monster({'name': 'Goblin', 'level': 1, 'exp': 10, 'gold': 5, 'attack': 5, 'defense': 2})
    world.add_monster({'name': 'Orc', 'level': 3, 'exp': 30, 'gold': 15, 'attack': 10, 'defense': 5})
    world.add_monster({'name': 'Dragon', 'level': 10, 'exp': 100, 'gold': 100, 'attack': 20, 'defense': 10})

    world.add_weapon({'name': 'Wooden Sword', 'attack': 2})
    world.add_weapon({'name': 'Iron Sword', 'attack': 5})
    world.add_weapon({'name': 'Dragon Slayer', 'attack': 15})

    world.add_armor({'name': 'Leather Armor', 'defense': 2})
    world.add_armor({'name': 'Chainmail', 'defense': 5})
    world.add_armor({'name': 'Plate Armor', 'defense': 10})

    world.add_quest({'name': 'Slay the Goblin', 'type': 'main', 'description': 'Defeat the Goblin in the forest.', 'reward': {'exp': 20, 'gold': 10}})
    world.add_quest({'name': 'Rescue the Princess', 'type': 'main', 'description': 'Rescue the princess from the Orc stronghold.', 'reward': {'exp': 50, 'gold': 50}})
    world.add_quest({'name': 'Find the Dragon Slayer', 'type': 'side', 'description': 'Find the legendary Dragon Slayer weapon.', 'reward': {'weapon': {'name': 'Dragon Slayer', 'attack': 15}}})


    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            player = create_new_game()
            # ... (Add game loop logic here)
            while True:
                print("\n--- Actions ---")
                print("1. Explore")
                print("2. Inventory")
                print("3. Quests")
                print("4. Save Game")
                print("5. Exit")

                action_choice = input("Enter your action: ")

                if action_choice == "1":
                    # ... (Add explore logic here)
                elif action_choice == "1":
                    print("\n--- Exploration ---")
                    print("1. Forest")
                    print("2. Cave")
                    print("3. Mountain")
                    print("4. Town")
                    print("5. Back to Actions")

                    explore_choice = input("Where would you like to explore? ")

                    if explore_choice == "1":
                        # ... (Add Forest exploration logic here)
                        print("You are now in the Forest.")
                        encounter = random.choice([True, False])
                        if encounter:
                            monster = random.choice(world.monsters)
                            print(f"You encounter a {monster['name']}!")
                            # ... (Add combat logic here)
                        else:
                            print("You find a chest with some treasure!")
                            # ... (Add treasure logic here)
                    elif explore_choice == "2":
                        # ... (Add Cave exploration logic here)
                        print("You are now in the Cave.")
                        encounter = random.choice([True, False])
                        if encounter:
                            monster = random.choice(world.monsters)
                            print(f"You encounter a {monster['name']}!")
                            # ... def combat(player, monster):
    print(f"A wild {monster['name']} appears!")
    while monster['level'] > 0 and player.level > 0:
        action = input("Do you wish to (1) attack or (2) flee? ")
        if action == "1":
            damage = max(0, player.level + random.randint(1, 5) - monster['defense'])
            monster['level'] -= damage
            print(f"You attack {monster['name']} for {damage} damage!")
            if monster['level'] <= 0:
                print(f"You have defeated the {monster['name']}!")
                player.gain_exp(monster['exp'])
                player.gold += monster['gold']
                break
            # Monster attacks back
            monster_damage = max(0, monster['attack'] - player.level)
            player.level -= monster_damage
            print(f"{monster['name']} attacks you for {monster_damage} damage!")
            if player.level <= 0:
                print(f"You have been defeated by the {monster['name']}. Game Over.")
                break
        elif action == "2":
            print(f"You flee from the {monster['name']}.")
            break
        else:
            print("Invalid action. Choose 1 to attack or 2 to flee.")(Add combat logic here)
                        else:
                            print("You find a chest with some treasure!")
                            # ... (Add treasure logic here)
                    elif explore_choice == "3":
                        # ... (Add Mountain exploration logic here)
                        print("You are now in the Mountain.")
                        encounter = random.choice([True, False])
                        if encounter:
                            monster = random.choice(world.monsters)
                            print(f"You encounter a {monster['name']}!")
                            # ... (Add combat logic here)
                        else:
                            print("You find a chest with some treasure!")
                            # ... (Add treasure logic here)
                    elif explore_choice == "4":
                        # ...def explore(player, world):
    location = input("Where would you like to explore? (Forest/Cave/Mountain/Town): ")
    if location.lower() == "forest":
        print("You venture into the forest.")
        encounter = random.choice([True, False])
        if encounter:
            monster = random.choice(world.monsters)
            combat(player, monster)
        else:
            print("You find a hidden chest!")
            # Add treasure logic here
    elif location.lower() == "town":
        print("You arrive at a bustling town.")
        # Add town logic here (e.g., shop, tavern, NPCs)
    else:
        print("That location is not available yet.") (Add Town exploration logic here)
                        print("You are now in the Town.")
                        # ... (Add town interactions logic here)
                    elif explore_choice == "5":
                        print("Returning to Actions.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
                elif action_choice == "2":
                    # ... (def show_inventory(player):
    print("\n--- Inventory ---")
    print("Weapons:")
    for weapon in player.weapons:
        print(f"- {weapon['name']}")
    print("Armor:")
    for armor in player.armor:
        print(f"- {armor['name']}")
    print(f"Gold: {player.gold}")Add inventory logic here)
                elif action_choice == "3":
                    # ... def start_quest(player, quest):
    print(f"Quest: {quest['name']}\nDescription: {quest['description']}")
    if quest['type'] == 'main':
        print("This is a main storyline quest!")
    elif quest['type'] == 'side':
        print("This is a side quest!")
    action = input("Do you wish to accept this quest? (y/n): ")
    if action.lower() == 'y':
        player.add_quest(quest)
        print(f"Quest accepted: {quest['name']}")
    else:
        print("You decided not to take the quest.")(Add quests logic here)
                elif action_choice == "4":
                    save_game(player)
                elif action_choice == "5":
                    print("Returning to main menu.")
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            player = load_game()
            # ... (Add game loop logic here)
        elif choice == "3":
            player = load_game()
            # ... (Add game loop logic here)
        elif choice == "4":
            # ... (Add settings logic here)
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
