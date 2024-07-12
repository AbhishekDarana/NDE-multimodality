"""Abhishek Darana- Driver code to locate RAW data and convert to csvs and plot images and config files for identified rebars(example of processed data is in sample data folder)"""
import sys
import glob
sys.path.append('C:/directory/path/downloaded_py_files/')
import GPR_locate_rebars as gpr_lr
import warnings
import os
warnings.filterwarnings('ignore')
# Save DZT into CSV files
downloaded_path = r"C:\Users\Abhishek\Documents\Summer_research\CHARISMA-main\ground-penetrating-radar\Rebar corrosion\data\GPR Zone 04\csv"
folder_path=os.path.join(downloaded_path,"formatted_data")
print(folder_path)
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
data_list=glob.glob(os.path.join(downloaded_path,"data*.csv"))
ultimate_list=[]
for i in data_list:
    val=i.split(".csv")[0]
    if os.path.exists(os.path.join(downloaded_path,"config"+val[-1]+".csv")):
        ultimate_list.append(i)
# df1, df2 = gpr_lr.readdzt(os.path.join(downloaded_path,'Mississippi_bridge_data.DZT'))
# gpr_lr.save_to_csv(df1, downloaded_path, 'data')
# gpr_lr.save_to_csv(df2, downloaded_path, 'config', True, True)

for i in ultimate_list:
    # Read saved CSV file
    # df_1, df_2 = gpr_lr.read_csv(downloaded_path)
    # user_directory = "C:/directory/path/"
    suffix=os.path.basename(i.split(".csv")[0])
    df_1, df_2 = gpr_lr.read_csv(i)
    result_variables = gpr_lr.config_to_variable(df_2)
    locals().update(result_variables)
    # Outlier removal through IQR
    IQR_df_1 = gpr_lr.Interquartile_Range(df_1, min_value=0.10, max_value=0.95, multiplier=1.5)
    # Split the DataFrame (too long column)
    clipped_df_chunk=gpr_lr.data_chunk(IQR_df_1)
    # Apply power gain 
    gpr_data_powered = gpr_lr.gain(clipped_df_chunk[0], type="pow", alpha=0.4, t0=120)
    # Apply trinomial dewow function
    dewowed_ar = gpr_lr.dewow(gpr_data_powered)
    # Apply scan-by-scan time-zero correction
    time0df, rh_nsamp = gpr_lr.Timezero_individual(dewowed_ar, rhf_position, rhf_range)
    migrated_df, profilePos, dt, dx, velocity = gpr_lr.FK_migration(time0df, rhf_spm, rhf_sps, rhf_range, rh_nsamp, rhf_espr=11)
    gpr_lr.locate_rebar_consecutive(folder_path,suffix,migrated_df, velocity, rhf_range, rh_nsamp, profilePos, vmin=0.15, vmax=0.7, amplitude_threshold=0.53, depth_threshold=8, minimal_y_index=90, num_clusters=11, random_state=42, redundancy_filter=0.6)