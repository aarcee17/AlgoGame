def conservative_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 5)
    highest_bid = max(bid for _, bid in previous_players)
    new_bid = highest_bid + 2 if highest_bid < 10 else 0  # Bids more if the highest is low
    return (True, new_bid) if new_bid > 0 else (False, 0)

def aggressive_predict(scoreboard, previous_players):
    initial_bid = 15
    if not previous_players:
        return (True, initial_bid)
    # Reduces bid if didn't win last round
    last_round_win = previous_players[-1][0] == 'PlayerName' and previous_players[-1][1] > 0
    return (True, initial_bid - 5) if not last_round_win else (True, initial_bid)
import random

def random_predict(scoreboard, previous_players):
    participate = random.choice([True, False])
    bid = random.randint(0, 10) if participate else 0
    return (participate, bid)

def tactical_predict(scoreboard, previous_players):
    if not previous_players:
        return (True, 10)
    average_bid = sum(bid for _, bid in previous_players) / len(previous_players)
    return (True, int(average_bid + 5)) if average_bid < 8 else (False, 0)

def make_incremental_predictor():
    bid = 5
    def incremental_predict(scoreboard, previous_players):
        nonlocal bid
        if bid >= 15:
            bid = 5  # Reset after reaching threshold
        else:
            bid += 2  # Increment bid
        return (True, bid)
    return incremental_predict
