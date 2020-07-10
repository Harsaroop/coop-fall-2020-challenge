class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.list = []
        self.un = 0
        self.list_un = []

        
    def add(self, num: int):
        self.list.append(num)
        self.value += num 

    def subtract(self, num: int):
        e = -1 * num
        self.list.append(e)
        self.value = self.value - num       

    def undo(self):
        self.un = self.list.pop()
        self.value = self.value - self.un

    def redo(self):
        self.list.append(self.un)
        self.value = self.value + self.un

    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.un = self.list.pop()
            self.value = self.value - self.un
            self.list_un.append(self.un)

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.un = self.list_un.pop()
            self.value = self.value + self.un
            self.list.append(self.un)

