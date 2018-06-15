"""
little sister models
"""
# pylint: disable=invalid-name, too-few-public-methods, no-member


from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from . import mydb, login_manager

class Permission(mydb.Model):
    """permission list"""
    __tablename__ = 'permission'
    pid = mydb.Column(mydb.Integer, primary_key=True)
    stagenum = mydb.Column(mydb.Integer)
    groupnum = mydb.Column(mydb.Integer)
    tauid = mydb.Column(mydb.Integer)
    power = mydb.Column(mydb.Integer)

    def __repr__(self):
        return '<Permission %r>' % self.pid



class Students(mydb.Model):
    """Students info"""
    __tablename__ = 'students'
    stdtid = mydb.Column(mydb.Integer, primary_key=True)
    instageid = mydb.Column(mydb.String(64))
    stdtname = mydb.Column(mydb.String(64))
    stagenum = mydb.Column(mydb.Integer)
    groupnum = mydb.Column(mydb.Integer)
    warned = mydb.Column(mydb.Boolean, default=False)
    notactive = mydb.Column(mydb.Boolean, default=False)

    def __repr__(self):
        return '<Students %r>' % self.stdtname

class Records(mydb.Model):
    """Points and Records"""
    __tablename__ = 'records'
    recordid = mydb.Column(mydb.Integer, primary_key=True)
    stdtid = mydb.Column(mydb.Integer)
    stagenum = mydb.Column(mydb.Integer)
    weekid = mydb.Column(mydb.Integer)
    work1 = mydb.Column(mydb.Integer)
    work2 = mydb.Column(mydb.Integer)
    work3 = mydb.Column(mydb.Integer)
    work4 = mydb.Column(mydb.Integer)
    work5 = mydb.Column(mydb.Integer)
    work6 = mydb.Column(mydb.Integer)
    work7 = mydb.Column(mydb.Integer)
    work8 = mydb.Column(mydb.Integer)
    work9 = mydb.Column(mydb.Integer)
    work10 = mydb.Column(mydb.Integer)
    work11 = mydb.Column(mydb.Integer)
    work12 = mydb.Column(mydb.Integer)


    def __repr__(self):
        return '<Records %r>' % self.stdtid


class Role(mydb.Model):
    """role"""
    __tablename__ = 'roles'
    uid = mydb.Column(mydb.Integer, primary_key=True)
    name = mydb.Column(mydb.String(64), unique=True)
    defaultp = mydb.Column(mydb.Boolean, default=False, index=True)
    permissions = mydb.Column(mydb.Integer)
    user = mydb.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, mydb.Model):
    """user"""
    __tablename__ = 'users'
    uid = mydb.Column(mydb.Integer, primary_key=True)
    username = mydb.Column(mydb.String(64), unique=True, index=True)
    email = mydb.Column(mydb.String(64), unique=True, index=True)
    passwd_hash = mydb.Column(mydb.String(128))
    role_id = mydb.Column(mydb.Integer, mydb.ForeignKey('roles.uid'))
    confirmed = mydb.Column(mydb.Boolean, default=False)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.role is None:
                self.role = Role.query.filter_by(defaultp=True).first()

    @property
    def passwd(self):
        """设置无法读取密码属性"""
        raise AttributeError('无法读取')

    @passwd.setter
    def passwd(self, passwd):
        """生成密码离散值"""
        self.passwd_hash = generate_password_hash(passwd)

    def verify_passwd(self, passwd):
        """验证离散值密码"""
        return check_password_hash(self.passwd_hash, passwd)

    def get_id(self): 
        return self.uid

    def generate_confirmation_token(self, expiration=300):
        """生成注册确认令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.uid})

    def confirm(self, token):
        """验证存在"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except: # pylint: disable=W0702
            return False
        if data.get('confirm') != self.uid:
            return False
        self.confirmed = True
        mydb.session.add(self)
        return True

    def generate_resetpw_token(self, expiration=3600):
        """生成重置密码确认令牌"""
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.uid})

    def reset_password(self, token, new_password):
        """写入重置的新密码"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except: # pylint: disable=W0702
            return False
        if data.get('reset') != self.uid:
            return False
        self.passwd_hash = generate_password_hash(new_password)
        mydb.session.add(self)
        return True 


    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    """用户存在性回调函数"""
    return User.query.get(int(user_id)) 
