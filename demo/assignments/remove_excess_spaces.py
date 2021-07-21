import re
import os

source = "story.txt"
target = "temp.txt"

with open(source, "rt") as sf, open(target, "wt") as tf:
    for line in sf:
        line = line.strip()
        if len(line) > 0:
            result = re.sub(r"\s+", ' ', line)
            tf.write(result + "\n")

os.remove(source)
os.rename(target, source)
