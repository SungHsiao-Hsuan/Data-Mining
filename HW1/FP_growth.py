from collections import defaultdict
from itertools import combinations
from fp_tree import FP_tree


def FP_growth(dataset,a):

    min_sup = a.min_sup
    min_conf = a.min_conf

    frequent_items = {}

    # Create total transactions
    total_transaction = generate_total_transaction(dataset)
    total_transaction_count = len(total_transaction)

    # Creat C1
    C1 = generate_C1(dataset)

    # Create frequent itemsets
    L1 = generate_Lk(C1,total_transaction_count,min_sup)

    # Sort dictionary
    sort_L1 = {k: L1[k] for k in sorted(set(L1))}


    # Sort frequent itemsets
    sorted_item_list = sorted(sort_L1, key=sort_L1.get, reverse=True)

    for keyword in sorted_item_list:
        frequent_items[keyword] = L1[keyword]


    # Renew transactions
    new_total_transaction = {}

    for key1 in total_transaction.keys():
        tmp_list = []
        for key2 in frequent_items.keys():
            if set([key2]).issubset(total_transaction[key1]):
                tmp_list.append(key2)

        if len(tmp_list) >= 1:
            new_total_transaction[key1] = tmp_list


    # Build FP-tree
    tree = FP_tree(new_total_transaction)

    for trans in new_total_transaction.values():
        tree.insert_node(trans)


    # Sort table
    tree.table = tree.sort_table(tree.table,frequent_items)

    # Build tree trasverse order
    tree_trasverse_order = sorted_item_list.copy()
    tree_trasverse_order.reverse()

    # find path of frequent itemset
    frequent_itemset_path = find_frequent_itemset_path(tree.table,tree_trasverse_order,min_sup,total_transaction_count)


    # Find frequent itemsets through path of frequent itemset
    frequent_itemsets = {}
    max_len = 0

    for key, value in frequent_itemset_path.items():

        # Calculate the path of the node counts
        node_pointer = 0

        for path in value:
            path_subset = []

            for node in path:
                path_subset.append(node.name)

            path_subset_length = len(path_subset)

            max_len = max(max_len, path_subset_length)


            # Find path combaination and calculate
            for i in range(1,path_subset_length + 1):

                subset_combination = list(combinations(path_subset,i))

                for j in range(len(subset_combination)):

                    subset_combination[j] = list(subset_combination[j])
                    subset_combination[j].append(key)
                    subset_combination[j] = tuple(sorted(tuple(subset_combination[j])))

                    if subset_combination[j] in frequent_itemsets:

                        frequent_itemsets[subset_combination[j]] += tree.table[key][node_pointer].node_count
                    else:
                        frequent_itemsets[subset_combination[j]] = tree.table[key][node_pointer].node_count

            node_pointer += 1


    # Resort frequent_itemsets
    resort_frequent_itemsets = []
    resort_frequent_itemsets.append(frequent_items)

    # add prefix and node
    max_len += 1
    for target_len in range(2,max_len + 1):
        tmp_resort = {}

        for k in frequent_itemsets.keys():
            if len(k) == target_len and frequent_itemsets[k] / total_transaction_count >= min_sup:
                tmp_resort[k] = frequent_itemsets[k]

        resort_frequent_itemsets.append(tmp_resort)

    recommand_data = generation_rule(min_conf,resort_frequent_itemsets,total_transaction_count)
    return recommand_data


# Other functions

def generate_total_transaction(dataset):
    total_transaction = defaultdict(set)

    for transaction in dataset:
        total_transaction[transaction[0]].add(transaction[2])

    return total_transaction


def generate_C1(dataset):
    C1 = defaultdict(int)
    for transaction in dataset:
        C1[transaction[2]] += 1

    return C1

def generate_Lk(candidate_dictionary,total_count,min_sup):

    return {key:value for key,value in candidate_dictionary.items() if value / total_count >= min_sup}


def find_frequent_itemset_path(table,sorted_itemsets,min_sup,total_transaction):

    conditional_pattern = {}

    for item in sorted_itemsets:
        subtree_item = table[item]
        pattern_list = []

        tmp_path_dic = defaultdict(int)

        for node in subtree_item:
            path = []
            current = node

            path_count = current.node_count
            while current.parent.name != "Root":

                current = current.parent
                path.append(current)
                tmp_path_dic[current.name] += path_count

            pattern_list.append(path)


        discard_node = []

        for tmp_k in tmp_path_dic.keys():

            if tmp_path_dic[tmp_k] / total_transaction < min_sup:
                discard_node.append(tmp_k)


        new_pattern_list = []
        for path in pattern_list:

            path = [it for it in path if it.name not in discard_node]
            new_pattern_list.append(path)

        conditional_pattern[node.name] = new_pattern_list

    return conditional_pattern


def generation_rule(min_conf,frequent_itemsets,total_itemsets_cont):

    recommand_data = []

    # Find all possible frequent itemsets
    # Example：(0,1,2)：{0}->{1,2}, {1}->{0,2}, {2}->{0,1},{0,1}->{2}, {1,2}->{0},{0,2}->{1}

    for subitems in range(len(frequent_itemsets)-1,0,-1):
        sub_frequent_itemset = frequent_itemsets[subitems]

        for key in  sub_frequent_itemset.keys():

            level = len(key)
            pointer = 1

            key_set = set(key)

            while level > 1:

                sub_comb = list(combinations(key_set,level-1))

                for i in range(len(sub_comb)):

                    tmp_relation = [set(sub_comb[i])]
                    other_items = set(key) - set(sub_comb[i])
                    tmp_relation.append(other_items)

                    target = list(tmp_relation[0])[0] if len(tmp_relation[0]) == 1 else tuple(sorted(tmp_relation[0]))

                    # Calculate confidence
                    conf_denominator = frequent_itemsets[subitems-pointer][target]
                    conf_numerator = frequent_itemsets[subitems][key]

                    conf = conf_numerator / conf_denominator

                    # Check if the confidence is above the minimum confidence threshold.
                    if conf >= min_conf:

                        tmp_relation.append('%.3f'%(round(conf_numerator/total_itemsets_cont,3)))
                        tmp_relation.append('%.3f'%(round(conf,3)))

                        # Calculate lift
                        lift_denominator_length = len(tmp_relation[1])

                        if lift_denominator_length == 1:

                            lift_denominator = frequent_itemsets[lift_denominator_length-1][list(tmp_relation[1])[0]] / total_itemsets_cont

                        else:

                            lift_denominator = frequent_itemsets[lift_denominator_length-1][tuple(sorted(tuple(tmp_relation[1])))] / total_itemsets_cont

                        lift = conf / lift_denominator

                        tmp_relation.append('%.3f'%(round(lift,3)))

                        recommand_data.append(tmp_relation)

                level -= 1
                pointer += 1

    return recommand_data