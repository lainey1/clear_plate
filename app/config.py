import os

# Create Configuration class
class Configuration:

    SECRET_KEY = os.environ.get("SECRET_KEY")
    '''
        - for session management and cryptographic operations.
        - loaded from the environment variable "SECRET_KEY" for security purposes
        - used for signing cookies and other security features.
        - ! REMEMBER: set variable in .env
    '''

    # SQLAlchemy Database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

     # Disable track modifications to save memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
