import unittest
from pokemonCatcher import find_pokemons

class TestFindPokemons(unittest.TestCase):

    def test_find_pokemons(self):
        self.assertEqual(find_pokemons("E"), 2)
        self.assertEqual(find_pokemons("NESO"), 4)
        self.assertEqual(find_pokemons("NSNSNSNSNS"), 2)
        self.assertEqual(find_pokemons(""), 1)
        self.assertEqual(find_pokemons("NNNSSS"), 4)
        self.assertEqual(find_pokemons("NNNOOOSSSEEE"), 12)


    # Test the exception case
    def test_find_pokemons_invalid_input(self):
       with self.assertRaises(Exception):
           find_pokemons("WXYZ")

    def test_find_pokemons_empty_input(self):
        with self.assertRaises(Exception):
            find_pokemons()

if __name__ == "__main__":
    unittest.main()