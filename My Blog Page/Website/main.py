from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'development-only-not-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.webp', '.gif']
app.config['UPLOAD_DIRECTORY'] = 'static/uploads/'
app.config['UI_DIRECTORY'] = 'static/ui/'
