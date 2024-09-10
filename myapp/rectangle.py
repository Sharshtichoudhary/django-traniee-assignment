class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __len__(self):
        return 2  # Indicate there are two elements 

    def __getitem__(self, index):
        if index == 0:
            return {'length': self.length}
        elif index == 1:
            return {'width': self.width}
        else:
            raise IndexError("Index out of range")
        
        
# Sample example
rect = Rectangle(6, 3)

for item in rect:
    print(item)