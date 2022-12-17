"""
Module contains functions for interacting with equations in cartesian coordinates
"""
from itertools import pairwise

import numpy as np
from stl import Mesh
import sympy


def discretizeEquation(formula: str, nodeCount=10, xlim=5, ylim=5) -> tuple[np.ndarray, np.ndarray]:
    equation = sympy.sympify(formula)

    xRange = np.linspace(-xlim, xlim, nodeCount)
    yRange = np.linspace(-ylim, ylim, nodeCount)

    points = []
    for x in xRange:
        for y in yRange:
            points.append([x, y, equation.evalf(subs={'x': x, 'y': y})])

    faces = []
    numX = len(xRange)
    numY = len(yRange)
    for x1, x2 in pairwise(range(numX)):
        for y1, y2 in pairwise(range(numY)):
            faces.append([x1+y1*numY, x1+y1*numY+1, x1+1+(y1+1)*numY])
            faces.append([x1+y1*numY, x1+1+(y1+1)*numY, x1+(y1+1)*numY])

    return np.array(points, dtype=float), np.array(faces)


def makeMesh(points: np.ndarray, faces: np.ndarray):
    surface = Mesh(np.zeros(faces.shape[0], dtype=Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            surface.vectors[i][j] = points[f[j], :]
    return surface


def makeSTL(formula: str):
    mesh = discretizeEquation(formula)
    return makeMesh(*mesh)
