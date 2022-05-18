import json


def load_candidates_from_json(path='./data/candidates.json'):
    """Открываем файл и читаем из него данные """

    with open(path) as file:
        return json.load(file)


def get_candidates_list():
    """Функция форматирует данные
    и оттадет форматированную строку"""

    pre_format_list = ['<pre>', ]

    candidates_data = load_candidates_from_json()

    for item in candidates_data:
        format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

        pre_format_list.append(format_string)

    pre_format_list.append('</pre>')

    return ''.join(pre_format_list)


def get_candidate_info(uid):
    """По заданному id получаем данные о кандидате
     и возвращаем форматированную строку"""

    candidates_data = get_data_from_json()

    for item in candidates_data:
        if uid == item['id']:
            return f'<img src="https://i.pravatar.cc/150"> ' \
                   f'<pre>Имя - {item["name"]}\n' \
                   f'Позиция - {item["position"]}\n' \
                   f'Навыки - {item["skills"]}</pre>'


def get_candidates_with_skill(skill):
    """Функция находит всех кандидатов с полем skills
    и возвращает форматированную строку"""

    candidates_data = get_data_from_json()

    pre_format_list = ['<pre>', ]

    for item in candidates_data:
        if skill.lower() in item['skills'] or skill.capitalize() in item['skills']:
            format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

            pre_format_list.append(format_string)

    pre_format_list.append('</pre>')

    return ''.join(pre_format_list)
