import sys
import unittest

# Importing the Ateneo_Counter class from the specific module
from app.mymodules.Ateneo_Counter import Ateneo_Counter

# Adding the project directory to the Python path
sys.path.append('/app')

# Path to the CSV file
file_path = '/app/app/ds752_iscritti_anno_accademico_2017-2018.csv'


class TestAteneoCounter(unittest.TestCase):
    """ A test case class for testing the Ateneo_Counter class """

    def test(self):
        """ Test method to verify the functionality of the Ateneo_Counter class """

        # Creating an instance of Ateneo_Counter with the provided file_path
        result = Ateneo_Counter(file_path)

        # Asserting the expected output dictionary with the actual result
        self.assertEqual(result, {
            "Milano Politecnico": 44038,
            "Milano Cattolica": 38462,
            "Milano Bocconi": 13428,
            "Milano": 60641,
            "Milano Bicocca": 32999,
            "Milano San Raffaele": 2602,
            "Milano IULM": 5742,
            "Rozzano (MI) Humanitas University": 724})


if __name__ == '__main__':
    # Running the test cases
    unittest.main()
