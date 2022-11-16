import os

sourceDir = os.path.dirname(__file__)

f = open(os.path.join(sourceDir, "week08-05-input.txt"))
lines = f.readlines()
for line in lines: 
    print(f"Words, {line.strip()}")
f.close()