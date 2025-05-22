import core

NBA_WNBA_worksheets_dict = core.read_NBA_WNBA('NBA__WNBA_Daily_Stats.xlsx')

NBA_WNBA_stats_dict = core.filter_NBA_WNBA(NBA_WNBA_worksheets_dict)

daily_stats_worksheets_dict = core.read_daily_stats('Daily_Stats_L1_Support.xlsx')

rows_dict = core.filter_daily_stats(daily_stats_worksheets_dict, NBA_WNBA_stats_dict)

# core.create_csv(rows_dict)

print("\nFinished")
