from datetime import datetime
import csv
import time
import random
import math
import numpy as np
import asciichartpy

from rich import print
from rich import box
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich.layout import Layout 
from rich.table import Table

from rich.live import Live
from rich.prompt import Prompt
from rich.progress import track
from rich.progress import Progress

from rich.traceback import install
install(show_locals=True)

# # Function to generate sinusoidal wave data
# def generate_wave_data(num_points, amplitude, frequency, phase_shift):
#     data = []
#     for i in range(num_points):
#         value = amplitude * math.sin(2 * math.pi * frequency * i / num_points + phase_shift)
#         data.append(value)
#     return data

# # Generate product metric data
# num_points = 35  # Number of data points

# # Define the characteristics of the wave
# amplitude = 50
# frequency = 0.1
# phase_shift = 0

# product_data = {"Metric": generate_wave_data(num_points, amplitude, frequency, phase_shift)}

# # Print product metrics graph
# graph_data = [product_data[metric] for metric in product_data]

# graph = asciichartpy.plot(graph_data, {'height': 20})
# panel = f"[bold]Product Metrics Tracking[/bold]\n\n{graph}"

# # Append metric values to the panel
# for metric, values in product_data.items():
#     panel += f"\n{metric}: {values[-1]:.2f}"

# print(panel)


s1 = []
s2 = []
s3 = []

for i in range(120):
    s1.append(15 * math.cos(i * ((math.pi * 8) / 120)))  # values range from -15 to +15
    s2.append(10 * math.sin(i * ((math.pi * 4) / 120)))  # values range from -10 to +10
    s3.append(8 * math.sin(i * ((math.pi * 12) / 120)))  # values range from -8 to +8

data = [s1, s2, s3]
graph = asciichartpy.plot(data, {'height': 15})  # rescales the graph to ±3 lines
print(Panel(graph, border_style = "Bold white", box = box.SQUARE, title = "Product Sales Analysis", title_align="left"))