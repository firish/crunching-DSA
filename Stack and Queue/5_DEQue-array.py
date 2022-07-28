# DEQue -> Double ended queue, support insertion and deletion at both front and rear end


class DEQue:

    def __init__(self):
        self._data = []

    def __len__(self): return(len(self._data))

    def isEmpty(self): return len(self._data) == 0

    def addFirst(self, el): pass