class Config:
    """Set Flask configuration vars from .env file."""

    # General
    # Database
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://web_api:web_api@localhost:3306/students_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = "false"
