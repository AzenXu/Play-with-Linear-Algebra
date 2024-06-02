from .Vector import Vector
from typing import Tuple

class Matrix:

    def __init__(self, list2d):
        # 构造函数，传入二维列表作为矩阵的值
        self._values = [row[:] for row in list2d]

    
    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    def row_num(self):
        """返回矩阵的行数"""
        return self._values.__len__()
    
    def col_num(self):
        """返回矩阵的列数"""
        return self._values[0].__len__()


    def shape(self):
        """返回矩阵的形状: (行数， 列数)"""
        # 矩阵是几行几列的
        # 这里定义的是以「行向量」为基本单位的矩阵
        return self.row_num(), self.col_num()


    def __getitem__(self, pos: Tuple[int, int]):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]


    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c



    __len__ = row_num   # 矩阵的行数，等于矩阵的长度（因为行向量是基本单位）


    def row_vector(self, index):
        """返回矩阵的第index个行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵的第index个列向量"""
        return Vector([row[index] for row in self._values])
