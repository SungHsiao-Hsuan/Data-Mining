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


# Other functions
def build_graph(graph):

    node_list = set()
    for key, value in graph.items():
        node_list.add(key)
        node_list.update(value)

    return list(node_list)


def initialization_PageRank(node_list):

    n = len(node_list)
    dic = {i: 1/n for i in node_list}
    return dic


def build_parent_dic(graph,node_list):

    dic_parent = {k:[] for k in node_list}

    for key in graph.keys():

        for item_subset in list(graph[key]):
            dic_parent[item_subset].append(key)

    return dic_parent


def find_parent(child,parent_dic):
    return parent_dic[child]


def normalization(dic):

    denominator = sum(dic.values())
    norm_dic = {k: dic[k] / denominator for k in dic.keys()}
    return norm_dic

