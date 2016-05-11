import csv
import requests 
from BeautifulSoup import BeautifulSoup

url = 'http://www.umpd.umd.edu/stats/incident_logs.cfm?year=2016&month=1'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

table = soup.findAll('table')[0]

num_rows = len(table.findAll('tr')[1:])

list_of_rows = []

for i in xrange(1, num_rows, 2):
        row = table.findAll('tr')[i]
        list_of_cells = []
        for cell in row.findAll('td'):
                list_of_cells.append(cell.text)
        list_of_cells.append(table.findAll('tr')[i+1].text)
        list_of_rows.append(list_of_cells)

	
outfile = open("./crimes.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(['Case Number', 'Occurred Date/Time', 'Reported Date/Time', 'Crime Type', 'Disposition', 'Location'])
writer.writerows(list_of_rows)