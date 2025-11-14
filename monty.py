if __name__ == "__main__":
    stay, switch = monty_hall_simulation(100_000)
    print(f"유지 성공 횟수: {stay}")
    print(f"변경 성공 횟수: {switch}")
