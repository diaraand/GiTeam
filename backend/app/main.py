"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves as the backend for the project. IT provides endpoints to retrieve data related to universities and enrolled students from a CSV file.

Endpoints:
1. GET '/Public_Private':
    - Retrieves and returns the comparison of male (M) and female (F) students between public and private universities.

2. GET '/Ateneo_Comp/{nome1}/{nome2}':
    - Retrieves and returns the comparison of male (M) and female (F) students enrolled in two specified universities.
    - Parameters:
        - nome1 (str): Name of the first university.
        - nome2 (str): Name of the second university.

3. GET '/Ateneo_Counter':
    - Retrieves and returns the total number of students enrolled in each university.

Dependencies:
- FastAPI: Modern web framemork for building APIs with Python.
- pandas: Data analysis library used for reading and processing CSV data.

Usage:
- Run this module to start the FastAPI application. IT exposes endpoints that interact with CSV data located at '/app/app/ds752_iscritti_anno_accademico_2017-18.csv', providing data on universities and enrolled students.
"""

from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd


from .mymodules.Public_Private import Public_Private
from .mymodules.Ateneo_Comp import Ateneo_Comp
from .mymodules.Ateneo_Counter import Ateneo_Counter
app = FastAPI()
file_path = '/app/app/ds752_iscritti_anno_accademico_2017-18.csv'


@app.get('/Public_Private')
def get_Public_Private():
    """
    Retrieves and returns the comparison of male (M) and female (F) students bewteen public and private universities.

    Returns:
    - JSONResponse: JSON response containing the compsriosn data
    """
    return (Public_Private(file_path))


@app.get('/Ateneo_Comp/{nome1}/{nome2}')
def get_Ateneo_Comp(nome1: str, nome2: str):
    """
    Retrieves and returns the comparison of male (M) and female (F) students enrolled in two specified universities.

    Args:
    - nome1 (str): Name of the first university.
    - nome 2 (str): Name of the second university.

    Returns:
    -JSONResponse: JSON response containing the comparison data.
    """
    return Ateneo_Comp(file_path, nome1, nome2)


@app.get('/Ateneo_Counter')
def get_Ateneo_Counter():
    """
    Retrieves and returns the total number of students enrolled in each univeristy.

    Returns:
    - JSONResponse: JSON response containing the toal number of students for each university.
    """
    return (Ateneo_Counter(file_path))
