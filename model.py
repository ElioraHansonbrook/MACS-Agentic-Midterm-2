"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

model.py
"""

from agents import AxelrodAgent
from pathlib import Path
import numpy as np
from mesa import Model, DataCollector
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
                agent = AxelrodAgent(
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
                self.space.place_agent(agent, pos=(i,j))
        self.datacollector = DataCollector(
            model_reporters = {
                "same" : self.collectGroups
            }
        )
        self.datacollector.collect(self)
    
    def collectGroups(self):
        acc = set()
        for agent in self.agents:
            if agent.getCultureNumber_int() not in acc:
                acc.add(agent.getCultureNumber_int())
        print(acc)
        return len(acc)

    def step(self):
        # Confirm number of agents is as expected
        assert(len(self.agents)==self.width*self.height)
        # for agent in self.agents:
        #     agent.outline = None
        agent = self.agents[random.randint(0, len(self.agents)-1)]
        # agent.outline = "red"
        neighbor = random.choice(self.space.get_neighbors(moore=False, pos=agent.pos))
        similarity = agent.getCulturalSimilarity(neighbor)
        if similarity != 1 and random.randint(0,100)/100 < similarity:
            location = random.choice(agent.culturePositionDifferenceLocations(neighbor))
            agent.culture[location] = neighbor.culture[location]
        self.datacollector.collect(self)

if __name__ == "__main__":
    # Testing board
    model = AxelrodModel()
    model.step()