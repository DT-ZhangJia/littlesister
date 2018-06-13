"""
little sister views
"""
# pylint: disable=invalid-name, too-few-public-methods

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    """NameForm"""
    indexname = StringField('填写你的ID：', validators=[Required()]) 
    indexsubmit = SubmitField('提交') 
