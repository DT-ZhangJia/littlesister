"""
little sister errors
"""
# pylint: disable=invalid-name, too-few-public-methods

from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    """404"""
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    """500"""
    return render_template('500.html'), 500
