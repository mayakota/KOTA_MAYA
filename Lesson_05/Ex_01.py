import random
player = random.randint(1, 6)
computer = random.randint(1, 6)

print("Your rolled a", player)
print("Computer rolled a", computer)

if player > computer:
    print("Winner is you")

if player < computer:
    print("Winner is computer")
