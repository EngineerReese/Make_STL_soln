from math import ceil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from equation import discretizeEquation, makeMesh

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

    @property
    def xNodeCount(self):
        return ceil((self.xMax - self.xMin) / self.xStep)

    @property
    def yNodeCount(self):
        return ceil((self.yMax - self.yMin) / self.yStep)


@app.post('/equation', tags=['geometry'], status_code=204)
async def equation(body: FunctionSTL) -> FileResponse:
    """
    Gets an equation from the user to be turned into an STL
    :param body: an unparsed json containing formula key
    :return:
    """
    mesh = discretizeEquation(
        body.formula.lower(),
        xcount=body.xNodeCount,
        ycount=body.yNodeCount,
        xmin=body.xMin,
        xmax=body.xMax,
        ymin=body.yMin,
        ymax=body.yMax,
    )
    surface = makeMesh(*mesh)
    surface.save('to_download.stl')
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')


@app.get('/stlfile', tags=['geometry'], status_code=204)
async def stlfile() -> FileResponse:
    """downloads the most recent stl file"""
    return FileResponse('to_download.stl', media_type='model/stl', filename='equation.stl')
