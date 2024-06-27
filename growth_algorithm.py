
from cell_model import MeristemCell, ParenchymaCell, VascularCell

class Plant:
    def __init__(self):
        self.cells = [MeristemCell()]

    def grow(self):
        new_cells = []
        for cell in self.cells:
            if isinstance(cell, MeristemCell):
                new_cells.append(ParenchymaCell(energy=1))
                new_cells.append(VascularCell(energy=1))
            else:
                cell.energy += 1
                print(f"Energy increased for {cell.cell_type} cell: {cell.energy}")
        self.cells.extend(new_cells)
        print(f"Total cells after growth: {len(self.cells)}")

    def simulate_growth(self, steps):
        for step in range(steps):
            print(f"Growth step: {step + 1}")
            self.grow()

if __name__ == '__main__':
    plant = Plant()
    plant.simulate_growth(10)
    for cell in plant.cells:
        print(f"Cell Type: {cell.cell_type}, Energy: {cell.energy}")

        print(f"Cell Type: {cell.cell_type}, Energy: {cell.energy}")

