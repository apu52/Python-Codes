def create_cricket_dictionary(n):
    cricket_dict = {}
    for _ in range(n):
        player_name = input("Enter player's name: ")
        runs_scored = int(input("Enter runs scored by {}: ".format(player_name)))
        cricket_dict[player_name] = runs_scored
    return cricket_dict

num_players = int(input("Enter the number of players: "))

# Create the 'cricket' dictionary with player details
cricket_dict = create_cricket_dictionary(num_players)

player_to_search = input("Enter player's name to get runs scored: ")

# Print runs scored or -1 if player not found
runs_scored = cricket_dict.get(player_to_search, -1)
print("Runs scored by {}: {}".format(player_to_search, runs_scored))
