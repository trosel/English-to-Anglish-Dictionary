import json
import requests
from bs4 import BeautifulSoup

big_letters = map(chr, range(ord('A'), ord('Z')+1))
dictionary = {}
for letter in big_letters:
    response = requests.get('http://anglish.wikia.com/wiki/English_Wordbook/' + letter)
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find_all('table')[0]
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) < 4:
            continue 
        modern_english_word = columns[0].get_text().strip()
        part_of_speech = columns[1].get_text().strip()
        attested_anglish = columns[2].get_text().strip()
        unattested_anglish = columns[3].get_text().strip()

        dictionary[modern_english_word] = {
            'class' : part_of_speech,
            'attested' : attested_anglish,
            'unattested' : unattested_anglish
        }
with open('dictionary.json', 'w') as fp:
    json.dump(dictionary, fp)

print('file created')
