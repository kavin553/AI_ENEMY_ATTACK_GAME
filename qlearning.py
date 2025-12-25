import random
import pickle
actions = ["CHASE", "ATTACK", "RUN"]
q_table = {}

def get_state(enemy, player):
    dx = abs(enemy.x - player.x)
    dy = abs(enemy.y - player.y)
    return (dx // 100, dy // 100)  # simplified state

def choose_action(state):
    if random.random() < 0.2:  # exploration
        return random.choice(actions)

    q_values = [q_table.get((state, a), 0) for a in actions]
    return actions[q_values.index(max(q_values))]

def update_q(state, action, reward, next_state):
    old_value = q_table.get((state, action), 0)
    q_table[(state, action)] = old_value + 0.1 * reward
def save_q():
    with open("qtable.pkl","wb") as f:
        pickle.dump(q_table,f)
def load_q():
    global q_table
    try:
        with open("qtable.pkl","rb") as f:
            q_table=pickle.load(f)
    except:
        q_table={}        
