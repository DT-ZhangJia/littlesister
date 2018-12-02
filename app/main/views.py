"""
little sister views
"""
# pylint: disable=invalid-name, too-few-public-methods


from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from sqlalchemy import and_, or_, not_

from . import main
from .. import mydb
from ..models import User, Students, Records, Permission
from .forms import UpdateForm, UpdateCheck



studentDict = {}
studentrecordDict = {}
teamrecordDict = {}
teamdict = {1:"A", 2:"B", 3:"C", 4:"D", 5:"E"}
weekdict = {1:"一", 2:"二", 3:"三", 4:"四"}
stage = 6 #供进阶2期使用
recorddict = {}

@main.route('/')
def index():
    """index view"""

    all_students = Students.query.filter_by(stagenum = stage).all()
    for student in all_students:
        studentDict[student.stdtid] = [student.instageid, student.stdtname, student.groupnum]
        studentrecordDict[student.stdtid] = 0

    for k,v in teamdict.items():
        teamrecordDict[k] = 0

    all_records = Records.query.filter_by(stagenum = stage).all()
    for record in all_records:
        total = (record.work1 + record.work2 + record.work3 + record.work4 + record.work5 + record.work6
                 + record.work7 + record.work8 + record.work9 + record.work10 + record.work11 + record.work12)

        studentrecordDict[record.stdtid] = studentrecordDict[record.stdtid] + total 
        teamrecordDict[studentDict[record.stdtid][2]] = teamrecordDict[studentDict[record.stdtid][2]] + total

    sortrecord = sorted(studentrecordDict.items(),key = lambda item:item[1],reverse = True)
    sortteam = sorted(teamrecordDict.items(),key = lambda item:item[1],reverse = True)

    return render_template('index.html', fullrecords = all_records, 
                           studentDict=studentDict, teamdict=teamdict,
                           weekdict=weekdict, sortrecord=sortrecord, sortteam=sortteam)


@main.route('/team<groupnum>', methods=['GET', 'POST'])
def team(groupnum):
    """team view"""

    if teamdict. __contains__(int(groupnum)) == False:
        return render_template('404.html'), 404

    mypower = 0
    if current_user.is_authenticated:
        myta = Permission.query.filter(and_(Permission.stagenum == stage, 
            Permission.groupnum == groupnum, Permission.tauid == current_user.uid, Permission.power == 2)).first()
        myga = Permission.query.filter(and_(Permission.stagenum == stage, 
            Permission.groupnum == groupnum, Permission.tauid == current_user.uid, Permission.power == 1)).first()

        if myta:
            mypower = 2
        elif myga:
            mypower = 1
        else:
            mypower = 0


    updateform_app = UpdateForm()
    updatecheck_app = UpdateCheck()

    team_records = Records.query.filter_by(stagenum = stage).all()
    all_students = Students.query.all()
    for student in all_students:
        studentDict[student.stdtid] = [student.instageid, student.stdtname, student.groupnum]
    
    if updateform_app.validate_on_submit():
        recordupdate = Records.query.filter_by(recordid = updateform_app.modalrecordid.data).first()
        recordupdate.work1 = updateform_app.modalWork1.data
        recordupdate.work2 = updateform_app.modalWork2.data
        recordupdate.work3 = updateform_app.modalWork3.data
        recordupdate.work4 = updateform_app.modalWork4.data
        recordupdate.work5 = updateform_app.modalWork5.data
        recordupdate.work6 = updateform_app.modalWork6.data
        recordupdate.work7 = updateform_app.modalWork7.data
        recordupdate.work8 = updateform_app.modalWork8.data
        recordupdate.work9 = updateform_app.modalWork9.data
        recordupdate.work10 = updateform_app.modalWork10.data
        recordupdate.work11 = updateform_app.modalWork11.data
        recordupdate.work12 = updateform_app.modalWork12.data
        mydb.session.add(recordupdate)# pylint: disable=no-member
        mydb.session.commit()# pylint: disable=no-member
        #return redirect(url_for('main.index'))

    if updatecheck_app.validate_on_submit():
        checkupdate = Records.query.filter_by(recordid = updatecheck_app.modalrecordid_check.data).first()
        checkupdate.work5 = updatecheck_app.modalcheck.data #第5列是打卡积分栏
        mydb.session.add(checkupdate)# pylint: disable=no-member
        mydb.session.commit()# pylint: disable=no-member


    return render_template('team.html', team_records = team_records, teamnum=groupnum,
                           studentDict=studentDict, teamdict=teamdict, mypower=mypower,
                           weekdict=weekdict, modalform=updateform_app, checkform=updatecheck_app)



