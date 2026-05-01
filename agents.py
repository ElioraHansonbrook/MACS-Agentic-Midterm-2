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
        self.outline = None
    
    ## An initial implementation for getting an integer representing culture from the culture vector
    def getCultureNumber_string(self):
        return f"{hex(int(self.culture[0]*1.6))[2]}{hex(int(self.culture[1]*1.6))[2]}{hex(int(self.culture[2]*1.6))[2]}{hex(int(self.culture[3]*1.6))[2]}{hex(int(self.culture[4]*1.6))[2]}"

    ## An O(1) complexity, presumed high speed implementation of calculating the culture number
    def getCultureNumber_int(self):
        return self.culture[0]*10**4 * self.culture[0]*10**3 * self.culture[0]*10**2 * self.culture[0]*10**1 * self.culture[0]*10**0

    ## Calculate the degree of cultural similarity between two agents
    ## O(n) complexity
    def getCulturalSimilarity(self, otherAgent: AxelrodAgent):
        assert(len(self.culture)==len(otherAgent.culture))
        acc = 0
        for i in range(len(self.culture)):
            acc += int(self.culture[i]==otherAgent.culture[i])
        return acc/len(self.culture)
    
    ## Identify the indices two culture vectors differ
    ## O(n) complexity
    def culturePositionDifferenceLocations(self, otherAgent: AxelrodAgent):
        assert(len(self.culture)==len(otherAgent.culture))
        acc = []
        for i in range(len(self.culture)):
            if self.culture[i] != otherAgent.culture[i]:
                acc.append(i)
        return acc
    
