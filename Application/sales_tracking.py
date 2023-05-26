from datetime import datetime
import csv
import time
import random
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

# # Print sales graph
# while True:
#     graph = asciichartpy.plot(sales_data, {'height': 20})
#     panel = f"[bold]Product Sales Tracking[/bold]\n\n{graph}"
#     print(Panel(panel))
#     time.sleep(1)  # Wait for 1 second before updating the graph



# Function to generate random sales data
def generate_sales_data(num_points):
    sales_data = []
    sales = 1000  # Initial sales value
    for _ in range(num_points):
        change = random.randint(-100, 100)  # Generate random sales change
        sales += change
        sales_data.append(sales)
    return sales_data

# Generate sales data
num_points = 50  # Number of data points
sales_data = generate_sales_data(num_points)

# Print sales graph
graph = asciichartpy.plot(sales_data, {'height': 20})
panel = f"[bold]Product Sales Tracking[/bold]\n\n{graph}"
print(Panel(panel, border_style = "bold white", box = box.SQUARE))