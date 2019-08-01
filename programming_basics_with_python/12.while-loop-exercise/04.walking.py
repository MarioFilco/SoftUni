target = 10000
all_steps = 0
while target >= all_steps:
    steps = input()
    if steps == "Going home":
        steps = input()
        all_steps += int(steps)
        break
    else:
        all_steps += int(steps)

if target <= all_steps:
    print(f"Goal reached! Good job!")
else:
    print(f"{target - all_steps} more steps to reach goal.")
