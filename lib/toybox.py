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
        names_list = [toy.get_name for toy in self.get_toys()]
        names = []
        for toy in self.get_toys():
            names.append(toy.get_name())
        
        return f"You have {count} toys: {", ".join(names)}"