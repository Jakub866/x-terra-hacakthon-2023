import xml.etree.ElementTree as ET
import numpy as np

from PIL import Image

tree = ET.parse('highways_openstreetmaps.txt')
root = tree.getroot()

h = 1000
w = 1476
bblatlon = [46.285274888842004, 6.763458251872402, 46.56358153431913, 7.359466553089039]
dw = (bblatlon[3] - bblatlon[1]) / w
dh = (bblatlon[2] - bblatlon[0]) / h

roadtypemap = {
    'trunk': 210,
    'primary': 211,
    'secondary': 212,
    'tertiary': 213
}
shape = (h, w)
roads = np.zeros(shape, np.int8)



def platlon2xy(platlon):
    return [int(round((platlon[1] - bblatlon[1]) / dw)), int(round((platlon[0] - bblatlon[0]) / dh))]


def pxy2latlon(pxy):
    return [bblatlon[1] + pxy[0] * dw, bblatlon[0] + pxy[1] * dh]


def render_point(p, highway):
    if 0 <= p[0] < w and 0 <= p[1] < h:
        roads[p[1]][p[0]] = roadtypemap.get(highway, 0)


def render_way(nodes, highway):
    last = -1
    for node in nodes:
        p = platlon2xy(node)
        if p != last:
            if last != -1:
                d = [p[0] - last[0], p[1] - last[1]]
                if abs(d[0]) > 1 or abs(d[1]) > 1:
                    if abs(d[0]) >= abs(d[1]):
                        for dx in range(1, abs(d[0])):
                            dy = int(round(dx * d[1] / d[0]))
                            render_point([last[0] + dx, last[1] + dy], highway)
                    else:
                        for dy in range(1, abs(d[1])):
                            dx = int(round(dy * d[0] / d[1]))
                            render_point([last[0] + dx, last[1] + dy], highway)
            render_point(p, highway)
            last = p


def process_ways(r):
    for child in r:
        if child.tag == 'way':
            nodes = []
            for nd in child.findall('nd'):
                nodes.append([float(nd.attrib['lat']), float(nd.attrib['lon'])])
            highway = 0
            for tag in child.findall('tag'):
                if tag.attrib['k'] == 'highway':
                    highway = tag.attrib['v']
            render_way(nodes, highway)


process_ways(root)

img = Image.fromarray(roads, mode="L")
img.save('roads.png')
