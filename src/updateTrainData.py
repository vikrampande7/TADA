"""
@author: Vikram Pande
Remove specific ARFs from existing
"""

import pandas as pd

# Load two data files
arf_loci = pd.read_csv("TADA\data\ARF Gene Loci.csv")
train_data = pd.read_csv('TADA\data\TrainingsData.csv')

print(train_data.shape)

# list of ARFs to be removed
arfsRemove = arf_loci['Locus'].to_list()

# Function to remove ARFs
def remove_arfs(arfs_list, df):
    """
    Input:
        arfs_list: (List) List of ARF names to be removed in new data
        df: (pd.DataFrame) Training Data DataFrame
    Returns:
        df: (pd.DataFrame) Updated DataFrame with removed ARFs
    """
    for i,value in enumerate(arfs_list):
        print(f"Deleting {i}:{value}")
        df = df[~df['Name'].str.startswith(value)]

    return df

# Updated Training Data
updated_data = remove_arfs(arfsRemove, train_data)
print(updated_data.shape)

updated_data.to_csv('TADA\data\TrainingsDataV2.csv')
