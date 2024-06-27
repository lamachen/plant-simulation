
class Cell:
    def __init__(self, cell_type, energy=0):
        self.cell_type = cell_type
        self.energy = energy

class MeristemCell(Cell):
    def __init__(self, energy=0):
        super().__init__('Meristem', energy)

class ParenchymaCell(Cell):
    def __init__(self, energy=0):
        super().__init__('Parenchyma', energy)

class VascularCell(Cell):
    def __init__(self, energy=0):
        super().__init__('Vascular', energy)

