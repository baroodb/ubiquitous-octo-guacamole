from fastapi import FastAPI, File, UploadFile, Form
import numpy as np
from typing import Optional
import cv2
import shutil

app = FastAPI()


@app.get('/hello')
def hello():
    return {'Hello': 'World'}


@app.post('/upload/')
def upload(image: bytes = File(...)):
    return {'filesize': len(image)}


@app.post('/upload2')
def upload2(image2: UploadFile = File(...)):

    with open(image2.filename, 'wb') as buffer:
        shutil.copyfileobj(image2.file, buffer)
    img = cv2.imread(image2.filename)
    return {"Response": img.shape}