from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from equation import makeSTL

app = FastAPI()

origins = [
    'http://localhost:8080',
    'localhost:8080',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', tags=['root'])
async def root() -> FileResponse:
    return FileResponse('../frontend/main.html')


class FunctionSTL(BaseModel):
    formula: str
    xMin: float
    xMax: float
    xStep: float
    yMin: float
    yMax: float
    yStep: float


@app.post('/equation', tags=['geometry'], status_code=204)
async def equation(func: FunctionSTL) -> FileResponse:
    """
    Gets an equation from the user to be turned into an STL
    :param body: an unparsed json containing formula key
    :return:
    """
    surface = makeSTL(func.formula.lower())
    surface.save('to_download.stl')
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')


@app.get('/stlfile', tags=['geometry'], status_code=204)
async def stlfile() -> FileResponse:
    """downloads the most recent stl file"""
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')
