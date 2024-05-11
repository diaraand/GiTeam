import sys  # to import sys module to access to some variables
import unittest  # we imported the testing framework
from app.mymodules.Ateneo_Comp import Ateneo_Comp  # we imported the function Ateneo_Comp from Ateneo_Comp.py module located in the mymodules packed within app package

sys.path.append('/app')  # we added /app to the list of directories to allow Python to find modules located in the /app directory
file_path = '/app/app/ds752_iscritti_anno_accademico_2017-18.csv'  # assign the path of the file selected to file_path


class TestAteneoComp(unittest.TestCase):  # the test class will inherit a set of methods and assertions used to write test cases

    def test_invalid_input(self):  # define the test method within the TestAteneoComp class in order to test the behavior of Ateneo_Comp when invalid input is provided

        result = Ateneo_Comp(file_path, int(5), int(9))  # this is to call the function with invalid input parameter and it assign it to result
        self.assertEqual(result, 'invalid input')  # it puts the result equal to invalid input

    def test_none(self):

        result = Ateneo_Comp(file_path, None, None)
        self.assertEqual(result, 'invalid input')

    def test_valid(self):

        result = Ateneo_Comp(file_path, 'Milano', 'Milano Cattolica')  # the test will be valid only if we for example Milano and Milano Cattolica
        self.assertEqual(result, {
                                    "Milano Cattolica": {"M": 13466, "F": 24996},
                                    "Milano": {"M": 25373, "F": 35268}})


if __name__ == '__main__':  # checks if the script is being run as the main program
    unittest.main()  # collects all the test cases and runs them