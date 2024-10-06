class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        self.attributes = iter([{'length': self.length}, {'width': self.width}])
        return self

    def __next__(self):
        try:
            return next(self.attributes)
        except StopIteration:
            raise StopIteration


rectangle = Rectangle(10, 5)
for attribute in rectangle:
    print(attribute)