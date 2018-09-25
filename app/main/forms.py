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

class UpdateForm(FlaskForm):
    """Update Records"""
    modalrecordid = StringField('recordid：', validators=[Required()])
    modalWork1 = StringField('HW1S：', validators=[Required()])
    modalWork2 = StringField('HW1R：', validators=[Required()])
    modalWork3 = StringField('HW2S：', validators=[Required()])
    modalWork4 = StringField('HW2R：', validators=[Required()])
    modalWork5 = StringField('打卡：', validators=[Required()])
    modalWork6 = StringField('优卡：', validators=[Required()])
    modalWork7 = StringField('提问：', validators=[Required()])
    modalWork8 = StringField('解答：', validators=[Required()])
    modalWork9 = StringField('分享：', validators=[Required()])
    modalWork10 = StringField('笔记：', validators=[Required()])
    modalWork11 = StringField('直播：', validators=[Required()])
    modalWork12 = StringField('协助：', validators=[Required()])

    modalsubmit = SubmitField('提交更改') 

class UpdateCheck(FlaskForm):
    """Update Check"""
    modalrecordid_check = StringField('recordid：', validators=[Required()])
    modalcheck = StringField('打卡：', validators=[Required()])
    modalsubmit_check = SubmitField('提交更改') 