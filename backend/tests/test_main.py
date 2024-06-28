import sys
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

sys.path.append('/app')
file_path = 'app/ds752_iscritti_anno_accademico_2017-18.csv'

client = TestClient(app)


class TestFastAPIEndpoints(unittest.TestCase):

    @patch('app.main.Public_Private')
    def test_Public_Private(self, mock_Public_Private):
        mock_Public_Private.return_value = {"key": "value"}
        response = client.get('/Public_Private')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"key": "value"})

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_invalid_input(self, mock_Ateneo_Comp):
        mock_Ateneo_Comp.return_value = 'invalid input'
        response = client.get('/Ateneo_Comp/5/9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'invalid input')

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_none(self, mock_Ateneo_Comp):
        mock_Ateneo_Comp.return_value = 'invalid input'
        response = client.get('/Ateneo_Comp//')
        self.assertEqual(response.status_code, 404)

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_valid(self, mock_Ateno_Comp):
        mock_Ateno_Comp.return_value = {
            "Milano Cattolica": {"M": 13466, "F": 24996},
            "Milano": {"M": 25373, "F": 35268}
        }
        response = client.get('Ateneo_Comp/Milano/Milano%20Cattolica')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "Milano Cattolica": {"M": 13466, "F": 24996},
            "Milano": {"M": 25373, "F": 35268}
        })

    @patch('app.main.Ateneo_Counter')
    def test_Ateneo_Counter(self, mock_Ateneo_Counter):
        mock_Ateneo_Counter.return_value = {"key": "value"}
        response = client.get('/Ateneo_Counter')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"key": "value"})


if __name__ == '__main__':
    unittest.main()
