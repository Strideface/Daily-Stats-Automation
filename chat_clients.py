#Use this dictionary to ensure values always go into the right cell in order when creating the new csv file.
#Any changes to the Daily-Team-Stats spreadsheet will need to be reflected here.
#Values initialised as 0 by default
#so that I only need to update the clients that have had tickets, when creating copy of this dict in the core logic.

chat_clients_dict = {
    'EuroLeague TV' : 0,
    'NBA' : 0, #Not on ZD
    'Sky Sport Now' : 0,
    'UFC' : 0,
    'UFC Fight Pass Brasil' : 0,
    'Univision Now' : 0,
}