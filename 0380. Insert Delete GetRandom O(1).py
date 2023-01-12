class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.val_index = {} # self.val_index[x] -> 數字 x 出現在 self.vals 的 index
                            # self.vals[self.val_index[x]] = x
        
    def insert(self, val: int) -> bool:
        # if val in self.vals: # list -> O(n)
        if val in self.val_index: # dict -> O(1) hashable
            return False
        self.vals.append(val) # list -> O(1)
        self.val_index[val] = len(self.vals) - 1
        return True

    # self.vals = [0, 3, 2, 1, 8]
    # self.val_index = {0:0, 3:1, 2:2, 1:3, 8:4}
    # if reomve(3)
    def remove(self, val: int) -> bool:
        # if val in self.vals: # list -> O(n)
        if val in self.val_index: # dict -> O(1) hashable
            # self.vals.remove(val) # remove 速度慢  O(n)
            index = self.val_index[val] # index = 1
            last_val = self.vals[-1] # last_val = 8
            self.vals[index] = last_val # self.vals[1] = 8
            self.vals.pop() # .pop() = 8

            self.val_index[last_val] = index # self.val_index[8] = 1
            self.val_index.pop(val) # O(1) val = 3
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.vals) # list -> O(1)
        
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
