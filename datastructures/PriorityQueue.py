class Priority_Queue():
    def __init__(self, array):
        self.queue = self.make_queue(array)

    def make_queue(self, array):
        for i in array:
            self.append(i)
        
    def is_empty(self):
        return len(self.queue) == 0

    def append(self, obj):
        self.queue.append(obj)
        self.swim(len(self.queue) - 1)

    def peek(self):
        return self.queue[0] if not self.is_empty() else None

    def poll(self):
        return self.queue.pop(0)
    
    def remove(self, obj):
        if self.is_empty():
            raise Exception("PQ is empty")

        for i in range(len(self.queue) - 1):
            if self.queue[i] == obj:
                self.swap(i, -1)
                self.queue.pop()
                self.swim(i) # or sink depending on implementation

    def swap(self, i, j):
        self.queue[j], self.queue[i] = self.queue[i], self.queue[j]

    def less(self, i, j):
        return self.queue[i] <= self.queue[j]

    # bottom up swim
    def swim(self, k):
        parent = (k - 1)//2

        while k > 0 and self.less(k, parent):
            self.swap(parent, k)
            k = parent
            parent = (k - 1)//2

    # top down swim
    def sink(self, k):
        left, right = 2*k + 1, 2*k + 2
        smallest = left

        if self.less(right, left) and right < len(self.queue):
            smallest = right

        if self.less(k, smallest) or left >= len(self.queue):
            return
        
        self.swap(smallest, k)
        k = smallest