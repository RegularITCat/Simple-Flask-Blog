from app import app, db
import view
from posts.blueprint import posts
from flask_wtf.csrf import CSRFProtect

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()
    csrf = CSRFProtect(app)
    csrf.init_app(app)
