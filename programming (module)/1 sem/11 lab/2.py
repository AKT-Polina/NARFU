import csv
import requests
from io import StringIO

url = 'https://www.stats.govt.nz/large-datasets/csv-files-for-download/'

response = requests.get(url)
data = csv.reader(StringIO(response.text))

for row in data:
    print(row)
