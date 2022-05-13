from flask import Flask

from utils import *


app = Flask(__name__)


@app.route("/")
def page_index():
    """"""

    return get_candidates_list()


@app.route("/candidates/<int:uid>/")
def page_candidates(uid):
    """"""

    return get_candidate_info(uid)


@app.route('/skills/<skill>/')
def page_skills(skill):
    """"""

    return get_candidates_with_skill(skill)


app.run()
