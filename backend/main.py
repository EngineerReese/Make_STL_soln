from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from equation import makeSTL

app = FastAPI()

origins = [
    'http://localhost:3000',
    'localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/', tags=['root'])
async def root():
    return FileResponse('frontend/main.html')


@app.post('/equation', tags=['geometry'], status_code=204)
async def equation(formula: str = Form()) -> None:
    """
    Gets an equation from the user to be turned into an STL
    :param formula: a valid equation
    :return:
    """
    return


@app.post('/stlfile', tags=['geometry'], status_code=204)
async def stlfile(formula: str = Form()) -> FileResponse:
    """
    downloads a stl file of the identified equation
    :param formula: a valid equation
    :return:
    """
    surface = makeSTL(formula.lower())
    surface.save('to_download.stl')
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')
