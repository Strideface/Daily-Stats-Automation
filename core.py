import csv
import openpyxl
from B2B_clients import B2B_clients_dict
from B2C_clients import B2C_clients_dict


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

    #feeds into filter_daily_stats in order to combine the NBA and WNBA stats
    return {'NBA - email': NBA_emails, 'NBA - chat': NBA_chats, 'WNBA - email': WNBA_emails}


def filter_daily_stats(worksheets_dict, *NBA_WNBA_dict):
    #*args for now until this function is finished then it will need to be passed in always

    # print('Backlog: \n')
    # for row in worksheets_dict['Current Backlog'].iter_rows(values_only=True):
    #     print(row)

    #NEW:
    print('\n New \n')
    #seperate B2B from B2C tickets
    B2B = []
    B2C = []
    for row in worksheets_dict['Daily Support Contacts'].iter_rows(values_only=True):
        print(row)
        if row[0] == 'B2B':
            B2B.append(row)
        elif row[0] == 'B2C':
            B2C.append(row)


    print('\n B2B \n')
    print(B2B)
    #B2B New:

    #make new copy of B2B_clients_dict
    B2B_email = B2B_clients_dict.copy()
    #for every client name (row[2], find it in B2B_email and replace the original value (0) with the ticket count value (row[-1] - 'SUM'))
    for row in B2B: 
        try: 
            B2B_email[row[2]] = int(row[-1])
        except KeyError:
            print(f'KeyError thrown for {row[2]} (May not exist in B2B_clients_dict)')
            continue
    #for every client in the B2B_clients_dict, check if they are in the B2B list
    #if they are, add them to the new dict with the ticket count
    #else, add them to the new dict with a value of 0
    # for client in B2B_clients_dict.values():
    #     if client == B2B[x][2]:
    #         # print(client)
    #         B2B_email[client] = int(B2B[x][-1])
    #         x += 1
    #     else:
    #         B2B_email[client] =  0

    print('\n B2B_email \n')
    print(B2B_email)
    print(len(B2B_email))

    print('\n B2C \n')
    print(B2C)

    #B2C New:

    #Same process as above but also combine the NBA and WNBA stats AND seperate emails from chats

    #Emails:
    B2C_email = B2C_clients_dict.copy()
    for row in B2C: 
        try:          
            if isinstance(row[3], float):
                B2C_email[row[2]] += int(row[3])
            if isinstance(row[5], float):
                B2C_email[row[2]] += int(row[5])
            if isinstance(row[7], float):
                B2C_email[row[2]] += int(row[7])
        except KeyError:
            print(f'KeyError thrown for {row[2]} (May not exist in B2C_clients_dict)')
            continue

        #in order to add Any Channel, Email and Web values together.
        #need to check if the value is a float (e.g. 1.0) first as if the value is nothing
        #it's actually an empty string (e.g. '') and will throw an error if you try operate.

    print('\n B2C_email \n')
    print(B2C_email)
    print(len(B2C_email))

    
    # print('\n P1-P2 \n')
    # for row in worksheets_dict['Previous Day P1P2 Ticket...'].iter_rows(values_only=True):
    #     print(row)

#return a dictionary with the key representing each tab name for the new csv file and the value a dict
#with the field name and row values for those tabs.
#The csv file replicates the layout of the 'Daily Team Stats' spreadsheet (The tabs with quantative data only).
    return {'B2B Email': B2B_email, 'B2B Backlog': None, 'B2C Email': B2C_email, 'B2C Backlog': None, 'B2C Chat': None}



def create_csv(rows_dict):
    print(rows_dict)
    f = open(f'NBA_WNBA_Stats.csv','w',encoding="utf-8", newline='')

    field_names = ['NBA - email', 'NBA - chat', 'WNBA - email']

    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()

    writer.writerow({'NBA - email': rows_dict['NBA - email'], 'NBA - chat': rows_dict['NBA - chat'], 'WNBA - email': rows_dict['WNBA - email']})
    f.close()
