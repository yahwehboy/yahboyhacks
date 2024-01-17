import requests
from bs4 import BeautifulSoup

#sets a default header for our requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

#gets the target website using its url
target = requests.get('https://sabiprogrammers.com/', headers=headers ).content

#parse the website content using BeautifulSoup
soup = BeautifulSoup(target, 'html.parser')

#gets the specific content using CSS selectors
results= soup.select('.bdt-ep-advanced-icon-box-content')

#saves the results to txt/csv file
with open("result.txt", "w", encoding="utf-8") as output:
    for result in results:
        output.write(f"{result.text}\n")