
import unittest
from cell_model import MeristemCell, ParenchymaCell, VascularCell
from growth_algorithm import Plant

class TestCellModel(unittest.TestCase):
    def test_meristem_cell(self):
        cell = MeristemCell(energy=10)
        self.assertEqual(cell.cell_type, 'Meristem')
        self.assertEqual(cell.energy, 10)

    def test_parenchyma_cell(self):
        cell = ParenchymaCell(energy=5)
        self.assertEqual(cell.cell_type, 'Parenchyma')
        self.assertEqual(cell.energy, 5)

    def test_vascular_cell(self):
        cell = VascularCell(energy=3)
        self.assertEqual(cell.cell_type, 'Vascular')
        self.assertEqual(cell.energy, 3)

class TestPlantGrowth(unittest.TestCase):
    def test_initial_growth(self):
        plant = Plant()
        plant.simulate_growth(1)
        self.assertEqual(len(plant.cells), 3)  # 1 MeristemCell -> 1 ParenchymaCell + 1 VascularCell

    def test_energy_increase(self):
        plant = Plant()
        plant.simulate_growth(1)
        for cell in plant.cells:
            if cell.cell_type != 'Meristem':
                self.assertEqual(cell.energy, 1)

if __name__ == '__main__':
    unittest.main()

