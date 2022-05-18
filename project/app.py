from flask import Flask, render_template

from project.utils import *


app = Flask(__name__)


@app.route("/")
def page_index():
    """Представление для списка кандидатов"""

    candidates = get_candidates()

    return render_template('list.html', items=candidates)


@app.route("/candidate/<int:uid>/")
def page_candidate(uid):
    """Представление для вывода информации о кандидате по его ID"""

    candidate = get_candidate(uid)

    return render_template('item.html', candidate=candidate)


@app.route("/search/<candidate_name>/")
def page_search(candidate_name):
    """Представление для поиска кандидата по его имени"""

    candidates = get_candidates_by_name(candidate_name)

    return render_template('search.html', items=candidates)


@app.route('/skills/<skill_name>/')
def page_skills(skill_name):
    """Представление для списка кандидатов, имеющих опеределенный навык"""

    candidates = get_candidates_by_skill(skill_name)

    return render_template('skill.html', items=candidates)


app.run()
