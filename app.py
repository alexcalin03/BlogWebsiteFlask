from flask import Flask, render_template
from models import db, User, Post, Comment

app = Flask(__name__)
app.config.from_object('config.Config')


db.init_app(app)


@app.route('/')
def display_content():
    return render_template('base.html')

@app.route('/users/profile/<int:user_id>')
def display_user_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    return render_template('user_profile.html', user=user)

@app.route('/users')
def display_all_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/posts')
def display_all_posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)

@app.route('/posts/<int:post_id>')
def display_post(post_id):
    found_post = Post.query.filter_by(id=post_id).first()
    found_post.reads += 1
    db.session.commit()
    return render_template('post.html', post=found_post)

if __name__ == '__main__':
    app.run(debug=True)
