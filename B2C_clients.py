#Use this dictionary to ensure values always go into the right cell in order when creating the new csv file.
#Any changes to the Daily-Team-Stats spreadsheet will need to be reflected here.
#Values initialised as 0 by default
#so that I only need to update the clients that have had tickets, when creating copy of this dict in the core logic.

B2C_clients_dict = {
    'ABFF Play' : 0,
    'BroadwayHD': 0,
    'Carlisle United TV' : 0,
    'Dallas Mavericks TV' : 0,
    'Dice Support Tickets' : 0,
    'European League of Football' : 0,
    'EuroLeague TV' : 0,
    'SkweekTV' : 0,
    'SuperMotocross Video Pass' : 0,
    'FIH': 0,
    'Fever Direct' : 0,
    'Ligue 1' : 0,
    'Longhorn Network' : 0,
    'Racer+ Support' : 0,
    'NBA' : 0, #Not on ZD
    'Sportsnet Pittsburgh' : 0,
    'Newcastle United TV' : 0,
    'NWSL+' : 0,
    'NZ Rugby' : 0,
    'Oilers Plus' : 0,
    'Sky Sport Now' : 0,
    'SPURSPLAY' : 0,
    'SuperLeague+' : 0,
    'TNA+' : 0,
    'UEFA TV' : 0,
    'UFC' : 0,
    'UFC Fight Pass Brasil' : 0,
    'Univision Now' : 0,
    'Univision TVE' : 0,
    'WNBA' : 0, #Not in ZD
    'Rugbypass.tv' : 0,
    'WWE Network' : 0,
}