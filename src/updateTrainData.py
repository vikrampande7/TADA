"""
@author: Vikram Pande
Remove specific ARFs from existing
"""

import pandas as pd
import copy

# Load two data files
arf_loci = pd.read_csv("TADA\data\ARF Gene Loci.csv")
train_data = pd.read_csv('TADA\data\TrainingsData.csv')

print(train_data.shape)

# list of ARFs to be removed
arfsRemove = arf_loci['Gene Name'].to_list()
arfsRemove_copy = copy.deepcopy(arfsRemove)
arfsRemove_copy.append('PPARF')

print(f"L1: {len(arfsRemove)}")
print(f"L2: {len(arfsRemove_copy)}")

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
        df = df[~df['Name'].str.contains(value)]
    print("--Done--")

    return df

# Updated Training Data
updated_data = remove_arfs(arfsRemove, train_data)
updated_data_ = remove_arfs(arfsRemove_copy, train_data)
print(updated_data.shape)
print(updated_data_.shape)

# Remove index column
# updated_data_.drop(columns=updated_data_.columns[0], axis=1, inplace=True)

updated_data.to_csv('TADA\data\TrainingsDataV2_.csv')
updated_data_.to_csv('TADA\data\TrainingsDataV2.csv')
