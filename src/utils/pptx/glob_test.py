from glob import glob

files = glob("./**/*.PNG", recursive=True)
print(files)

for i in range(0, 10, 2):
    print(i)
    print(i + 1)
