from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]'
    s = re.sub(pattern, '-', s)
    return s.lower()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128), nullable=False, unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.Date, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)
