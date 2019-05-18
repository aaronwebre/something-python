player_names = []

should_add_player = input("Would you like to add a player to the list (Yes/No) ")
while should_add_player.lower() == "yes":
    new_player = input("\nEnter the name of the player to add to the team: ")
    player_names.append(new_player)
    should_add_player = input("\nWould you like to add another player? (Yes/No) ")

print("\nThere are {} players on the team. ".format(len(player_names)))
    
player_number = 1
for player in player_names:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

keeper = input("Please select the goal keeper by selecting the player number. (1-{}) ".format(len(player_names)))

keeper = int(keeper)

print("The goal keeper in the game will be: {}".format(player_names[keeper -1]))
