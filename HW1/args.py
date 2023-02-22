import argparse

def parse_args():
    p = argparse.ArgumentParser()

    def a(*args, **kwargs):
        p.add_argument(*args, **kwargs)

    a('--min_sup', type=float, default=0.11, help='Minimum support')
    a('--min_conf', type=float, default=0.9, help='Minimum confidence')
    a('--dataset', type=str, default='kaggle.txt', help='Dataset to use, please include the extension')

    return p.parse_args()