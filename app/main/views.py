"""
little sister views
"""
# pylint: disable=invalid-name, too-few-public-methods


from flask import render_template
from flask_login import login_required


from . import main
from ..models import User

@main.route('/')
def index():
    """index view"""
    return render_template('index.html')


@main.route('/ulist')
@login_required
def ulist():
    """user list"""
    all_user = User.query.all()
    return render_template('ulist.html', userlist=all_user)
