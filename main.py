import json
import re
file =  open("input.txt", "r")
target_string_list = file.readlines()

data = {}
for pair in target_string_list:

    pair = pair.strip().replace("\n","").split(":")

    if len(pair) == 2:

        print(pair)
        data.update({
            re.sub(' +', ' ', str(pair[0])) : re.sub(' +', ' ', str(pair[1]))
        })





with open("file.json", "w") as file:
    file.write(str(json.dumps(data)))
print(data)

