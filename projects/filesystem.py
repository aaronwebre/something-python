from pathlib import Path
import os

directory = "../"

print("Found .py files:")
for filename in Path(directory).glob('**/*.py'):
    print(filename)

list = os.listdir(directory)
pairs = []

print("File sizes:")
for file in list:
    location = os.path.join(directory, file)
    size = os.path.getsize(location)
    pairs.append((size, file))

pairs.sort(key=lambda s: s[0])

for pair in pairs:
    print(pair)


