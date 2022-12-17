from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


@app.post('/equation')
async def equation():
    """
    Gets an equation from the user to be turned into an STL
    :return:
    """
    return


@app.get('/file/{fid}')
async def stlfile(fid):
    """
    downloads a stl file of the identified equation
    :param fid:
    :return:
    """
    return
