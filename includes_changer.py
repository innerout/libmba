import os
import os.path
import sys
import fileinput

if len(sys.argv) < 2:
    print("Directory path not inserted terminating")
    exit(0)
    
print(sys.argv[1])

dir_path = sys.argv[1]
path, dirs, files = next(os.walk(dir_path))
print(path)
print(os.sep)

files_full= []

for file in files:
    files_full.append(path + os.sep + file)

for file in files_full:
    print(file)

for line in fileinput.input(files_full, inplace = 1):
    if '#include' and '\"mba' in line:
        line = line.replace("\"", "<", 1)
        #line = line.replace("mba/", "")
        line = line.replace("\"", ">", 1)
    #elif '#include' and '<mba/':
    #   line = line.replace("mba/", "")
    sys.stdout.write(line)



