import os
import sys

path_array = []


# used goto.txt as config from store

def read_file(fullFilename):
    with open(fullFilename) as file:
        for line in file:
            path_array.append(line.strip())


read_file("C:\\bat\\store\\store-files\\goto.txt")

# print(os.getcwd())
paths_map = {}

for path_item in path_array:
    splitted_path_item = []
    update_path_item = path_item.replace("\\", "\\\\")
    path_item_arr = update_path_item.split(" ")
    for path_item in path_item_arr:
        if path_item != "":
            splitted_path_item.append(path_item)
    paths_map[splitted_path_item[0].strip()] = splitted_path_item[1].strip()

if len(sys.argv) > 1:
    firstArg = sys.argv[1]
    sys.stdout.write(paths_map[firstArg])
    sys.exit(0)
else:
    print("")
    for key, value in paths_map.items():
        print("      ", key, "                   ", value)
    print("")
    print(paths_map['py'])
