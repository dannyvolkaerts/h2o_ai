# %%
import pandas as pd
import h2o

# Read the seeds.csv file into a pandas dataframe
df = pd.read_csv('seeds.csv')

# Display the first few rows of the dataframe
print(df.head())
# %%
# initialise h2o cluster
h2o.init()
# Prepare the data for modelling


# %%
# Split the dataset in training, validation and testset


#%%
# Train a decision tree and show the tree


#%% 
# Check the model performance on the testset

#%% 
# Now we will train a GBM model but set the hyperparameters
# as given in the slides (make use of a grid and train the models)

# Extract the best model and show the performance

#%% 
# Now let's automate this with autoML
# set the max runtime on 5 minutes

#%% 
# Check the leaderboard

# Is the overall performance of the model better than the manual search?