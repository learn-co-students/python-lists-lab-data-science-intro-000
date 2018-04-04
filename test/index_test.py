import unittest2 as unittest
from ipynb.fs.full.index import *

class TestPythonLists(unittest.TestCase):

    def test_italy(self):
        self.assertEqual(italy, 'Italy')

    def test_mexico(self):
        self.assertEqual(mexico, 'Mexico')

    def test_kindof_neighbors(self):
        self.assertEqual(kindof_neighbors, ['USA', 'Argentina', 'Mexico', 'USA'])

    def test_malta_presence(self):
        self.assertIn('Malta', countries)

    def test_new_mexico_presence(self):
        self.assertNotIn('New Mexico', countries)

    def test_unique_countries(self):
        self.assertItemsEqual(['Argentina', 'Canada', 'Croatia', 'Finland', 'Italy', 'Malta', 'Mexico', 'Morocco', 'South Korea', 'USA'], unique_countries)

    def test_num_repeats(self):
        self.assertEqual(num_of_repeats, 3)
