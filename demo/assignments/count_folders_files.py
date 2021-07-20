import os

allfiles = os.walk(r"c:\classroom\jun17\demo")

folders_count = files_count = 0

for (dirname, folders, files) in allfiles:
    folders_count += 1
    files_count += len(files)

print(f"No. of folder :  {folders_count:3}")
print(f"No. of files  :  {files_count:3}")
