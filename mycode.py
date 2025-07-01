import pandas as pd
import os

# create a sample Dataframe with column names

data = {'Name' : ['Alice','bob','Charlie'],
        'Age' : [25,30,35],
        'City' : ['New York','Los Angeles','Chicago']}

df = pd.DataFrame(data)

# Ensure the "data" directory exists at root level
data_dir = 'data'
os.makedirs(data_dir,exist_ok = True)

# Define the file path
file_path = os.path.join(data_dir,'sample_data.csv')

# Save the dataframe to a csv file,including column names
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")

