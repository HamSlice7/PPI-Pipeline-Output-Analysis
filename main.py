import pandas as pd
import sys 
import os
import get_max
import get_mean
import filtering_output_max
import filtering_output_mean

data = sys.argv[1]
file_name = os.path.basename(data)
file_name = os.path.splitext(file_name)
file_name = file_name[0]
df = pd.read_csv(data)

#Getting the max and mean values for each complex in the output.
max_df = get_max.get_max(df)
mean_df = get_mean.get_mean(df)

#Saving the max and mean data frame as a csv file.
max_df.to_csv(f"{file_name}_max.csv", index=False)
mean_df.to_csv(f"{file_name}_mean.csv", index = False)

#Filtering the max data frame based on a LIS + LIA threshold and creating a new data frame.
max_df_LIS_LIA_threhsold = filtering_output_max.filtering_max_LIS_LIA(max_df, 0.203, 3432)
#Filtering the max data frame based on a ipTM threshold and creating a new data frame.
max_df_iptm_threshold = filtering_output_max.filtering_max_ipTM(max_df, 0.7)

#Saving the max LIS + LIA and max ipTM filtered data frames to csv files.
max_df_LIS_LIA_threhsold.to_csv(f"{file_name}_filtered_LIS_LIA_max.csv", index=False)
max_df_iptm_threshold.to_csv(f"{file_name}_filtered_iptm_max.csv", index = False)

#Filtering the mean data frame based on a LIS + LIA threshold and creating a new data frame.
mean_df_LIS_LIA_threshold = filtering_output_mean.filtering_mean_LIS_LIA(mean_df, 0.073, 1610)
#Filtering the mean data frame based on a ipTM threshold and creating a new data frame.
mean_df_iptm_threshold = filtering_output_mean.filtering_mean_ipTM(mean_df, 0.6)

#Saving the mean LIS + LIA and mean ipTM filtered data frames to csv files.
mean_df_LIS_LIA_threshold.to_csv(f"{file_name}_filtered_LIS_LIA_mean.csv", index=False)
mean_df_iptm_threshold.to_csv(f"{file_name}_filtered_iptm_mean.csv", index = False)