import pandas as pd




def get_max(data: pd.DataFrame) -> pd.DataFrame: 

    """
    Return a data frame of the max ipTM, LIS, and LIA value from each predicted complex
    
    Parameters:
        - data (pd.DataFrame): Data frame output from PPI pipeline 
    
    Return:
        Max ipTM, LIS, and LIA value from each complex (pd.DataFrame)
    
    """


    #Get the max ipTM, LIS, and LIA from each complex (5 predictions for each complex) and save them as individual data frames
    df_iptm_max = data.groupby(["Protein 1", "Protein 2"])["ipTM"].max().reset_index()
    df_lis_max = data.groupby(["Protein 1", "Protein 2"])["LIS"].max().reset_index()
    df_lia_max = data.groupby(["Protein 1", "Protein 2"])["LIA"].max().reset_index()

    #Merge the max ipTM, LIS, and LIA data frames together
    combined_df = pd.merge(df_iptm_max,df_lis_max, on = ["Protein 1", "Protein 2"])
    combined_df = pd.merge(combined_df,df_lia_max, on = ["Protein 1", "Protein 2"] )

    return combined_df

