import pandas as pd


def data_clean(nodes):
    nodes_data = [node.get_node_properties() for node in nodes]
    nodes_other_data = [node.get_node_information() for node in nodes]
    relations = [node.get_relations2nodes() for node in nodes]

    nodes_df = pd.DataFrame(nodes_data)


def write_to_file(nodes, filepath):
    pass
