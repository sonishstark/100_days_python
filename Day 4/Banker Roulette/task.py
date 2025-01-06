import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friends = random.uniform(0, 4)
winner = round(random_friends)
print(friends[winner])

print(random.choice(friends))