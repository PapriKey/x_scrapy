import pandas

from source.data_collect_by_api.objects import User


class BFSNode(object):
    def __init__(self, unique, layer=0, expanded=False):
        super(BFSNode).__init__()
        self.unique = unique
        self.layer = layer
        self.expanded = expanded


def get_seed_users(filename="../data/seed_user.csv"):
    """

    :param filename: [display_name,account_name,url]
    :return: [account_name]
    """
    data = pandas.read_csv(filename)
    return data['account_name'].values.tolist()


def breadth_first_search_collect(max_layer=3, get_seeds=get_seed_users, node_cls=User):
    """

    :param max_layer:
    :param get_seeds: the function that get the seed users
    :param node_cls: the class of the node
    :return:
    """
    uniques = get_seeds()
    nodes = {val: node_cls(unique=val) for val in uniques}
    s = [BFSNode(val) for val in uniques]
    while len(s) > 0:
        u = s.pop()  # a bfs-node that is not visited
        f = nodes[u.unique].get_edge()  # a set of node.unique that link with the bfs-node
        if u.layer <= max_layer:
            for node_unique in f:
                if node_unique not in nodes:
                    # TODO: determine whether an account is a robot account
                    nodes[node_unique] = node_cls(node_unique)
                    s.append(BFSNode(node_unique, layer=u.layer + 1))
    return nodes.values()


if __name__ == "__main__":
    breadth_first_search_collect()
