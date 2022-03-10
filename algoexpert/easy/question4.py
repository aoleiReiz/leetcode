
def tournamentWinner(competitions, results):
    current_best_team = ""
    team_score = {}
    for i, competition in enumerate(competitions):
        home_team, away_team = competition
        winning_team = home_team if results[i] == 1 else away_team
        team_score[winning_team] = team_score.get(winning_team, 0) + 3
        if team_score[winning_team] > team_score.get(current_best_team, 0):
            current_best_team = winning_team

    return current_best_team