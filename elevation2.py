from PIL import Image

layer = "GEO"

COST_PER_COLOR = {
    "SCL-WATER-ONLY":{
        (0, 0, 255): 0,
        "DEFAULT": 1,
    },
    "SCL": {
        (16, 211, 45): 1,
        (255, 255, 83): 2,
        (129, 129, 129): 3,
        (134, 134, 134): 3,
        (192, 192, 192): 3,
        (83, 255, 250): 4,
        "DEFAULT": 5,
    },
    "GEO": {
        "DEFAULT": 5
    }
}

image = Image.open("forfilip.png")
pixels = list(image.getdata())
width, height = image.size
rows = [pixels[i * width:(i + 1) * width] for i in range(height)]
p_p = []
cost_per_pixel = []
with open(f"elevation2.txt", "w") as cost_file:
    x=[]
    for row in rows:
        _row = []
        for pixel in row:
            if pixel not in p_p:
                p_p.append(pixel)

            cost = "NA"  # default cost
            try:
                if pixel in COST_PER_COLOR[layer].keys():
                    cost = str(COST_PER_COLOR[layer][pixel])
                else:
                    cost = str(COST_PER_COLOR[layer]["DEFAULT"])
            except KeyError:
                pass
            _row.append(cost)
        x.append(_row)
        cost_file.write(", ".join(_row))
        cost_file.write("\n")

print(p_p)
