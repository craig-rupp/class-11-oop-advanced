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
        self._keys.append(key)
        self._values.append(value)
        
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
        if len(self._keys) != len(other._values):
            return False
        for k, v in zip(self._keys, self._values):
            if k not in other._keys or other[k] != v:
                return False
        return True
    
    def __str__(self):
        result = '{'
        for key, value in zip(self._keys, self._values):
            result += '{}: {}, '.format(repr(key), repr(value))
            result = result.rstrip(', ')
        result += '}'
        return result 
    
    #ask for clarity on this
    __repr__ = __str__
    
        
    
    


