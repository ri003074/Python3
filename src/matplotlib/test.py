import matplotlib.pyplot as plt
import pandas as pd


data = [
    {"p1": 1, "pin": "P1857"},
    {"p1": 2, "pin": "P1858"},
]

for i in range(100):
    fig = plt.figure(figsize=(8, 3))
    ax = fig.add_subplot(1, 1, 1)

    data[0]["p1"] = i
    data[1]["p1"] = i + 1
    df = pd.DataFrame(data)
    df = df.set_index("pin")

    print(i)
    df.plot(ax=ax)
    plt.savefig("a" + str(i) + ".png")
    plt.close("all")
