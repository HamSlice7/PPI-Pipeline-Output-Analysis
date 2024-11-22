import pandas as pd
import sys 
import os


data_mean = sys.argv[1]
file_name_mean = os.path.basename(data_mean)
file_name_mean = os.path.splitext(file_name_mean)
file_name_mean = file_name_mean[0]
df_mean = pd.read_csv(data_mean)


def filtering_mean_LIS_LIA(df: pd.DataFrame, LIS: int, LIA: int):
    """
    Filter the mean LIS and LIA of the 5 replicates for each complex based on a user defined threshold

    Parameters:
        - df: Pandas data frame representing the mean LIS and LIA of the 5 replicates for each complex
        - LIS: LIS value for filtering probable binary interactions
        - LIA: LIA value for filtering probable binary interactions
    
    Return: 
        - The filtered data frame containing rows that pass the LIA + LIS thresholds
    """
    mean_df_filter_LIS_LIA = df.loc[(df["Mean LIS"] >= LIS) & (df["Mean LIA"] >= LIA)]
    mean_df_filter_LIS_LIA.to_csv(f"{file_name_mean}_filtered_LIS_LIA_mean.csv", index=False)
    return mean_df_filter_LIS_LIA



def filtering_mean_ipTM(df: pd.DataFrame, ipTM:int):
    """
    Filter the mean ipTM values of the 5 replicates for each complex based on a user defined threshold

    Parameters:
        - df: Pandas data frame representing the mean LIS and LIA of the 5 replicates for each complex
        - ipTM: ipTM value for filtering probable binary interactions
    
    Return: 
        - The filtered data frame containing rows that pass the ipTM threshold
    """
    mean_df_filter_iptm = df[df["Mean ipTM"] >= ipTM]
    return mean_df_filter_iptm
