import numpy as np


class Variable:
    '''
    numpyの多次元配列を格納するためのクラス
    '''
    def __init__(self, data):
        self.data = data


# class Function:
#     '''
#     Variableクラスを入力に受け取り、
#     入力と出力の対応関係を計算し、
#     計算結果をVariableクラスとして出力する
#     '''
#     def __call__(self, input):
#         x = input.data
#         y = x ** 2
#         output = Variable(y)
#         return output


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        return output

    def forward(self, in_data):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        return x ** 2


x = Variable(np.array(10))
f = Square()
y = f(x)

print(type(y))
print(y.data)
