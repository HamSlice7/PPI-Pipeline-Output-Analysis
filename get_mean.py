import pandas as pd


def get_mean(data: pd.DataFrame) -> pd.DataFrame:

    """
    Return a data frame of the mean values of for ipTM, LIS, LIA, pTM, AF Confidience (0.8*ipTM + 0.2*pTM)
    and pLDDT for the 5 predicted structures for each complex 

    Parameters:
        - csv_file (pd.DataFrame): Data frame output from PPI pipeline 

    Return:
        - Mean ipTM, LIS, LIA, pTM, AF Confidience (0.8*ipTM + 0.2*pTM)
          and pLDDT values from each complex.

    """

    #assign the pipeline output data to the variable 'df'
    

    #Create a list of the metrics that will be used for averages
    metric_columns = ["LIS", "LIA", "ipTM", "pTM", "AFM Confidence", "pLDDT", "Distances", "SASA", "Change in SASA", "MSA_depth_inhibitors", "MSA_depth_peptidase", "Peptidase active site"]

    #Group the pipeline data by "Protein 1" and "Protein 2" and then take the means of the groups based on the specified columns in the "metric_columns" list
    df_complex_mean = data.groupby(["Protein 1", "Protein 2"])[metric_columns].mean().reset_index()

    return df_complex_mean


        