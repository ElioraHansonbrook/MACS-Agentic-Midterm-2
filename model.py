"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

model.py
"""

from agents import AxelrodAgent
from pathlib import Path
import numpy as np
from mesa import Model
from mesa.space import SingleGrid
import random


class AxelrodModel(Model):
    def __init__(self, seed = None, rng = None, width = 10, height = 10, agentCount = 100):
        super().__init__(seed=seed, rng=rng)
        self.space = SingleGrid(
            width = width,
            height = height,
            torus=False
        )
        for i in range(0,10):
            for j in range(0,10):
                AxelrodAgent(
                    model = self,
                    culture = [
                        random.randint(0,10),
                        random.randint(0,10),
                        random.randint(0,10),
                        random.randint(0,10),
                        random.randint(0,10),
                    ]
                    )
    
    def move(self):
        assert(len(self.agents)==100)


if __name__ == "__main__":
    # Testing board
    model = AxelrodModel()
    model.move()