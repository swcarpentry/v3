class Recent(object):

    def __add__(self, item):
        self.items.append(item)
        self.items = self.items[-self.number:]
        return self

    def __init__(self, number=3):
        self.number = number
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

if __name__ == '__main__':
    history = Recent()
    for era in ['Permian', 'Triassic', 'Jurassic', 'Cretaceous', 'Tertiary']:
        history = history + era
        print len(history), history
