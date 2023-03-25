import time
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

grp = nx.Graph()
height = 5
width = 10
def changeEdgeWeight(grp, n1, n2, data):
    oldWeight = grp.get_edge_data(n1, n2)["weight"]
    grp.add_edge(n1, n2, weight = oldWeight + data)

def updateWeights(grp, weigthArray):
    for i in range(0, height + 1):
        for j in range(0,width + 1):
            if i > 0:
                changeEdgeWeight(grp, str(i) + str(j), str(i - 1) + str(j), abs(weigthArray[i][j] - weigthArray[i - 1][j]))
            if j < width:
                changeEdgeWeight(grp, str(i) + str(j), str(i) + str(j + 1), abs(weigthArray[i][j] - weigthArray[i][j + 1]))

testArray = np.random.randint(10, size=(height + 1,width + 1))
print(testArray)
testArray2 = np.random.randint(10, size=(height + 1,width + 1))
print(testArray2)

def generateGraph(grp):
    for i in range(0,height + 1):
        for j in range(0,width + 1):
            grp.add_node(str(i) + str(j), layer = j)
            if i > 0:
                grp.add_edge(str(i) + str(j), str(i - 1) + str(j), weight = 0)
    #            if j < width:
    #                grp.add_edge(str(i) + str(j), str(i - 1) + str(j + 1), weight=random.randint(0, 101))
            if j < width:
                grp.add_edge(str(i) + str(j), str(i) + str(j + 1), weight = 0)
    #            if i < height:
    #                grp.add_edge(str(i) + str(j), str(i + 1) + str(j + 1), weight=random.randint(0, 101))
    return grp
tic = time.perf_counter()
grp = generateGraph(grp)
toc = time.perf_counter()
updateWeights(grp, testArray)
updateWeights(grp, testArray2)
print(f"Graph generated in {toc - tic:0.4f} seconds")

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


#print(nx.astar_path(grp, '00', '99'))
tic = time.perf_counter()
print(nx.astar_path(grp, '11', '33', weight='weight'))
toc = time.perf_counter()

print(f"Path found in {toc - tic:0.4f} seconds")

printGraph(grp)