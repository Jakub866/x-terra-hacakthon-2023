import os
import json

HFiles_dir = "hfiles/"
width = 1476

plot = []
current_line = []
last_known_elevation = 0
files_len = len(os.listdir(HFiles_dir))
filenames = [f"hfile{i}.txt" for i in range(files_len)]
for filename in filenames:
    file_path = f"{HFiles_dir}/{filename}"
    with open(file_path, "r") as file:
        _info = json.loads(file.readline().replace("'", '"')).get("results", [])
        for pixel in _info:
            last_known_elevation = pixel.get("elevation", last_known_elevation) or last_known_elevation
            current_line.append(str(int(last_known_elevation)))
        plot.append(current_line)

plot2 = []
for i in range(1000):
    line = []
    for j in range(1476):
        line.append(plot[j][i])
    plot2.append(line)

print(len(plot2))
print(len(plot2[0]))
out = open("elevation.txt", "w")
out.write("\n".join([", ".join(l) for l in plot2]))
