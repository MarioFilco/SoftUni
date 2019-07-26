vacation_days = int(input())

minutes_game = ((365 - vacation_days) * 63) + vacation_days * 127

diff = 30000 - minutes_game

if diff > 0:
    down_min = 30000 - minutes_game
    print(f"Tom sleeps well")
    print(f"{down_min // 60} hours and {down_min % 60} minutes less for play")
else:
    over_min = minutes_game - 30000
    print(f"Tom will run away")
    print(f"{over_min // 60} hours and {over_min % 60} minutes more for play")
