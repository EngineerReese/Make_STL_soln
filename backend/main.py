import json

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

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


@app.post('/equation', tags=['geometry'], status_code=204)
async def equation(body: str = Body()) -> FileResponse:
    """
    Gets an equation from the user to be turned into an STL
    :param body: an unparsed json containing formula key
    :return:
    """
    formula = json.loads(body)['formula']
    surface = makeSTL(formula.lower())
    surface.save('to_download.stl')
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')


@app.get('/stlfile', tags=['geometry'], status_code=204)
async def stlfile() -> FileResponse:
    """downloads the most recent stl file"""
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')
