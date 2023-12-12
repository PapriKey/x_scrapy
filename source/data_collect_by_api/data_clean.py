import os.path
import pandas as pd


def data_clean(nodes):
    nodes_data = [node.get_node_properties() for node in nodes]
    nodes_other_data = [node.get_node_information() for node in nodes]
    relations = [node.get_relations2nodes() for node in nodes]

    nodes_df = pd.DataFrame(nodes_data)
    relations_df = pd.DataFrame(relations)
    nodes_other_data_df = pd.DataFrame(nodes_other_data)

    # TODO: data clean

    return nodes_df, relations_df, nodes_other_data_df


def write_to_file(nodes, filepath, **filenames):
    nodes_df, relations_df, nodes_other_data_df = data_clean(nodes)
    nodes_df.to_csv(os.path.join(filepath, str(filenames['nodes_data'])), index=False)
    nodes_other_data_df.to_csv(os.path.join(filepath, str(filenames['nodes_other_data'])), index=False)
    relations_df.to_csv(os.path.join(filepath, str(filenames['relations_data'])), index=False)
