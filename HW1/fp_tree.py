class Node:
    def __init__(self, name):
        self.name = name
        self.node_count = 1
        self.parent = None
        self.internodes = {}

    def find_node(self, item):

        return self.internodes.get(item, None)


class FP_tree:
    def __init__(self, sorted_transaction):
        self.root = Node("Root")
        self.root.node_count = None
        self.table = {}

    def insert_node(self, transaction):
        current = self.root

        for item in transaction:

            next_node = current.find_node(item)

            if next_node:
                current = next_node
                current.node_count += 1

            else:

                new_node = Node(item)
                new_node.parent = current
                current.internodes[item] = new_node
                current = new_node
                in_list = self.table.get(item)

                if in_list:
                    self.table[item].append(new_node)

                else:
                    self.table[item] = [new_node]

    def sort_table(self,table,sorted_frequent):
        sort_table = {}
        for k in sorted_frequent.keys():
            sort_table[k] = table[k]

        return sort_table