import argparse

title = 'graph_4'

def parse_args():
    p = argparse.ArgumentParser()

    def a(*args, **kwargs):
        p.add_argument(*args, **kwargs)



    a('--dataset', type=str, default=f'{title}.txt', help='Dataset to use, please include the extension')
    a('--authority', type=str, default=f'{title}_HITS_authority.txt', help='Dataset to use, please include the extension')
    a('--hub', type=str, default=f'{title}_HITS_hub.txt', help='Dataset to use, please include the extension')
    a('--PageRank', type=str, default=f'{title}_PageRank.txt', help='Dataset to use, please include the extension')
    a('--SimRank', type=str, default=f'{title}_SimRank.txt', help='Dataset to use, please include the extension')
    a('--ibm_dataset', type=str, default=f'{title}.txt', help='Dataset to use, please include the extension')

    return p.parse_args()