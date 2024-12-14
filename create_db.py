from datetime import datetime, timedelta
from app import app, db, User, Post, Comment

with app.app_context():

    db.create_all()

    # Add users
    users = [
        User(username="Michael", email="michael@gmail.com", age=30),
        User(username="Alex", email="alex@yahoo.com", age=28),
        User(username="Andrew", email="andrew@icloud.com", age=26),
        User(username="David", email="david@hotmail.com", age=24),
        User(username="Tyler", email="tyler@e-uvt.com", age=22)
    ]
    db.session.add_all(users)
    db.session.commit()


    michael, alex, andrew, david, tyler = User.query.all()

    # Add posts
    posts = [
        Post(user_id=michael.id, posted=datetime.utcnow() - timedelta(days=1), title="Michael's Travel Blog",
             body="I recently visited Paris and it was amazing!"),
        Post(user_id=michael.id, posted=datetime.utcnow() - timedelta(days=2), title="Why I Love Coding",
             body="Programming has changed my life for the better."),
        Post(user_id=michael.id, posted=datetime.utcnow() - timedelta(days=3), title="A Day in My Life",
             body="Sharing my daily routine for those interested."),

        Post(user_id=alex.id, posted=datetime.utcnow() - timedelta(days=1), title="Favorite Recipes",
             body="Here are my top 5 favorite recipes of all time."),
        Post(user_id=alex.id, posted=datetime.utcnow() - timedelta(days=2), title="Yoga for Beginners",
             body="Yoga has been a game-changer for me. Here's how you can start."),
        Post(user_id=alex.id, posted=datetime.utcnow() - timedelta(days=3), title="Book Recommendations",
             body="Sharing my must-read books for this year."),

        Post(user_id=andrew.id, posted=datetime.utcnow() - timedelta(days=1), title="The Joy of Photography",
             body="Capturing moments is something I live for."),
        Post(user_id=andrew.id, posted=datetime.utcnow() - timedelta(days=2), title="Fitness Tips",
             body="My tips for staying fit and healthy."),
        Post(user_id=andrew.id, posted=datetime.utcnow() - timedelta(days=3), title="Best Gadgets of 2024",
             body="My favorite tech gadgets this year."),

        Post(user_id=david.id, posted=datetime.utcnow() - timedelta(days=1), title="Why I Love Cycling",
             body="Cycling is more than just a hobby; it’s a passion."),
        Post(user_id=david.id, posted=datetime.utcnow() - timedelta(days=2), title="Top Movies of the Decade",
             body="These movies have left a mark on me."),
        Post(user_id=david.id, posted=datetime.utcnow() - timedelta(days=3), title="How to Stay Motivated",
             body="Sharing my methods for keeping motivation alive."),

        Post(user_id=tyler.id, posted=datetime.utcnow() - timedelta(days=1), title="Learning Guitar",
             body="My journey of learning to play the guitar."),
        Post(user_id=tyler.id, posted=datetime.utcnow() - timedelta(days=2), title="Traveling on a Budget",
             body="How I managed to travel without breaking the bank."),
        Post(user_id=tyler.id, posted=datetime.utcnow() - timedelta(days=3), title="Starting a Podcast",
             body="Why I decided to start a podcast and how I did it.")
    ]
    db.session.add_all(posts)
    db.session.commit()


    posts = Post.query.all()

    # Add comments
    comments = [
        Comment(user_id=alex.id, post_id=posts[0].id, body="Paris is beautiful! Thanks for sharing."),
        Comment(user_id=andrew.id, post_id=posts[1].id, body="Coding changed my life too!"),
        Comment(user_id=david.id, post_id=posts[2].id, body="Loved reading about your daily routine."),
        Comment(user_id=tyler.id, post_id=posts[0].id, body="I've always wanted to visit Paris. Great post!"),

        Comment(user_id=michael.id, post_id=posts[3].id, body="Those recipes look delicious!"),
        Comment(user_id=andrew.id, post_id=posts[4].id, body="Yoga has really helped me stay calm."),
        Comment(user_id=david.id, post_id=posts[5].id, body="Thanks for the book recommendations!"),
        Comment(user_id=tyler.id, post_id=posts[3].id, body="Can't wait to try these recipes."),

        Comment(user_id=michael.id, post_id=posts[6].id, body="Photography is so inspiring!"),
        Comment(user_id=alex.id, post_id=posts[7].id, body="Fitness tips are always helpful. Thanks!"),
        Comment(user_id=david.id, post_id=posts[8].id, body="Those gadgets sound amazing."),
        Comment(user_id=tyler.id, post_id=posts[6].id, body="I love taking photos too!"),

        Comment(user_id=michael.id, post_id=posts[9].id, body="Cycling is such a great activity."),
        Comment(user_id=alex.id, post_id=posts[10].id, body="I’ve seen some of these movies. Great list!"),
        Comment(user_id=andrew.id, post_id=posts[11].id, body="Motivation tips are always welcome!"),
        Comment(user_id=tyler.id, post_id=posts[9].id, body="I’ve recently taken up cycling as well."),

        Comment(user_id=michael.id, post_id=posts[12].id, body="Learning guitar must be so fun!"),
        Comment(user_id=alex.id, post_id=posts[13].id, body="Traveling on a budget is always tricky."),
        Comment(user_id=andrew.id, post_id=posts[14].id, body="Starting a podcast sounds exciting!"),
        Comment(user_id=david.id, post_id=posts[12].id, body="I’ve been wanting to learn guitar too!")
    ]
    db.session.add_all(comments)
    db.session.commit()

    print("Database populated with unique posts and comments.")
