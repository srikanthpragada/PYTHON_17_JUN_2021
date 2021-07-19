import os

allfiles = os.walk(r"c:\classroom\jun17\demo")
count = 0
for (dirname, folders, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            count += 1
            print(dirname + "\\" + f)

print(f"Found {count} files")