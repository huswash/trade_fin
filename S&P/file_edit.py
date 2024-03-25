from glob import glob
import pandas as pd
from pathlib import Path

# Get the date from the file name
files = glob('/path/  *.txt')
for file in files:
    file_date = file.split('/')[-1].strip('TP-REPORT-').rstrip('.txt')
    my_date = pd.to_datetime(file_date, format='%d-%m-%Y')
    new_date = my_date.strftime('%Y-%m-%d')
    new_filename = file.replace(file_date, new_date)
    Path(file).rename(Path(new_filename))
    break
