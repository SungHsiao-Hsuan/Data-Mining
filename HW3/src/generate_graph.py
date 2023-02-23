from collections import defaultdict
import random
import utils


# file_name = title
graph_list = []

def gen_graph(vertex_count, edge_count):

    if edge_count > vertex_count * (vertex_count-1) / 2:
        print("Edge number over vertex maximum posibility")
        return

    graph_dic = defaultdict(list)
    node_count_dic = {}

    # Init dictionary
    for v in range(vertex_count):
        graph_dic[v] = []
        node_count_dic[v] = 0

    # print(graph_dic)

    for e in range(edge_count):
        tmp = []
        ori = random.randint(0,vertex_count-1)
        insert = random.randint(0,vertex_count-1)
        while ((ori == insert) or (node_count_dic[ori] == (vertex_count-1)) or (insert in graph_dic[ori])):
            ori = insert = random.randint(0,vertex_count-1)
            insert = random.randint(0,vertex_count-1)

        node_count_dic[ori] += 1
        graph_dic[ori].append(insert)
        tmp.append(ori)
        tmp.append(insert)
        graph_list.append(tmp)

    return graph_list


graph_list = gen_graph(100,1100)
# print(graph_list)

utils.ibm_write_file(
    data = graph_list,
    filename = "../inputs/edge-1100.txt"
)
