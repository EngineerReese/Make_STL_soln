from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from equation import equations

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
    return {}


@app.post('/equation', tags=['geometry'])
async def equation() -> dict:
    """
    Gets an equation from the user to be turned into an STL
    :return:
    """
    newId = max(equations.keys()) + 1
    equations[newId] = 0
    return {
        'message': 'equation added',
        'id': newId,
    }


@app.get('/file/{fid}', tags=['geometry'])
async def stlfile(fid: int) -> dict:
    """
    downloads a stl file of the identified equation
    :param fid:
    :return:
    """
    return {}
