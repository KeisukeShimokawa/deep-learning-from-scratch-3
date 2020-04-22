import numpy as np


class Variable:
    '''
    numpyの多次元配列のみを取り扱うデータ構造
    '''
    def __init__(self, data):
        self.data = data


data = np.array(1.0)
x = Variable(data)
print(x.data)

x.data = np.array(2.0)
print(x.data)