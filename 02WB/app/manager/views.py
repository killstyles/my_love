from flask import render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user

from app import db
from . import manager
from app.decorators import decorator_admin, decorator_permission
from app.models import Permission, Comments, News
from .forms import EditUserForm
from flask import abort
from app.models import User

@manager.route('/edit_user', methods=['GET', 'POST'])
@decorator_admin
def edit_user() :
    id = request.args.get('id')
    if id is None :
        abort(404)
    user = User.query.filter_by(id=id).first()
    if user is None :
        abort(404)

    form = EditUserForm()
    if form.validate_on_submit() :
        user.name = form.name.data
        user.confirmed = form.confirmed.data
        user.location = form.location.data
        user.role_id = form.role_id.data
        user.about_me = form.about_me.data
        if len(form.password.data) != 0 :
            user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.user_info', id=user.id))

    form.name.data = user.name
    form.email.data = user.email
    form.location.data = user.location
    form.role_id.data = user.role_id
    form.about_me.data = user.about_me
    form.confirmed.data = user.confirmed
    return render_template('manager/edit_user.html', form=form)

@manager.route('/index')
@decorator_admin
def index() :
    page = request.args.get('page', type=int, default=1)
    comments = Comments.query.group_by(Comments.news_id).all()
    paginate = Comments.query.order_by(Comments.id.desc()).paginate(page=page, per_page=5, error_out=False)

    return render_template('manager/edit_comments.html',comments = comments,paginate=paginate)

@manager.route('/manager_comment')
@decorator_permission(Permission.MODE_COMMENT)
def manager_comment() :
    return 'i am moderator or admin'
@manager.route('/delete_comments')
@login_required
def delete_comments() :
    cid = request.args.get('cid')
    if cid is None:
        abort(404)
    comments = Comments.query.filter_by(id=cid).first()
    if comments is None:
        abort(404)

    if current_user == comments.user or current_user.is_admin() :
        db.session.delete(comments)
        db.session.commit()

    return redirect(url_for('manager.index',nid = comments.news_id))
