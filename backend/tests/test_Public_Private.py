import sys
import unittest
# adding the directory
sys.path.append('/app')
file_path = '/app/app/ds752_iscritti_anno_accademico_2017-18.csv'   # file path to the csv file
# import the function to test
from app.mymodules.Public_Private import Public_Private


# define a test class
class TestPublicPrivate(unittest.TestCase):

    # define a test method
    def test(self):
        # call the function to test
        result = Public_Private(file_path)
        self.assertEqual(result, {
                                "Milano Politecnico": {"M": 29448, "F": 14590},
                                "Milano Cattolica": {"M": 13466, "F": 24996},
                                "Milano Bocconi": {"M": 7519, "F": 5909},
                                "Milano": {"M": 25373, "F": 35268},
                                "Milano Bicocca": {"M": 12892, "F": 20107},
                                "Milano San Raffaele": {"M": 1024, "F": 1578},
                                "Milano IULM": {"M": 1672, "F": 4070},
                                "Rozzano (MI) Humanitas University": {"M": 285, "F": 439}})


# entry point for running the test
if __name__ == '__main__':
    unittest.main()
