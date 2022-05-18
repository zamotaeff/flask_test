import json


def load_candidates_from_json(path='./project/data/candidates.json'):
    """Открываем файл и читаем из него данные """

    with open(path) as file:
        return json.load(file)


def get_candidates():
    """"""

    return load_candidates_from_json()


def get_candidate(candidate_id):
    """По заданному id получаем данные о кандидате
     и возвращаем их"""

    candidates_data = load_candidates_from_json()

    for candidate in candidates_data:
        if candidate_id == candidate['id']:
            return candidate


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


def get_candidates_by_name(candidate_name):
    """Функция находит кандидата по его имени
    и возвращает форматированную строку"""

    candidates_data = load_candidates_from_json()

    pre_format_string = '<pre>'

    for item in candidates_data:
        if candidate_name.lower() in item['skills'] or candidate_name.capitalize() in item['skills']:
            format_string = f'Имя - {item["name"]}\nПозиция - {item["position"]}\nНавыки - {item["skills"]}\n\n'

            pre_format_string += format_string

    pre_format_string += '</pre>'

    return pre_format_string
