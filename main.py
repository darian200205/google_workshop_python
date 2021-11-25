#  Course-5
#  ----------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

URL = "https://lpf.ro/liga-1"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

result_table = soup.find(id='clasament_ajax')
#print(result_table)

team_rows = result_table.find_all(class_='echipa_row')
#print(team_rows)

teams = []
for team in team_rows:
    team_cell = team.find('td', class_='echipa')
    team_name = team_cell.find('a').text.strip()
    team_position = team.find('td', class_='poz').text.strip()
    team_points = team.find('td', class_='puncte').text.strip()

    teams.append(
        {
            'name': team_name,
            'position': team_position,
            'points': team_points
        }
    )

print(teams)

#print(page)

#print(page.content)


