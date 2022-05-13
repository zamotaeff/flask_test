from flask import Flask

from utils import *


app = Flask(__name__)


@app.route("/")
def page_index():
    """Представление для списка кандидатов"""

    return get_candidates_list()


@app.route("/candidates/<int:uid>/")
def page_candidates(uid):
    """Представление для вывода информации о кандидате по его ID"""

    return get_candidate_info(uid)


@app.route('/skills/<skill>/')
def page_skills(skill):
    """Представление для списка кандидатов, имеющих опеределенный навык"""

    return get_candidates_with_skill(skill)


app.run()
