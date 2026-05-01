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
        # Height of the model
        self.height = height
        # Width of the model
        self.width = width
        # Instantiate the space in which agents act
        self.space = SingleGrid(
            width = width,
            height = height,
            # No wrap, to conform to Axelrod
            torus=False
        )
        # Add actors to the model
        for i in range(0,width):
            for j in range(0,height):
                # For each square, one actor is assigned
                agent = AxelrodAgent(
                    model = self,
                    #Randomly seed culture of agents with single digit values
                    culture = [
                        # Axelrod is a little bit unclear; model is
                        # described as allowing single digit values
                        # to represent traits, but Axelrod uses
                        # different amounts in some runs. Using
                        # single digits here to reflect the initial
                        # model description
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                        random.randint(0,9),
                    ]
                    )
                # Add agent to the space
                self.space.place_agent(agent, pos=(i,j))
        # Add data collection
        self.datacollector = DataCollector(
            model_reporters = {
                # This is the sole data collector I add, noting the
                # Number of groups in the model
                "same" : self.collectGroups
            }
        )
        # Start collection
        self.datacollector.collect(self)
    
    ## Calculate the total number of groups and return it
    ## O(n) performance
    def collectGroups(self):
        # Using sets, allowing for typical O(1) add/check performance
        acc = set()
        for agent in self.agents:
            # Adding an agent only occurs if it isn't already in the set
            # thanks to sets' hashtable backing
            acc.add(agent.getCultureNumber_int())
        # Return the number of values in the set
        return len(acc)

    def step(self):
        # Confirm number of agents is as expected
        assert(len(self.agents)==self.width*self.height)
        # Select a random agent
        agent = self.agents[random.randint(0, len(self.agents)-1)]
        # Select a random neighbor of the agent in its VonNeumman neighborhood
        neighbor = random.choice(self.space.get_neighbors(moore=False, pos=agent.pos))
        # Calculate similarity between agent and neighbor
        similarity = agent.getCulturalSimilarity(neighbor)
        # Confirm agents aren't identical (to prevent crash) and then
        # use the random function to follow percentage rules set by
        # Axelrod in the model (e.g. a value with similarity 0.4 will
        # update 40% of the time)
        if similarity != 1 and random.randint(0,100)/100 < similarity:
            # Identify a random cultural trait that differs that will become similar
            location = random.choice(agent.culturePositionDifferenceLocations(neighbor))
            # Set the agent's trait equal to that of its neighbor
            agent.culture[location] = neighbor.culture[location]
        # Update the datacollector
        self.datacollector.collect(self)

if __name__ == "__main__":
    # Testing board
    model = AxelrodModel()
    model.step()