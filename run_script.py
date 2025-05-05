import core

worksheets_dict = core.read_xlsx('NBA__WNBA_Daily_Stats.xlsx')

core.filter_stats_from_worksheets(worksheets_dict)