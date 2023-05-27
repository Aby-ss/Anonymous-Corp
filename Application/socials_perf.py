from datetime import datetime
import csv
import time
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

# Instagram API credentials
access_token = "YOUR_ACCESS_TOKEN"
instagram_business_account_id = "YOUR_BUSINESS_ACCOUNT_ID"

# Function to get Instagram account metrics
def get_instagram_metrics():
    endpoint = f"https://graph.facebook.com/v13.0/{instagram_business_account_id}?fields=followers_count,media_count&access_token={access_token}"
    response = requests.get(endpoint)
    data = response.json()
    followers = data.get("followers_count")
    posts = data.get("media_count")
    return followers, posts

# Get Instagram account metrics
followers, posts = get_instagram_metrics()

# Print metrics
panel = f"[bold]Instagram Account Metrics[/bold]\n\nFollowers: {followers}\nPosts: {posts}"
print(panel)
