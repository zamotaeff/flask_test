from flask import Flask

from project.utils import *


app = Flask(__name__)


@app.route("/")
def page_index():
    """Представление для списка кандидатов"""

    return get_candidates()


@app.route("/candidates/<int:uid>/")
def page_candidates(uid):
    """Представление для вывода информации о кандидате по его ID"""

    return get_candidate(uid)


@app.route('/skills/<skill>/')
def page_skills(skill):
    """Представление для списка кандидатов, имеющих опеределенный навык"""

    return get_candidates_by_skill(skill)


app.run()
