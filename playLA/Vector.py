class Vector:
    
    def __init__(self, lst):
        self._values = lst

    def __add__(self, another):
        assert len(self) == len(another), '请输入维度一样的变量'
        return Vector([a + b for a,b in zip(self, another)])
    
    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        ''' 返回向量长度 （有多少个元素） '''
        return len(self._values)
    
    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))