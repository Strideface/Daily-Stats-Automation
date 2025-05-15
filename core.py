import csv
import openpyxl


def read_NBA_WNBA(file_name):

    wb = openpyxl.load_workbook(file_name) 
    #get names of all tabs in the spreadsheet
    tab_names_list = wb.sheetnames
    #return the worksheet objects for each of those names
    worksheets = []
    for tab_name in tab_names_list:
        worksheets.append(wb.get_sheet_by_name(tab_name))

    #return worksheet objects which then feeds into filter_NBA_WNBA
    return {'NBA': worksheets[0], 'WNBA': worksheets[1]}


def read_daily_stats(file_name):

    wb = openpyxl.load_workbook(file_name) 
    #get names of all tabs in the spreadsheet
    tab_names_list = wb.sheetnames
    #return the worksheet objects for each of those names
    worksheets = []
    for tab_name in tab_names_list:
        worksheets.append(wb.get_sheet_by_name(tab_name))

    #return worksheet objects which then feeds into filter_daily_stats
    return {'Current Backlog': worksheets[0], 'Daily Support Contacts': worksheets[1], 
            'Previous Day P1P2 Ticket...': worksheets[2]} 


def filter_NBA_WNBA(worksheets_dict):
    
    NBA_emails = 0
    NBA_chats = 0
    WNBA_emails = 0

    #iterate through the items in the rows to add up values of emails and seperate them from chats
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

    #same as above but only need the total figure ('SUM')
    for row in worksheets_dict['WNBA'].iter_rows(values_only=True):
        for item in row:
            if 'SUM' == item:
                WNBA_emails += int(float(row[2]))
                break
                # break as there are two 'SUM' items in the row (don't want to add twice)

    #feeds into the creation of a new csv file function
    return {'NBA - email': NBA_emails, 'NBA - chat': NBA_chats, 'WNBA - email': WNBA_emails}


def filter_daily_stats(worksheets_dict):

    for row in worksheets_dict['Current Backlog'].iter_rows(values_only=True):
        print(row)

    for row in worksheets_dict['Daily Support Contacts'].iter_rows(values_only=True):
        print(row)

    for row in worksheets_dict['Previous Day P1P2 Ticket...'].iter_rows(values_only=True):
        print(row)

    return


def create_csv(rows_dict):
    print(rows_dict)
    f = open(f'NBA_WNBA_Stats.csv','w',encoding="utf-8", newline='')

    field_names = ['NBA - email', 'NBA - chat', 'WNBA - email']

    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()

    writer.writerow({'NBA - email': rows_dict['NBA - email'], 'NBA - chat': rows_dict['NBA - chat'], 'WNBA - email': rows_dict['WNBA - email']})
    f.close()
