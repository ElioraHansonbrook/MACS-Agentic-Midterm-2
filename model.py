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
        self.height = height
        self.width = width
        self.space = SingleGrid(
            width = width,
            height = height,
            torus=False
        )
        for i in range(0,10):
            for j in range(0,10):
                AxelrodAgent(
                    model = self,
                    #Randomly seed culture of agents with single digit values
                    culture = [
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                    ]
                    )
    
    def move(self):
        # Confirm number of agents is as expected
        assert(len(self.agents)==self.width*self.height)


if __name__ == "__main__":
    # Testing board
    model = AxelrodModel()
    model.move()