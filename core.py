import csv

def read_csv(csv_name):
    with open(csv_name,'r',encoding='latin-1',newline='') as f:
        #encoding with 'utf-8' causes 'UnicodeDecodeError, invalid continuation byte' error. 
        #'For NBA__WNBA_Daily_Stats.xlsx', 'latin-1' is used to encode.
        print(f.read())