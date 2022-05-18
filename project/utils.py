import json


def load_candidates_from_json(path='./data/candidates.json'):
    """Открываем файл и читаем из него данные """

    with open(path) as file:
        return json.load(file)


def get_candidates():
    """Функция форматирует данные
    и оттадет форматированную строку"""

    pre_format_string = '<pre>'

    candidates_data = load_candidates_from_json()

    for item in candidates_data:
        format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

        pre_format_string += format_string

    pre_format_string += '</pre>'

    return pre_format_string


def get_candidate(candidate_id):
    """По заданному id получаем данные о кандидате
     и возвращаем форматированную строку"""

    candidates_data = load_candidates_from_json()

    for item in candidates_data:
        if candidate_id == item['id']:
            return f'<img src="https://i.pravatar.cc/150"> ' \
                   f'<pre>Имя - {item["name"]}\n' \
                   f'Позиция - {item["position"]}\n' \
                   f'Навыки - {item["skills"]}</pre>'


def get_candidates_by_skill(skill_name):
    """Функция находит всех кандидатов с полем skills
    и возвращает форматированную строку"""

    candidates_data = load_candidates_from_json()

    pre_format_string = '<pre>'

    for item in candidates_data:
        if skill_name.lower() in item['skills'] or skill_name.capitalize() in item['skills']:
            format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

            pre_format_string += format_string

    pre_format_string += '</pre>'

    return pre_format_string


def get_candidates_with_skill(skill):
    """Функция находит всех кандидатов с полем skills
    и возвращает форматированную строку"""

    candidates_data = load_candidates_from_json()

    pre_format_list = ['<pre>', ]

    for item in candidates_data:
        if skill.lower() in item['skills'] or skill.capitalize() in item['skills']:
            format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

            pre_format_list.append(format_string)

    pre_format_list.append('</pre>')

    return ''.join(pre_format_list)
