"""
Test module for main function

Execute this test by running on the terminal (from the backend/) the command:
pytest --cov=app --cov-report=html tests/
"""

import sys
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

sys.path.append('/app')
file_path = 'app/ds752_iscritti_anno_accademico_2017-18.csv'

client = TestClient(app)


class TestFastAPIEndpoints(unittest.TestCase):
    """
    A test case class for testing FastAPI endpoints.
    """

    @patch('app.main.Public_Private')
    def test_Public_Private(self, mock_Public_Private):
        """
        Verifies that the /Public_Private endpoint returns the expected response.

        The mock_Public_Private function is used to simulate the behavior of the actual Public_Private function and returns a predefined response.
        """
        mock_Public_Private.return_value = {"key": "value"}
        response = client.get('/Public_Private')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"key": "value"})

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_invalid_input(self, mock_Ateneo_Comp):
        """
        Verifies that the /Ateneo_Comp endpoint returns 'invalid input' for invalid input parameters.

        The mock_Ateneo_Comp function is used to simulate the behavior of the actual Ateneo_Comp function and returns 'invalid input' for the specified parameters.
        """
        mock_Ateneo_Comp.return_value = 'invalid input'
        response = client.get('/Ateneo_Comp/5/9')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'invalid input')

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_none(self, mock_Ateneo_Comp):
        """
        Verifies that the /Ateneo_Comp endpoint returns a 404 status code for None input parameters.

        The mock_Ateneo_Comp function is used to simulate the behavior of the actual Ateneo_Comp function and returns 'invalid input' for the specified parameters.
        """
        mock_Ateneo_Comp.return_value = 'invalid input'
        response = client.get('/Ateneo_Comp//')
        self.assertEqual(response.status_code, 404)

    @patch('app.main.Ateneo_Comp')
    def test_Ateneo_Comp_valid(self, mock_Ateno_Comp):
        """
        Verifies that the /Ateneo_Comp endpoint returns the correct comparison of male and female students.

        The mock_Ateneo_Comp function is used to simulate the behavior of the actual Ateneo_Comp function and returns a predefined response for the specified universities.
        """
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
        """
        Verifies that the /Ateneo_Counter endpoint returns the expected response.

        The mock_Ateneo_Counter function is used to simulate the behavior of the actual Ateneo_Counter funxtion and returns a predefined response.
        """
        mock_Ateneo_Counter.return_value = {"key": "value"}
        response = client.get('/Ateneo_Counter')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"key": "value"})


if __name__ == '__main__':
    unittest.main()
