class Triangulo:
    def __init__(self, side_1, side_2, side_3):
        self.side1 = side_1
        self.side2 = side_2
        self.side3 = side_3

    def major_side(self):
        if self.side2 < self.side1 > self.side3:
            return print("lado 1")
        elif self.side1 < self.side2 > self.side3:
            return print("Lado 2")
        elif self.side1 < self.side3 > self.side2:
            return print("Lado 3")
    
    def triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return print("Es un triangulo equilatero")
        elif self.side1 != self.side2 != self.side3:
            return print("Es un trisngulo escaleno")
        else:
            return print("Es un trisngulo isoceles")