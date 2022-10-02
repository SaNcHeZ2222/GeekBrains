class CreatePilePlate:
    def __init__(self, max_len):
        self.pile = [[]]
        self.number = 0
        self.len = max_len

    def add_plate(self, count):
        for _ in range(count):
            self.pile[self.number].append(1)
            if len(self.pile[self.number]) == self.len:
                self.pile.append([])
                self.number += 1
        print(self.pile)

    def add_plate_in_new_list(self, count):
        self.pile.append([])
        self.number += 1
        for _ in range(count):
            self.pile[self.number].append(1)
            if len(self.pile[self.number]) == self.len:
                self.pile.append([])
                self.number += 1
        print(self.pile)

    def delete_pile(self, count):
        index = len(self.pile) - 1
        while True:
            try:
                self.pile[index].pop()
                count -= 1
            except Exception as e:
                del self.pile[index]
                index -= 1
            if count == 0:
                return


pile = CreatePilePlate(4)
pile.add_plate(3)
pile.add_plate_in_new_list(5)
pile.add_plate(3)
pile.add_plate_in_new_list(5)
pile.delete_pile(6)
print(pile.pile)
