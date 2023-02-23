import numpy as np

def SimRank(graph, decay_factor, iteration):

    # SimRank init
    node_list = build_graph(graph)
    sim_matrix = np.eye(len(node_list))


    # Parent dic
    dic_parent = build_parent_dic(graph, node_list)

    # Build index dic
    index_dic = {}


    for k in range(len(node_list)):
        index_dic[node_list[k]] = k

    for itr in range(iteration):
        old_matrix = sim_matrix.copy()

        for i in range(len(node_list)):

            for j in range(len(node_list)):

                sim_matrix[i][j] = update_simrank(node_list[i],node_list[j],old_matrix,decay_factor,dic_parent,index_dic)

    return sim_matrix


# Other functions
def build_graph(graph):

    node_list = set()
    for key, value in graph.items():
        node_list.add(key)
        node_list.update(value)

    return list(node_list)


def build_parent_dic(graph,node_list):

    dic_parent = {k:[] for k in node_list}

    for key in graph.keys():

        for item_subset in list(graph[key]):
            dic_parent[item_subset].append(key)

    return dic_parent


def find_parent(child,parent_dic):
    return parent_dic[child]



def get_sim_value(a, b, index_dic, old_sim_matrix):

    index_a = index_dic[a]
    index_b = index_dic[b]

    return old_sim_matrix[index_a][index_b]



def update_simrank(a,b,old_sim_matrix,decay_factor,parent_dic,index_dic):
    if a == b:
        return 1

    else:
        in_a = find_parent(a,parent_dic)
        in_b = find_parent(b,parent_dic)

        if len(in_a) == 0 or len(in_b) == 0:
            return 0

        else:
            Sim_sum = 0
            for i in in_a:
                for j in in_b:
                    Sim_sum += get_sim_value(i,j,index_dic,old_sim_matrix)

        Sim_sum *= (decay_factor/(len(in_a)* len(in_b)))

    return Sim_sum