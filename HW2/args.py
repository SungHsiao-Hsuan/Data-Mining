import argparse

def parse_args():
    p = argparse.ArgumentParser()

    def a(*args, **kwargs):
        p.add_argument(*args, **kwargs)

    a('--dataset', type=str, default='data3.csv', help='Dataset to use, please include the extension')
    a('--gendata',type =str,default = 'data3.csv',help='Name of generated dataset')
    a('--dot_name',type =str,default = 'data3',help='Name of .dot for decision tree')

    return p.parse_args()