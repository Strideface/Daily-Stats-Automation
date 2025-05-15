import core

worksheets_dict = core.read_xlsx('NBA__WNBA_Daily_Stats.xlsx')

rows_dict = core.filter_stats_from_worksheets(worksheets_dict)

core.create_csv(rows_dict)

print("Finished")
