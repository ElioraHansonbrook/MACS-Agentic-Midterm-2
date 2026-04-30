"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

app.py
"""

from model import AxelrodModel
from mesa.visualization import Slider, SolaraViz, make_plot_component
from mesa.visualization.components.matplotlib_components import make_mpl_space_component
from mesa.visualization.components import AgentPortrayalStyle, PropertyLayerStyle

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        x=agent.cell.coordinate[0],
        y=agent.cell.coordinate[1],
        color="red",
        marker="Hi",
        size=20,
        zorder=2,
        alpha=0.8,
        edgecolors="black",
        linewidths=1.5
    )


state_space = make_mpl_space_component(
    #agent_portrayal=agent_portrayal,
    #propertylayer_portrayal=propertylayer_portrayal,
    post_process=None,
    draw_grid=False,
)

## Define variable model parameters
model_params = {
    #Dictionary Format
}

##Instantiate model
model = AxelrodModel(seed=54)

# Define all aspects of page
page = SolaraViz(
    model,
    components=[
        #state_space,
        # Plots
    ],
    model_params=model_params,
    name="Axelrod Replication",
    play_interval=150,
)
# Return page
page