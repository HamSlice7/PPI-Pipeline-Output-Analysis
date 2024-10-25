import pandas as pd
import sys
import os

file = sys.argv[1]
file_name = os.path.basename(file)
file_name = os.path.splitext(file_name)
file_name = file_name[0]
df = pd.read_csv(file)


def get_max(data: pd.DataFrame) -> pd.DataFrame: 

    """
    Return a data frame of the max ipTM, LIS, and LIA value from each predicted complex
    
    Parameters:
        - data (pd.DataFrame): Data frame output from PPI pipeline 
    
    Return:
        Max ipTM, LIS, and LIA value from each complex (pd.DataFrame)
    
    """

    df = data

    #Get the max ipTM, LIS, and LIA from each complex (5 predictions for each complex) and save them as individual data frames
    df_iptm_max = df.groupby(["Protein 1", "Protein 2"])["ipTM"].max().reset_index()
    df_lis_max = df.groupby(["Protein 1", "Protein 2"])["LIS"].max().reset_index()
    df_lia_max = df.groupby(["Protein 1", "Protein 2"])["LIA"].max().reset_index()

    #Merge the max ipTM, LIS, and LIA data frames together
    combined_df = pd.merge(df_iptm_max,df_lis_max, on = ["Protein 1", "Protein 2"])
    combined_df = pd.merge(combined_df,df_lia_max, on = ["Protein 1", "Protein 2"] )
    
    #Save the combined data frame to a csv file
    combined_df.to_csv(f"{file_name}_max.csv", index=False)

    return combined_df


get_max(df)