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

