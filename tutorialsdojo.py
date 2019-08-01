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
    
    def get_courses(self):
        page = self.fetch_page(self.base_url)
        divs = page.findAll('div', {'class': 'fusion-button-wrapper fusion-aligncenter'})
        courses = []

        for div in divs:
            link = div.find('a')
            title = div.find('span', {'class': 'fusion-button-text fusion-button-text-left'})
            courses.append({
                'title': title.text,
                'url': link['href']
            })
        return courses
