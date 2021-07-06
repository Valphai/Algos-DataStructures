class HashTable():
    def __init__(self) -> None:
        self.MAX = 100
        self.array = [None for i in range(self.MAX)]
        
        """ CHAINING IMPLEMENTATION (LINKED LIST)
        self.array = [[] for i in range(self.MAX)]
        """

    def __setitem__(self, key, value):
        hash_func = hash(key)
        self.array[hash_func] = value
    
    def __getitem__(self, key):
        hash_func = hash(key)
        return self.array[hash_func]
    
    def __delitem__(self, key):
        hash_func = hash(key)
        self.array[hash_func] = None

    """ CHAINING IMPLEMENTATION (LINKED LIST)
    def __setitem__(self, key, value):
        hash_func = hash(key)
        found = False
        for idx, tup in enumerate(self.array[hash_func]):
            if tup[0] == key:
                self.array[hash_func][idx] = (key, value)
                found = True
                break
        if not found:
            self.array[hash_func][idx] = (key, value)
    
    def __getitem__(self, key):
        hash_func = hash(key)
        for tup in self.array[hash_func]:
            if tup[0] == key:
                return tup[1]
    
    def __delitem__(self, key):
        hash_func = hash(key)
        for tup in self.array[hash_func]:
            if tup[0] == key:
                del tup
    """
    """ OPEN ADRESSING
    def __setitem__(self, key, value):
        hash_func = hash(key)
        idx = hash_func
        x = 1
        while self.array[idx] is not None:
            idx = (hash_func + P(key, x)) % N
            x += 1
        self.array[idx] = (key, value)
    """