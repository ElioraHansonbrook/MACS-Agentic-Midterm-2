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
    
    ## An initial implementation for getting an integer representing culture from the culture vector
    def getCultureNumber_string(self):
        return f"{self.culture[0]}{self.culture[1]}{self.culture[2]}{self.culture[3]}{self.culture[4]}"

    ## An O(1), presumed high speed implementation of calculating the culture number
    def getCultureNumber_int(self):
        return self.culture[0]*10**4 * self.culture[0]*10**3 * self.culture[0]*10**2 * self.culture[0]*10**1 * self.culture[0]*10**0

    ## Calculate the degree of cultural similarity between two agents
    def getCulturalSimilarity(self, otherAgent: AxelrodAgent):
        assert(len(self.culture)==len(otherAgent.culture))
        acc = 0
        for i in range(0,len(self.culture)-1):
            acc += int(self.culture[i]==otherAgent.culture[i])
        return acc/len(self.culture)

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
    
