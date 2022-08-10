# Write your code here.

def get_number_of_teams():
    while True:
        try:
            num_of_teams = int(input("Enter the number of teams in the tournament: "))
            if num_of_teams <= 1:
                print("The minimum number of teams is 2, try again.")
            else:
                break
        except:
            print("Number not valid, try again.")
    return num_of_teams


def get_team_names(num_teams):
    team_names = []
    for i in range(num_teams):
        while True:
            name = input(f"Enter the name for team #{i + 1}: ")
            if len(name) < 2:
                print("Team names must have at least 2 characters, try again.")
            elif len(name.split()) > 2:
                print("Team names may have at most 2 words, try again.")
            else:
                team_names.append(name)
                break
    return team_names


def get_number_of_games_played(num_teams):
    while True:
        try:
            games_played = int(input("Enter the number of games played by each team: "))
            if games_played < num_teams - 1:
                print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            else:
                return games_played
        except:
            print("Invalid Number, try again")


def get_team_wins(team_names, games_played):
    plays = []
    for team_name in team_names:
        while True:
            num_wins = int(input(f"Enter the number of wins Team {team_name} had: "))
            if num_wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
            elif num_wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                plays.append([team_name, num_wins])
                break
    plays = sorted(plays, key=lambda x: x[1])
    print("Generating the games to be played in the first round of the tournament...")
    for i in range(num_teams// 2):
        print(f"Home: {plays[i][0]} VS Away: {plays[len(plays) - i  - 1][0]}")

# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)
