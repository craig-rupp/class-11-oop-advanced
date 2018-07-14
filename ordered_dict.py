class OrderedDict:
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values 
    
    def items(self):
        coupled_items = []
        for key, value in zip(self._keys, self._values):
            coupled_items.append((str(key), value))
        return coupled_items
    
    def __setitem__(self, key, value):
        if key not in self:
            self._keys.append(key)
            self._values.append(value)
        else:
            idx = self._keys.index(key)
            self._values[idx] = value
        
    def __getitem__(self, key):
        for k, v in zip(self._keys, self._values):
            if key == k:
                return v 
        raise KeyError('No Value for key : {}'.format(repr(key)))
    
    def __contains__(self, item):
        return item in self.keys()
        
    def __len__(self):
        return len(self.keys())
        
    def __eq__(self, other):
        for key, value in zip(self.keys(), self.values()):
            if key not in other or other[key] != value:
                return False
        return True
        
    def __ne__(self, other):
        for i, (a, b) in enumerate(zip(self._keys, self._values)):
            if a not in other._keys or other._keys[i] != self._keys[i]:
                return True
        return False
    
    def __str__(self):
        rst = "{"
        for key, value in zip(self.keys(), self.values()):
            rst += "{}: {}, ".format(repr(key), repr(value))
        rst = rst.rstrip(', ')
        rst += '}'
        return rst
    
    
    #ask for clarity on this
    __repr__ = __str__
    
    def __add__(self, other):
        comb_dict = OrderedDict()
        for ky, vl in zip(self._keys, self._values):
            if ky in other:
                continue
            comb_dict[ky] = vl
        for k, v in zip(other._keys, other._values):
            comb_dict[k] = v
        return comb_dict
        
    @classmethod
    def from_keys(cls, seq):
        new_inst = OrderedDict()
        for item in seq:
            new_inst[item] = None
        return new_inst

d = OrderedDict()

d['language'] = 'Python'
d['other'] = ('a', 'b', 'c')
d['language'] = 'Ruby'
print([d.keys(), d.values()])




