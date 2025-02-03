class Config:
    SECRET_KEY = 'nando'  # Cambia esto
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False