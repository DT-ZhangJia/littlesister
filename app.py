"""
little sister
"""
# pylint: disable=invalid-name
# test update

from app import create_app
from app.models import User, Role


app = create_app('default')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)
