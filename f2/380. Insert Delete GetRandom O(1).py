class RandomizedSet:

    def __init__(self):
        self.mem = {}
        self.loc = []

    def insert(self, val: int) -> bool:
        if val in self.mem:
            return False
        self.mem[val] = len(self.loc)
        self.loc.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mem:
            return False
        index = self.mem[val]
        last_ind = self.loc[-1]
        self.loc[index] = last_ind
        self.mem[self.loc[-1]] = index
        self.loc.pop()
        del self.mem[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.loc)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()