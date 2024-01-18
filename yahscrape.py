import requests
from bs4 import BeautifulSoup

#sets a default header for our requests
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

#gets user inputs 
url = input("Enter the targets url 'https://example.com/': ")
selector = input("Enter the CSS selector '.bdt-ep-advanced-icon-box-content': ")


#define the function
def yahscrape(x, y):
    
    #gets the target website using its url
    target = requests.get(url, headers=headers).content
    
    
        
    #parse the website content using BeautifulSoup
    soup = BeautifulSoup(target, 'html.parser')

    #gets the specific content using CSS selectors
    results= soup.select(selector)

    #saves the results to txt/csv file
    with open("result.txt", "w", encoding="utf-8") as output:
        for result in results:
            output.write(f"{result.text}\n")

#call the function
yahscrape(url, selector)
