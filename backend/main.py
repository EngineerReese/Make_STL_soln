from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from equation import equations, makeSTL

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


@app.get('/stlfile/{eid}', tags=['geometry'])
async def stlfile(eid: int) -> FileResponse:
    """
    downloads a stl file of the identified equation
    :param eid: id of an equation previously uploaded
    :return:
    """
    try:
        source = makeSTL(eid)
    except KeyError:
        raise HTTPException(status_code=404, detail='Error: No equation found by that id')
    else:
        return FileResponse('')
