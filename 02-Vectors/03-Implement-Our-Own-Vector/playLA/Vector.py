class Vector:

    def __init__(self, lst: list = []):
        self._values = lst

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        """
        __repr__方法的作用是怎么显示，供系统调用
            representation
            直接调用变量，系统会调用这个方法，返回一个字符串，用作变量的表示
        """
        return "Vector({})".format(self._values)

    def __str__(self):
        """
            print()方法调用
        """
        return "({})".format(", ".join(str(e) for e in self._values))
