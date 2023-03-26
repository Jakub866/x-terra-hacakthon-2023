




from pyproj import Transformer
import requests

inProj = 'epsg:3857'
outProj = 'epsg:4326'
height = 1000
width = 1476


x1,y1, x2, y2 = 752904.7286,5826183.1700, 819252.0692,5871128.1426


transformer = Transformer.from_crs(inProj, outProj)

ox1, oy1 = transformer.transform(x1, y1)
ox2, oy2 = transformer.transform(x2, y2)

print(ox2, oy2)
print(ox1, oy1)


# print(ox1-ox2)
# print(oy1-oy2)

shiftX = ox1-ox2
shiftY = oy1-oy2

shiftX = shiftX / width
shiftY = shiftY / height
counter = 0
print(shiftY, shiftX)

currentX, currentY = ox1, oy2

print(currentX)
print(currentY)


# PIXEL TO CORDINATES (W PXY (DANE, 1000-DANE))
def platlon(pxy, bblatlon=[46.285274888842004, 6.763458251872402, 46.56358153431913, 7.359466553089039], h=1000, w=1476):
    dx = (bblatlon[3] - bblatlon[1]) / w
    dy = (bblatlon[2] - bblatlon[0]) / h

    return [bblatlon[0] + (pxy[1] * dy), bblatlon[1] + (pxy[0] * dx)]

a = platlon(pxy=(492, 333))
b = platlon(pxy=(492, 666))
c = platlon(pxy=(984, 333))
d = platlon(pxy=(984, 666))

print(a)
print(b)
print(c)
print(d)

from weather import get_forecast

a_rain = get_forecast(*a)
b_rain = get_forecast(*b)
c_rain = get_forecast(*c)
d_rain = get_forecast(*d)

# |------------------|
# |   a    |   b     |
# |------------------|
# |   c    |   d     |
# |------------------|

scl_file = open("SCL.txt", "r")

lines = scl_file.readlines()
_lines = []
for line in lines:
    _lines.append(line.strip().split(", "))

# print(_lines)

MIN_RAIN = 3

# a
if a_rain >= MIN_RAIN:
    for w in range(round(width/2)):
        for h in range(round(height/2)):
            if _lines[h][w] == "2":
                _lines[h][w] = "6"


# b
if b_rain >= MIN_RAIN:
    for w in range(round(width/2), width - 1):
        for h in range(round(height/2)):
            if _lines[h][w] == "2":
                _lines[h][w] = "6"

# sciaganie zdjęć użytkowników google maps (z opinii, od przewodników)

# c
if c_rain >= MIN_RAIN:
    for w in range(round(width/2)):
        for h in range(round(height/2), height - 1):
            if _lines[h][w] == "2":
                _lines[h][w] = "6"

# d
if d_rain >= MIN_RAIN:
    for w in range(round(width/2), width - 1):
        for h in range(round(height/2), height - 1):
            if _lines[h][w] == "2":
                _lines[h][w] = "6"

scl_file2 = open("SCL2.txt", "w")
scl_file2.write("\n".join([", ".join(l) for l in _lines]))
