class Quadrilateral:

    def __init__(self, side_a, side_b, side_c, side_d):
        self.a = side_a
        self.b = side_b
        self.c = side_c
        self.d = side_d

    def find_perim(self):
        return(sum([self.a, self.b, self.c, self.d]))

    def find_area(self):
        raise NotImplementedError("Method not implemented")


class Rectangle(Quadrilateral):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not(self.a == self.c and self.b == self.d):
            raise ValueError("Not a Rectangle")

    def find_area(self):
        return(self.a*self.b)


shape_1 = Rectangle(1, 2, 1, 2)
print(shape_1.find_area())
