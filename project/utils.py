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
    и возвращает список"""

    candidates_data = load_candidates_from_json()

    lst = []

    for candidate in candidates_data:
        if skill_name.lower() in candidate['skills']:
            lst.append(candidate)

    return lst


def get_candidates_by_name(candidate_name):
    """Функция находит совпадение по имени
    и возвращает список кандидатов"""

    candidates_data = load_candidates_from_json()

    lst = []

    for candidate in candidates_data:
        if candidate_name.lower() in candidate['name'].lower():
            lst.append(candidate)

    return lst
