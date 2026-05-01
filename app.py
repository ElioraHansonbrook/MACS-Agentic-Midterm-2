"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

app.py
"""

# Imports
from model import AxelrodModel
import numpy as np
from mesa.visualization import Slider, SolaraViz, make_plot_component
from mesa.visualization.components.matplotlib_components import make_mpl_space_component
from mesa.visualization.components import AgentPortrayalStyle, PropertyLayerStyle

## Set the agent portrayal
def agent_portrayal(agent):
    return AgentPortrayalStyle(
        # Set the color based on cultural traits
        # The trailing five fills the sixth digit in a hexadecimal string
        color="#" + agent.getCultureNumber_string() + "5"
    )

## Set the property layer portrayal
def propertylayer_portrayal(layer):
    return PropertyLayerStyle(
        # Just vanilla property layer portrayal here
    )

# Create a plot of the number of groups
groupsCountPlot = make_plot_component("same")

# The space in which the model is visualized
state_space = make_mpl_space_component(
    agent_portrayal=agent_portrayal,
    propertylayer_portrayal=propertylayer_portrayal,
    post_process=None,
    draw_grid=False,
)

## Define variable model parameters
model_params = {
    # Dictionary Format
    # Added these controls just for fun; not in Axelrod's core description
    # But these variables were supplied by Axelrod to the model
    # So there is some relation to the paper.
    "width": Slider("Space Width", value=10, min=10, max=100, step=1),
    "height": Slider("Space Height", value=10, min=10, max=100, step=1),
}

##Temporary variable - random number generator seed
rngSeed = 2304
##Instantiate model
model = AxelrodModel(rng=np.random.default_rng(rngSeed))

# Define all aspects of page
page = SolaraViz(
    model,
    components=[
        state_space,
        # Plots
        groupsCountPlot,
    ],
    model_params=model_params,
    name="Axelrod Replication",
    play_interval=1,
    render_interval=100,
)