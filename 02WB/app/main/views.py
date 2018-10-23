from flask import render_template,url_for,redirect,request
from flask import abort, flash
from flask_login import login_required

from . import main
from app import db

from app.models import User
from .forms import EditUserForm, PostCommentsForm
from flask_login import current_user
from .forms import PostNewsForm
from app.models import News,Comments

from app.decorators import decorator_permission
from app.models import Permission
from flask import make_response

#这个函数要修改浏览器中的cookie
@main.route('/set_all_news_flag')
def set_all_news_flag() :
    response = make_response(redirect(url_for('.all_news')))
    response.set_cookie('follow_flag', '0', 60*60*24)
    return response

@main.route('/set_follow_news_flag')
def set_follow_news_flag() :
    response = make_response(redirect(url_for('.all_news')))
    response.set_cookie('follow_flag', '1', 60 * 60 * 24)
    return response

@main.route('/all_followers')
def all_followers() :
    id = request.args.get('id')
    if id is None:
        abort(404)
    user = User.query.filter_by(id=id).first()
    if user is None:
        abort(404)

    #通过反向关系followers得到的全是Follow对象
    #这些对象的特点是：followed_id都等于user.id
    #follower_id是关注user的用户的id---->follower是user对象
    afs = user.followers.all()

    users = [f.follower for f in afs]

    return render_template('main/all_followers.html', users=users)

@main.route('/follow')
@decorator_permission(Permission.FOLLOW)
def follow() :
    id = request.args.get('id')
    if id is None :
        abort(404)
    user = User.query.filter_by(id=id).first()
    if user is None :
        abort(404)
    current_user.follow(user)
    return redirect(url_for('main.user_info', id=user.id))

@main.route('/unfollow')
@decorator_permission(Permission.FOLLOW)
def unfollow() :
    id = request.args.get('id')
    if id is None :
        abort(404)
    user = User.query.filter_by(id=id).first()
    if user is None :
        abort(404)
    current_user.unfollow(user)
    return redirect(url_for('main.user_info', id=user.id))

@main.route('/delete_news')
@login_required
def delete_news() :
    nid = request.args.get('nid')
    if nid is None:
        abort(404)
    news = News.query.filter_by(id=nid).first()
    if news is None:
        abort(404)

    if current_user == news.user or current_user.is_admin() :
        db.session.delete(news)
        db.session.commit()

    return redirect(url_for('main.all_news'))

@main.route('/delete_comments')
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

    return redirect(url_for('main.news',nid = comments.news_id))

@main.route('/news')
def news() :
    nid = request.args.get('nid')
    if nid is None :
        abort(404)
    news = News.query.filter_by(id=nid).first()
    page = request.args.get('page', type=int, default=1)

    comments = Comments.query.filter_by(news_id=nid).order_by(Comments.id.desc()).all()
    paginate = Comments.query.filter_by(news_id=nid).order_by(Comments.id.desc()).paginate(page=page, per_page=5, error_out=False)
    if news is None :
        abort(404)
    return render_template('main/news.html', news=news,comments=comments,paginate=paginate)

@main.route('/post_news', methods=['GET', 'POST'])
@login_required
def post_news() :
    form = PostNewsForm()
    if form.validate_on_submit() :
        news = News()
        news.body = form.body.data
        news.private = form.private.data
        news.title = form.title.data
        news.user_id = current_user.id
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('.all_news'))
    return render_template('main/post_news.html', form=form)

@main.route('/post_comments', methods=['GET', 'POST'])
@login_required
def post_comments() :
    form = PostCommentsForm()
    if form.validate_on_submit() :
        comments = Comments()
        comments.body = form.body.data
        comments.user_id = current_user.id
        comments.news_id = request.args.get('nid')
        db.session.add(comments)
        db.session.commit()
        return redirect(url_for('.news',nid = comments.news_id))
    return render_template('main/post_comments.html', form=form)
#http://127.0.0.1/all_news?page=4
#http://127.0.0.1/all_news

from app.models import Follow

@main.route('/all_news')
def all_news() :
    #ans = News.query.all()
    #分页对象
    page = request.args.get('page', type=int, default=1)

    #后去cookie中follow_flag的值 '0' '1'
    follow_flag = request.cookies.get('follow_flag', default='0')

    if follow_flag == '0' :
        paginate = News.query.order_by(News.id.desc()).paginate(page=page, per_page=5, error_out=False)
    else:
        # followeds = Follow.query.filter_by(follower_id=current_user.id).all()
        # users = [f.followed for f in followeds]
        # news = [u.news.all() for u in users]
        # 联结查询：多张表一起查询
        # 本质：把符合条件的记录查询出来做一张虚拟表
        query = News.query.join(Follow, Follow.followed_id==News.user_id).filter(Follow.follower_id==current_user.id)
        paginate = query.order_by(News.id.desc()).paginate(page=page, per_page=5, error_out=False)

    #用到的表   users follows news
    #1.current_user.id == follows.follower.id
    #2.news.user_id == follows.followed.id


    #return render_template('main/all_news.html', ans=ans)
    #分页对象中有什么？
    #1.表示上一页页码的prev_num
    #2.表示下一页页码的next_num
    #3.表示上一页的分页对象的prev
    #4.表示下一页的分页对象的next
    #5.表示是否有上一页的has_prev
    #6.表示是否有下一页的has_next
    #7.表示总共的页数的pages
    #8.表示总共的元素数量的total_num
    #9.用来设置分页数字样式的iter_pages
    #10.用来表示当前分页的所有元素的items

    return render_template('main/all_news.html', paginate=paginate)

@main.route('/edit_user', methods=['GET', 'POST'])
@login_required
def edit_user() :
    form = EditUserForm()
    if form.validate_on_submit() :
        current_user.name = form.name.data
        current_user.about_me = form.about_me.data
        current_user.location = form.location.data
        if len(form.password.data) != 0 :
            current_user.password = form.password.data
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('.user_info', id=current_user.id))

    form.email.data = current_user.email
    form.name.data = current_user.name
    # form.password.data = '*******'
    # form.password_again.data = '*******'
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('main/edit_user.html', form=form)

@main.route('/user_info')
@login_required
def user_info() :
    id = request.args.get('id')
    if id is None :
        abort(404)
    user = User.query.filter_by(id=id).first()
    if user is None :
        abort(404)
    return render_template('main/user_info.html', user=user)

@main.route('/')
def index() :
    #render_template会去app/templates下找模板
    return render_template('main/index.html')

@main.route('/favicon.ico')
def favicon() :
    return 'ok'

