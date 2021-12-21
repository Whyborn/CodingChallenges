from get_input import get_data, split_on_lines
import numpy as np
import collections as coll

year, day = 2021, 21

data = split_on_lines(get_data(year, day))

_, player1 = data[0].split(": ")
_, player2 = data[1].split(": ")
player1_pos = int(player1)
player2_pos = int(player2)

roll_count = 0

# Part 1
class Dice:
    def __init__(self, val):
        self.val = val

    def roll(self):
        return_val = self.val
        self.val = 1 if self.val == 100 else self.val + 1
        return return_val
        

def Part1(player1_pos, player2_pos, dice):
    player1_score = 0; player2_score = 0
    roll_count = 0

    while True:
    #for _ in range(4):
        # Calculate player 1
        player1_pos += dice.roll() + dice.roll() + dice.roll()

        player1_pos = (player1_pos - 1) % 10 + 1

        player1_score += player1_pos
        roll_count += 3
        if player1_score >= 1000:
            return player2_score * roll_count
            
        # Calculate player 2
        player2_pos += dice.roll() + dice.roll() + dice.roll()

        player2_pos = (player2_pos - 1) % 10 + 1

        player2_score += player2_pos
        roll_count += 3
        if player2_score >= 1000:
            return player1_score * roll_count

#print(Part1(player1_pos, player2_pos, Dice(1)))

# Part 2

# This list tells us how many times each possible total occurs
dice_combinations = list(coll.Counter(i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)).items())

# Create a dictionary that will store the possible states and increment them
# The state consists of (player1_score, player1_pos, player2_score, player2_pos)

states = {(0, player1_pos, 0, player2_pos): 1}
p1_wins, p2_wins = 0, 0

# The loop is set up so that if a player wins, the dictionary is empty
while states:
    new_dict = coll.defaultdict(int)
    for state, state_count in states.items():
        # Unpack the values from state
        player1_score, player1_pos, player2_score, player2_pos = state

        # Now iterate through the possible outcomes for the turn
        # Make sure to duplicate the values for score and position so they don't override
        for dice_roll_p1, count_p1 in dice_combinations:
            player1_pos_ = (player1_pos + dice_roll_p1 - 1) % 10 + 1
            player1_score_ = player1_score + player1_pos_
            if player1_score_ >= 21:
                # Player 1 wins, increment his win count by the number of times this particular dice rolls occurs
                # times the number of times this particular state exists
                p1_wins += state_count * count_p1

                # And continue to end
                continue

            for dice_roll_p2, count_p2 in dice_combinations:
                player2_pos_ = (player2_pos + dice_roll_p2 - 1) % 10 + 1
                player2_score_ = player2_score + player2_pos_
                
                if player2_score_ >= 21:
                    # Player 1 wins, increment his win count by the number of times this particular dice rolls occurs
                    # times the number of times this particular state exists (with consideration of player 1 roll)
                    p2_wins += state_count * count_p1 * count_p2
                    continue

                # Now record the final state and how many times it occurs at the end of the complete turn
                new_dict[(player1_score_, player1_pos_, player2_score_, player2_pos_)] += state_count * count_p1 * count_p2

    # new_dict is empty either player wins- so if a player has won in all states, new_dict is empty and states == False
    states = new_dict

print(max(p1_wins, p2_wins))
