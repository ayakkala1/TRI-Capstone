
#Utility to download files from wwww.batteryarchive.org Created on 08/30/2020.
#For questions, email info@batteryarchive.org

#given a metadata file in csv format, generate the links and download cycle data and time series data
#cycle data file format: http://www.batteryarchive.org/data/[data_set]/[cell_id]_cycle_data.csv
#time data file format http://www.batteryarchive.org/data/[data_set]/[cell_id]_timeseries.csv
#files are downloaded to the folder that contains the csv and python file

import pandas as pd
import requests
import sys


def get_file(path, save_to_file_name):
    print (path)
    req = requests.get(path)
    url_content = req.content
    print (save_to_file_name)
    csv_file = open(save_to_file_name, 'wb')

    csv_file.write(url_content)
    csv_file.close()


data_set = 'snl'
prefix = "http://www.batteryarchive.org/data/"
try:
    df_snl = pd.read_csv("./" + data_set + ".csv")
    print(df_snl)

    number_of_cells = str(len(df_snl))

    for ind in df_snl.index:
        cell_id = df_snl['cell_id'][ind]
        file_name = cell_id.replace("/", "-")

        print(str(ind+1) + " of " + number_of_cells + ": Cycle data cell_id: " + cell_id)
        cycle_data = prefix + file_name + "_cycle_data.csv"
        get_file(cycle_data, file_name + "_cycle_data.csv")

        print(str(ind+1) + " of " + number_of_cells + ": Time data cell_id: " + cell_id)
        time_data = prefix + file_name + "_timeseries.csv"
        get_file(time_data, file_name + "_timeseries.csv")

    print("Done downloading files. Thank you for using www.batteryarchive.org")
    print("For questions on how to add your data, contact info@batteryarchive.org")


except OSError as e:
    print("Error reading data_set: " + str(e))
    print("please send the complete message to info@batteryarchive.org")

except:
    print("Unexpected error: ", sys.exc_info()[0])
    print("please send the complete message to info@batteryarchive.org")


