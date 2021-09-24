import requests
import pandas
import re
from typing import List
from text_methods import *


class hh_data_loader:
    def __init__(self,
                 config: dict):
        self.url = config['url']
        self.num_of_pages = config['number of pages']
        self.vacs_on_page = config['vacs on page']
        self.keywords = config['keywords']
        self.last_ids = []
        self.last_data = []

    def get_vacs_id(self):
        data = []
        for keyword in self.keywords:
            iter_on_keyword = 1
            for page in range(self.num_of_pages):
                try:
                    request = requests.get(url=self.url,
                                           params={'text': keyword, 'per_page': self.vacs_on_page, 'page': page})
                    request.raise_for_status()
                    vacs_on_page = request.json()['items']
                    for vac_num in range(len(vacs_on_page)):
                        data.append([iter_on_keyword, vacs_on_page[vac_num]['id'], keyword])
                        iter_on_keyword += 1
                    if len(vacs_on_page) != self.vacs_on_page:
                        break
                except requests.exceptions.HTTPError:
                    print("Error response from server")
        self.last_ids = data
        return data

    def get_vacancy_id(self, id):
        try:
            r = requests.get(url=self.url + "/" + str(id))
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError:
            return None

    def get_dataset(self):
        data = []
        ids = self.get_vacs_id()
        for id in range(len(ids)):
            row = []
            vacancy = self.get_vacancy_id(ids[id][1])
            if vacancy is None:
                continue
            row.append(vacancy['id'])
            row.append(vacancy['name'])
            row.append(ids[id][0])
            row.append(ids[id][2])
            row.append(description_extractor(vacancy['description']))
            row.append(key_skills_extractor(vacancy['key_skills']))
            data.append(row)
        dataFrame = pandas.DataFrame(data=data, columns=['vac_id', 'name', 'search_number',
                                                         'out', 'description', 'key_skills'])
        dataFrame.drop_duplicates()
        self.last_data = dataFrame
        return dataFrame
