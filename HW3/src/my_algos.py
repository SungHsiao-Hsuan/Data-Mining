import numpy as np
from collections import defaultdict

def HITS(graph, max_iteration, threshold):

    node_list = build_graph(graph)

    authority_dic, hub_dic = initialization_HITS(node_list)

    norm_auth = {}
    norm_hub = {}

    # Update authority dic and hub dic

    for i in range(max_iteration):

        if i == 0:
            pre_auth, pre_hub = authority_dic.copy(), hub_dic.copy()

        else:
            pre_auth, pre_hub = norm_auth.copy(), norm_hub.copy()

        authority_dic = update_authority(graph, node_list, pre_hub)
        hub_dic = update_hub(graph, node_list, pre_auth)

        norm_auth = normalization(authority_dic)
        norm_hub = normalization(hub_dic)


        check_sum = 0

        if i >= 1:

            for k in authority_dic.keys():
                check_sum += (abs(pre_auth[k] - norm_auth[k]) + abs(pre_hub[k] - norm_hub[k]))


            if check_sum < threshold:

                output_norm_auth = ['%.3f' % norm_auth[k] for k in node_list]
                output_norm_hub = ['%.3f' % norm_hub[k] for k in node_list]

                return output_norm_auth, output_norm_hub


    output_norm_auth = ['%.3f' % norm_auth[k] for k in node_list]
    output_norm_hub = ['%.3f' % norm_hub[k] for k in node_list]

    return output_norm_auth, output_norm_hub


def PageRank(graph, damping_factor, iteration):

    node_list = build_graph(graph)
    total_pages = len(node_list)

    Page_Rank = initialization_PageRank(node_list)

    # Parent dic
    dic_parent = build_parent_dic(graph,node_list)

    for i in range(iteration):

        old_pagerank = Page_Rank.copy()

        for key in Page_Rank.keys():

            # Record node in
            parent_list = find_parent(key,dic_parent)

            parent_score = 0

            if len(parent_list) != 0:
                for p in parent_list:
                    parent_score += (old_pagerank[p] / len(graph[p]))

            Page_Rank[key] = damping_factor/total_pages + (1-damping_factor) * parent_score

        Page_Rank = normalization(Page_Rank)

    output_PageRank = ['%.3f' % Page_Rank[k] for k in node_list]

    return output_PageRank

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



def initialization_HITS(node_list):

    # Build dictionary
    authority = hub = {i: 1 for i in node_list}
    return authority, hub



def initialization_PageRank(node_list):

    n = len(node_list)
    dic = {i: 1/n for i in node_list}
    return dic


def update_authority(graph, node_list, hub_dic):

    new_auth = {i: sum(hub_dic[k] for k, val in graph.items() if i in val) for i in node_list}
    return new_auth


def update_hub(graph, node_list, auth_dic):

    new_hub = {i: sum(auth_dic[h] for h in graph.get(i, [])) for i in node_list}

    return new_hub


def normalization(dic):

    denominator = sum(dic.values())
    norm_dic = {k: dic[k] / denominator for k in dic.keys()}
    return norm_dic



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