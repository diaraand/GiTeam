"""
Test module for the Public_Private function.

Execute this test by running on the terminal (from the backend/) the command:
pytest --cov=app --cov-report=html tests/
"""

import sys
import unittest
from app.mymodules.Public_Private import Public_Private  # import the function to test
# adding the directory
sys.path.append('/app')
file_path = 'app/ds752_iscritti_anno_accademico_2017-18.csv'  # file path to the csv file


# define a test class
class TestPublicPrivate(unittest.TestCase):
    """
    A test case for testing the Public_Private function.
    """

    # define a test method
    def test(self):
        """
        Verifies that the Public_Private function correctly calculates the number of male (M) and female (F) students enrolled in each university.

        The test compares the output of the Public_Private function against the expected result to ensure the function's accuracy.
        """
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
