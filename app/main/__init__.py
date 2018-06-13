"""
little sister blueprint factory
"""
# pylint: disable=invalid-name


from flask import Blueprint

main = Blueprint('main', __name__)


from .import views, errors # pylint: disable=wrong-import-position
