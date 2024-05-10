import sys  # to comment
import unittest

sys.path.append('/app')
file_path = '/app/app/ds752_iscritti_anno_accademico_2017-18.csv'

from app.mymodules.Ateneo_Comp import Ateneo_Comp


class TestAteneoComp(unittest.TestCase):

    def test_invalid_input(self):

        result = Ateneo_Comp(file_path, int(5), int(9))
        self.assertEqual(result, 'invalid input')

    def test_none(self):

        result = Ateneo_Comp(file_path, None, None)
        self.assertEqual(result, 'invalid input')

    def test_valid(self):

        result = Ateneo_Comp(file_path, 'Milano', 'Milano Cattolica')
        self.assertEqual(result, {
                                    "Milano Cattolica": {"M": 13466, "F": 24996},
                                    "Milano": {"M": 25373, "F": 35268}})
        

if __name__ == '__main__':
    unittest.main()    