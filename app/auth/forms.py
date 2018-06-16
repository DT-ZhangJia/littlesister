"""
little sister auth
"""
# pylint: disable=invalid-name

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    """login form class"""
    email_input = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    passwd_input = PasswordField('密码', validators=[Required()])
    remember_me_box = BooleanField('保持登录')
    submit_btn = SubmitField('登录')

class RegisterForm(FlaskForm):
    """register form class"""
    email_reg_input = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username_reg_input = StringField('姓名/显示名', validators=[Required(), Length(1, 64)]) # pylint: disable=C0301
    passwd_reg_input = PasswordField('密码', validators=[Required(), EqualTo('passwd2_reg_input', message='Passwords must match.')]) # pylint: disable=C0301
    passwd2_reg_input = PasswordField('再次输入密码', validators=[Required()])
    submit_reg_btn = SubmitField('注册')

    def validate_email_reg_input(self, field):#pylint: disable=R0201
        """check existed email"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('此邮箱已经注册。')
    
    #def validate_username_reg_input(self, field):#pylint: disable=R0201
    #    """check existed username"""
    #    if User.query.filter_by(username=field.data).first():
    #        raise ValidationError('用户名已存在。')

class ChangepwForm(FlaskForm):
    """change password form"""
    old_passwd_input = PasswordField('旧密码', validators=[Required()])
    passwd_chg_input = PasswordField('新密码', validators=[Required(), EqualTo('passwd2_chg_input', message='Passwords must match.')]) # pylint: disable=C0301
    passwd2_chg_input = PasswordField('再次输入新密码', validators=[Required()])
    submit_chg_btn = SubmitField('修改密码')

class ResetrequestForm(FlaskForm):
    """Reset Password Request"""
    email_request_input = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    submit = SubmitField('重设密码')

class PasswordResetForm(FlaskForm):
    """Reset Password Form"""
    email_resetpw_input = StringField('Email', validators=[Required(), Length(1, 64), Email()],
                                      render_kw={'readonly': True})
    passwd_reset_input = PasswordField('新密码', validators=[Required(), EqualTo('passwd2_reset_input', message='Passwords must match')]) # pylint: disable=C0301
    passwd2_reset_input = PasswordField('再次输入新密码', validators=[Required()])
    submit_reset_btn = SubmitField('重设密码')

