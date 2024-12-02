# %%
import pandas as pd
import dtale

# Import necessary libraries

# Load your dataset
# Replace 'your_dataset.csv' with the path to your dataset
df = pd.read_csv('seeds.csv')

# Start D-Tale to profile the data
d = dtale.show(df)
d.open_browser()
# %%
