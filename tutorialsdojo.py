import os
import requests
from bs4 import BeautifulSoup

class TutorialsDojo():

    def __init__(self):
        self.base_url = os.environ.get("TD_URL", 'https://tutorialsdojo.com/aws-cheat-sheets/')

    def fetch_page(self, url):
        source_code = requests.get(url)
        plain_text = source_code.text
        return BeautifulSoup(plain_text, "html.parser")
    
    def get_groups(self):
        page = self.fetch_page(self.base_url)
        divs = page.findAll('div', {'class': 'fusion-button-wrapper fusion-aligncenter'})
        groups = []

        for div in divs:
            link = div.find('a')
            title = div.find('span', {'class': 'fusion-button-text fusion-button-text-left'})
            groups.append({
                'title': title.text,
                'url': link['href']
            })
        return groups
    
    def get_topics(self, group):
        page = self.fetch_page(group['url'])
        divs = page.findAll('div', {'class': 'fusion-button-wrapper fusion-aligncenter'})
        topics = []

        for div in divs:
            link = div.find('a')
            title = div.find('span', {'class': 'fusion-button-text fusion-button-text-left'})
            topics.append({
                'title': title.text,
                'url': link['href']
            })
        return topics

    def get_content(self, topic):
        page = self.fetch_page(topic['url'])
        div = page.find('div', {'class': 'fusion-text'})
        
        for crap in div.findAll('p', {'data-pm-slice': '1 1 []'}):
            crap.decompose()

        return div.text
