import os
import glob, csv, time
import re

example_data_dir = os.path.join('..','exercises','exercise-8-data','*.*') # TODO: limit to just CSV files

# Loop through all of the files that match the path pattern
for csv_path in glob.glob(example_data_dir):
    print("Processing {path}".format(path=csv_path))

    # Good luck
