import pandas as pd
import sys 
import os

data_max = sys.argv[1]
file_name_max = os.path.basename(data_max)
file_name_max = os.path.splitext(file_name_max)
file_name_max = file_name_max[0]
df_max = pd.read_csv(data_max)


def filtering_max_LIS_LIA(df: pd.DataFrame, LIS: int, LIA: int) -> pd.DataFrame:
    """
    Filter the maximum LIS and LIA of the 5 replicates for each complex based on a user defined threshold

    Parameters:
        - df: Pandas data frame representing the maximum LIS and LIA of the 5 replicates for each complex
        - LIS: LIS value for filtering probable binary interactions
        - LIA: LIA value for filtering probable binary interactions
    
    Return: 
        - The filtered data frame containing rows that pass the LIA + LIS thresholds
    """
    max_df_filter_LIS_LIA = df.loc[(df["LIS"] >= LIS) & (df["LIA"] >= LIA)]
    return max_df_filter_LIS_LIA

filtering_max_LIS_LIA(df_max, 0.203, 3432).to_csv(f"{file_name_max}_filtered_LIS_LIA_max.csv", index=False)  


def filtering_max_ipTM(df: pd.DataFrame, ipTM:int) -> pd.DataFrame:
    """
    Filter the maximum ipTM values of the 5 replicates for each complex based on a user defined threshold

    Parameters:
        - df: Pandas data frame representing the maximum LIS and LIA of the 5 replicates for each complex
        - ipTM: ipTM value for filtering probable binary interactions
    
    Return: 
        - The filtered data frame containing rows that pass the ipTM threshold

    """
    max_df_filter_iptm = df[df["ipTM"] >= ipTM]
    return max_df_filter_iptm

filtering_max_ipTM(df_max, 0.7).to_csv(f"{file_name_max}_filtered_ipTM_max.csv", index=False)