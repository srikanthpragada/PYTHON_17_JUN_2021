import os

allfiles = os.walk(r"c:\classroom\jun17\demo")
pattern = input("Enter pattern :")
for (dirname, folders, files) in allfiles:
    for f in files:
        if f.endswith(".py"):
            # open and read file content
            filename = dirname + "\\" + f
            with open(filename) as fp:
                content = fp.read()
                if pattern in content:
                    print(filename)

