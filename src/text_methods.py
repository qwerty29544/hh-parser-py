import re


def html_cleaner(text):
    if text is None:
        return " "
    cleaner = re.compile(pattern='<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6})')
    text = cleaner.sub("", text)
    return text


def key_skills_extractor(input_list):
    if len(input_list) == 0:
        return " "
    else:
        data = []
        for i in range(len(input_list)):
            data.append(input_list[i]['name'])
        return " ".join(data)


def description_extractor(input_r):
    input_r = html_cleaner(input_r)
    input_r = stemmer(input_r)
    return input_r


def requirements_extractor(description):
    if description is None:
        return " "
    extractor = re.compile(pattern='Требования.*')
    text = extractor.findall(description)
    text = description_extractor(text)
    return text


def stemmer(text):
    return text