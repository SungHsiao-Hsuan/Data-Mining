from collections import defaultdict
from itertools import combinations

def apriori(dataset,a):

    min_sup = a.min_sup
    min_conf = a.min_conf

    frequent_itemsets = []
    level = 0

    # Create total transactions
    total_transaction = generate_total_transaction(dataset)
    total_transaction_count = len(total_transaction)

    # Creat C1
    C1 = generate_C1(dataset)

    #Find L1
    Lk = generate_Lk(C1,total_transaction_count,min_sup)
    frequent_itemsets.append(Lk)

    # Explore candidates of other levels
    while (len(Lk) > 1):

        Ck = generate_Ck(Lk,total_transaction,level)
        level += 1

        Lk = generate_Lk(Ck,total_transaction_count,min_sup)
        if len(Lk) == 0:
            break

        else:
            frequent_itemsets.append(Lk)


    # Apply generation rule
    recommand_data = generation_rule(min_conf,frequent_itemsets,total_transaction_count)
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


def generate_Ck(Lk1,total_transactions,level):
    # Lk1 represents the frequent itemsets generated from the previous level.

    Ck = {}

    # Generate C2
    if level == 0:

        for key1 in Lk1:
            for key2 in Lk1:

                intersection = set([key1]) & set([key2])

                if len(intersection) == level:
                    union_tuple = tuple(sorted(frozenset([key1]) | (frozenset([key2]))))
                    Ck[union_tuple] = 0


    # Generate other Ck
    else:

        tmp_Ck = {}

        for key1 in Lk1:

            for key2 in Lk1:

                intersection = set(key1) & set(key2)

                if len(intersection) == level:

                    union_tuple = tuple(sorted(frozenset(key1) | frozenset(key2)))
                    tmp_Ck[union_tuple] = 0


        # Check whether the candidate is valid.

        for tmp_Ck_key in tmp_Ck.keys():

            is_valid = True

            for cross in range(len(tmp_Ck_key)):

                other_union = set(tmp_Ck_key) - {tmp_Ck_key[cross]}
                other_union_tuple = tuple(sorted(tuple(other_union)))

                if other_union_tuple not in Lk1:
                    is_valid = False
                    break

            if is_valid == True:
                Ck[tmp_Ck_key] = 0

    # Calculate frequent of valid candidate
    for key in Ck:
        for value in total_transactions.values():
            if set(key).issubset(value):
                Ck[key] += 1

    return Ck


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