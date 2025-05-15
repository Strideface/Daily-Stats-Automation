import core

# worksheets_dict = core.read_NBA_WNBA('NBA__WNBA_Daily_Stats.xlsx')

# rows_dict = core.filter_NBA_WNBA(worksheets_dict)

# core.create_csv(rows_dict)

worksheets_dict = core.read_daily_stats('Daily_Stats_L1_Support.xlsx')

core.filter_daily_stats(worksheets_dict)

print("Finished")
