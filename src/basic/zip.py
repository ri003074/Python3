day1 = ["ab", "cd", "ef"]
day2 = ["aab", "acd", "aef"]
day3 = ["bab", "bcd", "bef"]

for day, fruit, drink in zip(day1, day2, day3):
    print(day, fruit, drink)
