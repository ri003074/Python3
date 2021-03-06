import pandas

input_file = "csv_type1_1.csv"
# df  = pd.read_excel('sampleLog.xlsx',index_col=[0])
df = pandas.read_csv(input_file, index_col=[0])
ax = df.plot(
    figsize=(10, 10),
    title="sample graph",
    legend=True,
    ylim=[0, 10],
    yticks=range(0, 12, 2),
)
ax.set_ylabel("mV")
ax.set_xlabel("mV")
fig = ax.get_figure()
fig.savefig("img.png")
