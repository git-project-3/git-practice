import random

def monty_hall_simulation(trials=100_000):
    stay_wins = 0
    switch_wins = 0

    #for문 (hhs)
    for _ in range(trials):
        # Place car behind one of three doors
        car = random.randrange(3)
        # Player picks a random door
        choice = random.randrange(3)

        # Host opens a goat door (not player's choice, not the car)
        possible_host_doors = [d for d in range(3) if d != choice and d != car]
        host_open = random.choice(possible_host_doors)

        # Switching means taking the remaining unopened door
        remaining_doors = [d for d in range(3) if d != choice and d != host_open]
        switched_choice = remaining_doors[0]

        # Count wins
        if choice == car:
            stay_wins += 1
        if switched_choice == car:
            switch_wins += 1
    return stay_wins, switch_wins
  
if __name__ == "__main__":
    stay, switch = monty_hall_simulation(100_000)
    print(f"유지 성공 횟수: {stay}")
    print(f"변경 성공 횟수: {switch}")
