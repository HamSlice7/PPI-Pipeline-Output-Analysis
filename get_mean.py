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
    metric_columns = ["LIS", "LIA", "ipTM", "pTM", "AFM Confidence", "pLDDT", "Distances", "SASA", "Change in SASA", "MSA_depth_inhibitors", "MSA_depth_peptidase"]

    #Group the pipeline data by "Protein 1" and "Protein 2" and then take the means of the groups based on the specified columns in the "metric_columns" list
    df_complex_mean = data.groupby(["Protein 1", "Protein 2"])[metric_columns].mean().reset_index()
    
    df_complex_mean.rename(columns={"LIS": "Mean LIS",
                                    "LIA" : "Mean LIA", 
                                    "ipTM": "Mean ipTM", 
                                    "pTM":"Mean pTM", 
                                    "AFM Confidence":"Mean AFM Confidence", 
                                    "pLDDT": "Mean pLDDT", 
                                    "Distances" : "Mean Distance", 
                                    "SASA":"Mean SASA",
                                    "Change in SASA":"Mean Change in SASA",
                                    "MSA_depth_inhibitors":"Mean MSA_depth_inhibitor",
                                    "MSA_depth_peptidase":"Mean MSA_depth_peptidase"}, inplace=True)
    

    df_complex_sd = data.groupby(["Protein 1", "Protein 2"])[metric_columns].std().reset_index()

    df_complex_sd.rename(columns={"LIS": "SD LIS",
                                  "LIA":"SD LIA", 
                                  "ipTM": "SD ipTM", 
                                  "pTM":"SD pTM", 
                                  "AFM Confidence":"SD AFM Confidence", 
                                  "pLDDT": "SD pLDDT", 
                                  "Distances" : "SD Distance", 
                                  "SASA":"SD SASA",
                                  "Change in SASA":"SD Change in SASA",
                                  "MSA_depth_inhibitors":"SD MSA_depth_inhibitor",
                                  "MSA_depth_peptidase":"SD MSA_depth_peptidase"}, inplace=True)

    df_mean_sd = pd.merge(df_complex_mean, df_complex_sd, on=["Protein 1", "Protein 2"])
    
    df_mean_sd = df_mean_sd.loc[:,['Protein 1',
                                   'Protein 2',
                                   'Mean LIS',
                                   'SD LIS',
                                   'Mean LIA',
                                   'SD LIA',
                                   'Mean ipTM',
                                   'SD ipTM',
                                   'Mean pTM',
                                   'SD pTM',
                                   'Mean AFM Confidence',
                                   'SD AFM Confidence',
                                   'Mean pLDDT',
                                   'SD pLDDT',
                                   'Mean Distance',
                                   'SD Distance',
                                   'Mean SASA',
                                   'SD SASA',
                                   'Mean Change in SASA',
                                   'SD Change in SASA',
                                   'Mean MSA_depth_inhibitor',
                                   'SD MSA_depth_inhibitor']]
    print(df_mean_sd.head())


    return df_mean_sd


        