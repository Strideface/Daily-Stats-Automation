import core

#Note: all files to be read and output must be located in the current file directory (where you are running this script)

#1)
#read and extract NBA/WNBA stats from the NBA/WNBA spreadsheet sent by Dean
#NBA_WNBA_worksheets_dict = core.read_NBA_WNBA('NBA__WNBA_Daily_Stats.xlsx')

#2)filter them to include only the relevant data (consolidating into emails and chats)
#NBA_WNBA_stats_dict = core.filter_NBA_WNBA(NBA_WNBA_worksheets_dict)

#OPTIONAL - Use this dict if you have not receieved the NBA/WNBA stats spreadsheet from Dean yet and want to
#set these values to 0. Can be updated manually later, as usual.
NBA_WNBA_stats_dict = {'NBA - email': 0, 'NBA - chat': 0, 'WNBA - email': 0}
####hash out steps 1 and 2 above if using this option###

#3)read and extract the other client stats from the Zendesk scheduled report
daily_stats_worksheets_dict = core.read_daily_stats('Daily_Stats_L1_Support.xlsx')

#4)filter them to include only the relevant data (plus combine the NBA and WNBA stats and create a dictionary of rows
#ready to be written to a new xlsx file)
rows_dict = core.filter_daily_stats(daily_stats_worksheets_dict, NBA_WNBA_stats_dict)

#5)create a new 'Daily_Team_Stats' xlsx file with the rows from the previous step
core.create_new_xlsx_file(rows_dict)

#You can now copy and paste the rows from each tab in this file into the actual Daily-Team-Stats spreadsheet,
#which it replicates the format of.

print("\nFinished")
