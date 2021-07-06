class UnionFind():
    def __init__(self, size):
        self.size = size
        self.array = [i for i in range(0, self.size + 1)]

    def __repr__(self) -> str:
        return str({idx:grp for idx,grp in zip(
            range(0, self.size + 1), self.array)})

    def find(self, i):
        root = i
        while root != self.array[root]:
            root = self.array[i]
        
        return root

    def union(self, i, j):
        root1, root2 = self.find(i), self.find(j)

        if root1 == root2: # in the same group
            return
        
        if root1 < root2:
            self.array[root1] = root2
        else:
            self.array[root2] = root1