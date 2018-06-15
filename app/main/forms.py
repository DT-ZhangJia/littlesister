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
    modalWork1 = StringField('HW1：', validators=[Required()])
    modalWork2 = StringField('HW2：', validators=[Required()])
    modalWork3 = StringField('打卡：', validators=[Required()])
    modalWork4 = StringField('打卡前三：', validators=[Required()])
    modalWork5 = StringField('答疑：', validators=[Required()])
    modalWork6 = StringField('分享：', validators=[Required()])
    modalWork7 = StringField('干货：', validators=[Required()])
    modalWork8 = StringField('笔记：', validators=[Required()])
    modalWork9 = StringField('选上话题：', validators=[Required()])
    modalWork10 = StringField('直播：', validators=[Required()])
    modalWork11 = StringField('脑洞：', validators=[Required()])
    modalWork12 = StringField('帮助助教：', validators=[Required()])

    modalsubmit = SubmitField('提交更改') 

class UpdateCheck(FlaskForm):
    """Update Check"""
    modalrecordid_check = StringField('recordid：', validators=[Required()])
    modalcheck = StringField('打卡：', validators=[Required()])
    modalsubmit_check = SubmitField('提交更改') 