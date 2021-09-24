import requests
import pandas
import re
from typing import List


def _html_cleaner_(text):
    if text is None:
        return "-"
    cleaner = re.compile(pattern='<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})')
    text = cleaner.sub("", text)
    return text


def _stemmer_(text):
    return text


class hh_parser:
    _login_: str
    _password_: str
    _base_url_: str
    _header_: str
    _api_agent_: str
    _per_page_: int
    _num_of_pages_: int

    def __init__(self,
                 login: str = None,
                 password: str = None,
                 per_page: int = 10,
                 num_of_pages: int = 20):
        self._login_ = login
        self._password_ = password
        self._base_url_ = "https://api.hh.ru/vacancies"
        self._header_ = "User-Agent"
        self._api_agent_ = "api-test-agent"
        self._per_page_ = per_page
        self._num_of_pages_ = num_of_pages
        self._last_data_ = None

    def get_vacancy(self, keyword, num_vac, num_page):
        r = requests.get(url=self._base_url_,
                         params={'text': keyword, 'per_page': self._per_page_, 'page': num_page})
        if num_vac > 0 and num_vac < self._per_page_:
            e = r.json().get('items')[num_vac]
        else:
            e = r.json().get('items')[0]
        return e

    def get_vacancy_id(self, id):
        r = requests.get(url=self._base_url_ + "/" + str(id))
        return r.json()

    def get_vacancies(self, keywords: List):
        data = []
        for keyword in keywords:
            for page in range(self._num_of_pages_):
                r = requests.get(url=self._base_url_,
                                 params={'text': keyword, 'per_page': self._per_page_, 'page': page})
                e = r.json().get('items')
                for num_vacancy in range(self._per_page_):
                    vacancy = []
                    vacancy.append(e[num_vacancy].get("id"))
                    vacancy.append(e[num_vacancy].get("name"))
                    vacancy.append(_html_cleaner_(e[num_vacancy].get("snippet").get("requirement")))
                    vacancy.append(_html_cleaner_(e[num_vacancy].get("snippet").get("responsibility")))
                    vacancy.append(_html_cleaner_(e[num_vacancy].get("snippet").get("description")))
                    vacancy.append(keyword)
                    vacancy.append(e[num_vacancy].get("salary"))
                    data.append(vacancy)
        dataFrame = pandas.DataFrame(data=data,
                                     columns=['id',
                                              'name',
                                              'requirements',
                                              'responsibilities',
                                              'description',
                                              'keyword',
                                              'salary'])
        self._last_data_ = dataFrame
        return data

    def save_last_csv(self, path: str = "d:\\"):
        if self._last_data_ is None:
            return False
        else:
            pandas.DataFrame.to_csv(self._last_data_, path, encoding="UTF-16")
            return True
