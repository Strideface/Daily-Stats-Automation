#Use this dictionary to ensure values always go into the right cell in order when creating the new csv file.
#Any changes to the Daily-Team-Stats spreadsheet will need to be reflected here.
#Values initialised as 0 by default
#so that I only need to update the clients that have had tickets, when creating copy of this dict in the core logic.


B2B_clients_dict = {
    'ABFF Client Support' : 0,
    'Adjara Sport Client Support' : 0,
    'Al Jazeera Client Support' : 0,
    'AMCN HIDIVE Client Support' : 0,
    'Anderlecht Client Support' : 0,
    'Blast TV Client Support' : 0,
    'Carlisle United Client Support' : 0,
    'Core Sports Client Support' : 0,
    'Dallas Mavericks Client Support' : 0,
    'ELF Client Support' : 0,
    'Endeavor Streaming Privacy' : 0,
    'PLCS Client Support' : 0, #EPL
    'EuroLeague Client Support' : 0,
    'FEDCOM Client Support' : 0, #Skweek TV
    'Supermotocross Client Support' : 0,
    'Feyenoord Client Support' : 0,
    'FIS Client Support' : 0,
    'Indiana Fever Client Support' : 0,
    'Ligue 1 Client Support' : 0,
    'Longhorn Network Client Support' : 0,
    'Racer+ Client Support' : 0, #Mav TV
    'Melissa Wood Health Client Support' : 0,
    'NBA Client Support' : 0,
    'NESN Client Support' : 0,
    'Newcastle United Client Support' : 0,
    'NHRA Client Support' : 0,
    'Northwoods League Client Support' : 0,
    'NWSL Client Support' : 0,
    'NZ Rugby Client Support' : 0,
    'Oilers Client Support' : 0,
    'PTO Client Support' : 0,
    'R & A Client Support' : 0,
    'Real Madrid Client Support' : 0,
    'Shout! TV Client Support' : 0,
    'Sky Sport Now Client Support' : 0,
    'Sport24 Client Support': 0,
    'SPTV Client Support' : 0,
    'Spurs TV Client Support' : 0,
    'SuperLeague+ Client Support' : 0,
    'TNA Plus Client Support' : 0,
    'UEFA TV Client Support' : 0,
    'UFC Client Support' : 0,
    'UFC Fight Pass Brasil Client Support' : 0,
    'Univision Now Client Support' : 0,
    'USGA Client Support' : 0,
    'WNBA League Pass Client Support' : 0,
    'World Rugby Client Support' : 0,
    'WWE Client Support' : 0,
}