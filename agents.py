"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

agents.py
"""

from mesa import Agent

#An agent representing a state in the state system
class AxelrodAgent(Agent):
    def __init__(
            self,
            model,
            culture = [0,0,0,0,0,]
            ):
        super().__init__(model)
        self.culture = culture
    
    @property
    def culture(self):
        return self._culture
    
    ## Setter implementation for culture adds
    ## single digit confirmation, allowing for
    ## the use of an array instead of an int for culture storage
    @culture.setter
    def culture(self, newValue):
        culture = [
            newValue[0]%10,
            newValue[1]%10,
            newValue[2]%10,
            newValue[3]%10,
            newValue[4]%10,
            ]
    
