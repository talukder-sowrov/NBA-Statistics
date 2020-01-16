import requests
from bs4 import BeautifulSoup


def createlist():
    month = input('What month is the game you are searching:\n').lower()
    website = requests.get(f'https://www.basketball-reference.com/leagues/NBA_2019_games-{month}.html')
    html_base = BeautifulSoup(website.text, 'html.parser')

    visitor_team_names = html_base.find_all('td', attrs={'data-stat': 'visitor_team_name'})
    home_team_names = html_base.find_all('td', attrs={'data-stat': 'home_team_name'})
    visitor_team_pts = html_base.find_all('td', attrs={'data-stat': 'visitor_pts'})
    home_team_pts = html_base.find_all('td', attrs={'data-stat': 'home_pts'})

    visitor_team_list = []
    home_team_list = []
    visitor_pts_list = []
    home_pts_list = []

    number_of_team = len(visitor_team_names)

    a = 0

    while a != number_of_team:
        # Creates Visitor Team List
        visitor_element = visitor_team_names[a]
        visitor_team = visitor_element.text
        visitor_team_list.append(visitor_team.lower())
        # Creates Visitor Points List
        visitor_pts_element = visitor_team_pts[a]
        visitor_pts = visitor_pts_element.text
        visitor_pts_list.append(visitor_pts)
        # Creates Home Team List
        home_element = home_team_names[a]
        home_team = home_element.text
        home_team_list.append(home_team.lower())
        # Creates Home Pts List
        home_pts_element = home_team_pts[a]
        home_pts = home_pts_element.text
        home_pts_list.append(home_pts)
        a += 1

    return home_team_list, home_pts_list, visitor_team_list, visitor_pts_list


def checkstring(visitor_team_list, home_team_list):
    visitor_team = input('Enter the Visiting team name: \n').lower()
    home_team = input('Enter the Home team name: \n').lower()
    if visitor_team.isdigit() or home_team.isdigit():
        checkstring(visitor_team_list, home_team_list)
    else:
        checkteam(visitor_team_list, home_team_list, visitor_team, home_team)


def checkteam(visitor_team_list, home_team_list, visitor_team, home_team):
    number = enumerate(visitor_team_list)
    game = []
    for index, team in number:
        if team == visitor_team:
            game.append(index)
    for value in game:
        if home_team_list[value] == home_team:
            game_value = value
            break
    checkvictor(game_value, visitor_pts_list, home_pts_list, visitor_team, home_team)


def checkvictor(game_value, visitor_pts_list, home_pts_list, visitor_team, home_team):
    print(visitor_pts_list[game_value])
    print(home_pts_list[game_value])
    if visitor_pts_list[game_value] > home_pts_list[game_value]:
        print(f'{visitor_team.title()} won the game over {home_team.title()}')
    else:
        print(f'{home_team.title()} won the game over {visitor_team.title()}')


home_team_list, home_pts_list, visitor_team_list, visitor_pts_list = createlist()
checkstring(visitor_team_list, home_team_list)





