"""
Implementation of Axelrod 1997
Agentic Modeling - Midterm 2
©2026 Eliora Hansonbrook

app.py
"""

from model import AxelrodModel
import numpy as np
from mesa.visualization import Slider, SolaraViz, make_plot_component
from mesa.visualization.components.matplotlib_components import make_mpl_space_component
from mesa.visualization.components import AgentPortrayalStyle, PropertyLayerStyle

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="#" + agent.getCultureNumber_string() + "5",
        edgecolors=agent.outline,
        size=250,
        marker="o",
    )

def propertylayer_portrayal(layer):
    return PropertyLayerStyle(

    )


state_space = make_mpl_space_component(
    agent_portrayal=agent_portrayal,
    propertylayer_portrayal=propertylayer_portrayal,
    post_process=None,
    draw_grid=False,
)

## Define variable model parameters
model_params = {
    #Dictionary Format
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
    ],
    model_params=model_params,
    name="Axelrod Replication",
    play_interval=1,
    render_interval=100,
)