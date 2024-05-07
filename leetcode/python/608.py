import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    lst = []
    for i in range(len(tree)):
        id, val = tree['id'][i], tree['p_id'][i]
        if pd.isnull(val):
            lst.append('Root')
        elif len(tree[tree['p_id']==id]) >= 1:
            lst.append('Inner')
        else:
            lst.append('Leaf')
    tree['type'] = lst
    tree.drop(labels='p_id', axis=1, inplace=True)
    return tree