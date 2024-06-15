import sys
import unittest

# Importing the Ateneo_Counter class from the specific module
from app.mymodules.Ateneo_Counter import Ateneo_Counter

sys.path.append('/app')  # we added /app to the list of directories to allow Python to find modules located in the /app directory
file_path = 'app/ds752_iscritti_anno_accademico_2017-18.csv'  # assign the path of the file selected to file_path


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
