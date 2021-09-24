import HHparser


new_agent = HHparser.hh_parser(login="qwerty29544@gmail.com", password="GAbhikPocbonmi4<")
# new_agent.get_vacancies(keywords=["Data Scientists", "Data Engineer", "Персонал"])
# new_agent.save_last_csv("d:\\test.csv")

print(HHparser._html_cleaner_(new_agent.get_vacancy_id(45694394).get("description")))

