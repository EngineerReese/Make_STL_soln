import unittest
import numpy as np

import equation


class EquationTestCase(unittest.TestCase):
    def test_discretizeEquation(self):
        points, faces = equation.discretizeEquation('x+y', xlim=1, ylim=1, nodeCount=3)
        actualPoints = np.array([
            [-1, -1, -2],
            [-1, 0, -1],
            [-1, 1, 0],
            [0, -1, -1],
            [0, 0, 0],
            [0, 1, 1],
            [1, -1, 0],
            [1, 0, 1],
            [1, 1, 2],
        ], dtype=float)
        self.assertTrue(np.allclose(points, actualPoints))
        print(faces)
        actualFaces = np.array([
            [0, 1, 4],
            [0, 4, 3],
            [3, 4, 7],
            [3, 7, 6],
            [1, 2, 5],
            [1, 5, 4],
            [4, 5, 8],
            [4, 8, 7],
        ])
        self.assertTrue(np.allclose(faces, actualFaces))
