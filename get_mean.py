import pandas as pd
import sys
import os

file = sys.argv[1]
file_name = os.path.basename(file)
file_name = os.path.splitext(file_name)
file_name = file_name[0]
df = pd.read_csv(file)

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
    df = data

    #Create a list of the metrics that will be used for averages
    metric_columns = ["LIS", "LIA", "ipTM", "pTM", "AFM Confidence", "pLDDT", "MSA_depth_peptidase", "MSA_depth_inhibitors"]

    #Group the pipeline data by "Protein 1" and "Protein 2" and then take the means of the groups based on the specified columns in the "metric_columns" list
    df_complex_mean = df.groupby(["Protein 1", "Protein 2"])[metric_columns].mean().reset_index()

    #Save df_complex_mean to a csv file
    df_complex_mean.to_csv(f"{file_name}_mean.csv", index=False)

    return df_complex_mean

get_mean(df)

        