class BellTower:
    def __init__(self, new_arr=()):
        self.arr = list(new_arr)

    def sound(self):
        for i in self.arr:
