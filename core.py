import csv
import openpyxl

def read_xlsx(file_name):
    # with open(file_name,'r',encoding="Latin-1",newline='') as f:
    #     #encoding with 'utf-8' causes 'UnicodeDecodeError, invalid continuation byte' error. 
    #     #'For NBA__WNBA_Daily_Stats.xlsx', 'latin-1' is used to encode.
    #     reader = csv.DictReader(f)
    #     # print(reader)
    #     for row in reader:
    #         print(row)

    wb = openpyxl.load_workbook(file_name) 
    #get names of all tabs in the spreadsheet
    tab_names_list = wb.sheetnames
    #return the worksheet objects for each of those names
    worksheets = []
    for tab_name in tab_names_list:
        worksheets.append(wb.get_sheet_by_name(tab_name))

    #return worksheet objects which then feeds into filter_stats_from_worksheets
    return {'NBA': worksheets[0], 'WNBA': worksheets[1]}

def filter_stats_from_worksheets(worksheets_dict):
    
    NBA_emails = 0
    NBA_chats = 0
    WNBA_emails = 0

    for row in worksheets_dict['NBA'].iter_rows(values_only=True):
        for item in row:
            if 'Email' == item:
                NBA_emails += int(float(row[2]))
            elif 'Web' == item:
                NBA_emails += int(float(row[2]))
            elif 'WhatsApp' == item:
                NBA_emails += int(float(row[2]))
            elif 'Messaging' == item:
                NBA_chats += int(float(row[2]))

    print(str(NBA_emails) + ', ' + str(NBA_chats))

    
    print('WNBA:')
    for row in worksheets_dict['WNBA'].iter_rows(values_only=True):
        for item in row:
            if 'SUM' == item:
                WNBA_emails += int(float(row[2]))
                break
                # break as there are two 'SUM' items in the row (don't want to add twice)

    print(str(WNBA_emails))

    return {'NBA - email': NBA_emails, 'NBA - chat': NBA_chats, 'WNBA - email': WNBA_emails}

def create_csv(rows_dict):
    print(rows_dict)
    f = open(f'NBA_WNBA_Stats.csv','w',encoding="utf-8", newline='')

    field_names = ['NBA - email', 'NBA - chat', 'WNBA - email']

    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()

    writer.writerow({'NBA - email': rows_dict['NBA - email'], 'NBA - chat': rows_dict['NBA - chat'], 'WNBA - email': rows_dict['WNBA - email']})
    f.close()
