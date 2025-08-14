from lib.toy import Toy

class ToyBox:
    def __init__(self):
        self.toys = []
    
    def add(self, toy):
        # if type(toy) != Toy:
        if not isinstance(toy, Toy):
            raise Exception("Can only accept Toy(s)")
        self.toys.append(toy)
    
    def get_toys(self):
        return self.toys
    
    def count_and_list_toy(self):
        count = len(self.toys)
        names = []
        for toy in self.toys:
            names.append(toy.name)
        
        return f"You have {count} toys: {", ".join(names)}"