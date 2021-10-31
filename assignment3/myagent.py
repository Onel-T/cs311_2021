# Hold grudge for 3 iterations and add on grudges when they confess
# Confess by default
# Stay silent 2 times only (not guaranteed) when they stay silent but also pop 2 grudges if available
# limit stack size to 5 
# last 5 moves
# want to confess but if there is a consistent silence then agent will become silent 

import argparse
import json
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    
    args = parser.parse_args()

data = {}
opponent_move = args.last_opponent_move
new_game = args.init
agent_moves = []

# Open json
with open("program_data.json", "r") as data_file:
   data = json.load(data_file)

# New game settings (reset json)
if new_game == "true":
    data["iterations"] = int(args.iterations)
    data["iterations_counter"] = 0
    data["agent"] = []

# Retrieve the json data
agent_moves = data["agent"]
iterations_counter = data["iterations_counter"]
game_iterations = data["iterations"]

# if stack not empty
if agent_moves:
    # Last 5 moves are confess
    if iterations_counter >= game_iterations - 5:
            # checking if next item is not confess
        if agent_moves[len(agent_moves) - 1] != "confess":
            agent_moves.pop()
            agent_moves.append("confess")
    # Grudge for opponent confessing (use 3 confess on stack)        
    elif opponent_move != "silent":
        for i in range(3):
            if len(agent_moves) == 5:
                agent_moves.pop(0)
                agent_moves.append("confess")
            else:
                agent_moves.append("confess")
    # if opponent stays silent
    elif opponent_move == "silent":
        # create unpredictable reaction
        if random.randint(0, 2) == 2:
            pass            
        else:
            for i in range(2):
                if len(agent_moves) == 5:
                    if agent_moves[len(agent_moves) - 1] == "confess":
                        agent_moves.pop()
                    else:
                        agent_moves.pop(0)
                agent_moves.append("silent")
            
    print(agent_moves.pop())

# stack is empty
else:
    # last 5 moves check
    if iterations_counter >= game_iterations - 5:
            agent_moves.append("confess")
    else:
        if opponent_move == "confess":
            # adding in 2 confess on empty stack
            for i in range(2):
                agent_moves.append("confess")
        elif opponent_move == "silent":
            agent_moves.append("silent")
        else:
            agent_moves.append("confess")
    print(agent_moves.pop())

# Update json values
data["agent"] = agent_moves
data["iterations_counter"] += 1

# Write and close json
with open("program_data.json", "w") as data_file:
    json.dump(data, data_file)
    data_file.close()
#print(data)
    

