import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
name_elements = soup.find_all('h4', class_='card-title')
price_elements = soup.find_all('h5', class_='')

for i in range(0, len(name_elements)):
    print(f'{i}: {price_elements[i].text} за {name_elements[i].text.strip()}')
    # print(str(i) + ": " + price_elements[i].text + " за " + name_elements[i].text.strip())

# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')
#
# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print("--" + authors[i].text)
#     tagsforquote = tags[i].find_all('a', class_='tag')
#     for tagforquote in tagsforquote:
#         print(tagforquote.text)
#     print()
