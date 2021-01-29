import builtins

builtins.print()

ranking = {
    "A": 100,
    "B": 85,
    "C": 95,
}

print(ranking.get("A"))


print(sorted(ranking))
print(sorted(ranking, key=ranking.get))
print(sorted(ranking, key=ranking.get, reverse=True))
