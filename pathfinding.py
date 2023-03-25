import time
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

grp = nx.Graph()
height = 999
width = 1475

# WATER = 0
# VEGETATION = 1
# DIRT = 2
# MOUNTAINS = 3
# ICE = 4
# OTHER = 5
# WET_GROUND = 6

SCL_WATER_CostArray = np.matrix(
    [
        [100, 100],
        [100, 0]
    ]
)

SCLCostArray = np.matrix(
    [
        [100, 100, 100, 100, 100, 100, 100],
        [100, 0, 10, 50, 40, 40, 20],
        [100, 10, 0, 40, 30, 30, 15],
        [100, 50, 40, 40, 50, 40, 50],
        [100, 40, 30, 50, 90, 90, 40],
        [100, 40, 30, 40, 90, 50, 40],
        [100, 20, 15, 50, 40, 40, 15]
    ]
)

# SCLCostArray = np.matrix([[100, 100, 100, 90, 100],[100, 10, 40, 40, 100],[100, 40, 0, 80, 70],[90, 10, 80, 90, 100],[100, 100, 70, 100, 80]])
# SCLCostArray = np.matrix([[80, 60, 0, 100, 100],[100, 10, 0, 90, 100],[80, 40, 0, 100, 80],[90, 40, 0, 90, 100],[100, 0, 0, 100, 80]])
def getCost(pos1, pos2, filterType):
    return filterType[pos1, pos2]
def changeEdgeWeight(grp, n1, n2, n1Terrain, n2Terrain, filterType):
    oldWeight = grp.get_edge_data(n1, n2)["weight"]
    grp.add_edge(n1, n2, weight = oldWeight + getCost(n1Terrain,n2Terrain, filterType))

def updateWeights(grp, weigthArray, filterType):
    for i in range(0, height + 1):
        for j in range(0,width + 1):
            if i > 0:
                changeEdgeWeight(grp, str(i) + ' ' + str(j), str(i - 1) + ' ' + str(j), weigthArray[i][j], weigthArray[i - 1][j], filterType)
            if j < width:
                changeEdgeWeight(grp, str(i) + ' ' + str(j), str(i) + ' ' + str(j + 1), weigthArray[i][j], weigthArray[i][j + 1], filterType)

def generateGraph(grp):
    for i in range(0,height + 1):
        for j in range(0,width + 1):
            grp.add_node(str(i) + ' ' + str(j), layer = j)
            if i > 0:
                grp.add_edge(str(i) + ' ' + str(j), str(i - 1) + ' ' + str(j), weight = 0)
    #            if j < width:
    #                grp.add_edge(str(i) + str(j), str(i - 1) + str(j + 1), weight=random.randint(0, 101))
            if j < width:
                grp.add_edge(str(i) + ' ' + str(j), str(i) + ' ' + str(j + 1), weight = 0)
    #            if i < height:
    #                grp.add_edge(str(i) + str(j), str(i + 1) + str(j + 1), weight=random.randint(0, 101))
    return grp

def printGraph(grp):
    elarge = [(u, v) for (u, v, d) in grp.edges(data=True) if d["weight"] > 50]
    esmall = [(u, v) for (u, v, d) in grp.edges(data=True) if d["weight"] <= 50]

    pos = nx.multipartite_layout(grp, subset_key="layer")  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(grp, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(grp, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        grp, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels
    nx.draw_networkx_labels(grp, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(grp, "weight")
    nx.draw_networkx_edge_labels(grp, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def dist(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x2-x1) + abs(y2-y1)

def getAStarPath(grp, pix1x, pix1y, pix2x, pix2y):
    tic = time.perf_counter()
    pathList = nx.astar_path(grp, str(pix1x) + ' ' + str(pix1y), str(pix2x) + ' ' + str(pix2y), weight='weight')
    pathPixPos = []
    for pix in pathList:
        temp = pix.split()
        pathPixPos.append((int(temp[0]), int(temp[1])))
    pathCostLis = []
    for n in range(0, len(pathList) - 1):
        pathCostLis.append(grp.get_edge_data(pathList[n], pathList[n + 1])["weight"])
    toc = time.perf_counter()
    print(f"Path found in {toc - tic:0.4f} seconds")
    return((pathPixPos, pathCostLis))

def getWeightArrayFromTxt(path):
    f = open(path, "r")
    weightArr = np.genfromtxt(path,dtype = int, delimiter=',')
    return weightArr


# testArray = np.random.randint(5, size=(height + 1,width + 1))
# print(testArray)
# testArray2 = np.random.randint(5, size=(height + 1,width + 1))
# print(testArray2)

tic = time.perf_counter()
grp = generateGraph(grp)
toc = time.perf_counter()
updateWeights(grp, getWeightArrayFromTxt("SCL.txt"), SCLCostArray)
updateWeights(grp, getWeightArrayFromTxt("SCL-WATER-ONLY.txt"), SCL_WATER_CostArray)
# updateWeights(grp, testArray2, SCLCostArray)
print(f"Graph generated in {toc - tic:0.4f} seconds")

#print(nx.astar_path(grp, '00', '99'))

getAStarPath(grp, 26, 73, 800, 26)

#printGraph(grp)