"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
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
    return (Public_Private(file_path))


@app.get('/Ateneo_Comp/{nome1}/{nome2}')
def get_Ateneo_Comp(nome1: str, nome2: str):
    return Ateneo_Comp(file_path, nome1, nome2)


@app.get('/Ateneo_Counter')
def get_Ateneo_Counter():
    return (Ateneo_Counter(file_path))
