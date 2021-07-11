from glob import glob

files = glob("./**/*.PNG", recursive=True)
print(files)
