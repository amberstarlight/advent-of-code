# Day 2: Rock Paper Scissors

from pathlib import Path

input = Path("input.txt").read_text()
round_list = list(filter(None, input.split("\n")))  # filter out newlines

opponent_moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

player_moves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

move_score_table = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

player_score_table = {
    "win": 6,
    "draw": 3,
    "lose": 0,
}

player_should = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}


# The core combat triangle of Rock, Paper, Scissors
def rock_paper_scissors(player_action, opponent_action):
    if player_action == opponent_action:
        return "draw"

    if player_action == "rock":
        if opponent_action == "paper":
            return "lose"
        return "win"

    if player_action == "paper":
        if opponent_action == "scissors":
            return "lose"
        return "win"

    if player_action == "scissors":
        if opponent_action == "rock":
            return "lose"
        return "win"


# Part 2: to work out what action the player should take
def pick_player_action(opponent_action, player_should):
    if player_should == "draw":
        return opponent_action

    if opponent_action == "rock":
        if player_should == "lose":
            return "scissors"
        return "paper"

    elif opponent_action == "paper":
        if player_should == "lose":
            return "rock"
        return "scissors"

    else:
        if player_should == "lose":
            return "paper"
        return "rock"


player_score = 0

for game in round_list:
    game_score = 0
    opponent_action = opponent_moves[game[0]]
    player_action = player_moves[game[2]]
    game_outcome = rock_paper_scissors(player_action, opponent_action)
    game_score = player_score_table[game_outcome] + move_score_table[player_action]
    player_score += game_score

print(player_score)

player_score_round_2 = 0

for game in round_list:
    game_score = 0
    opponent_action = opponent_moves[game[0]]
    player_action = pick_player_action(opponent_action, player_should[game[2]])
    game_outcome = player_should[game[2]]
    game_score = player_score_table[game_outcome] + move_score_table[player_action]
    player_score_round_2 += game_score

print(player_score_round_2)
