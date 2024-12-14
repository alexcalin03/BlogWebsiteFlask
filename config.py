import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
    DEBUG = True
