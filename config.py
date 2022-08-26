import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get(
        'BLOB_ACCOUNT') or 'udacitynanostorage'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or 'e5NTwY2KdDANfinS0bHfZjw+A0IqPvqTj5ftuEMiyoBkV5kgveJyQ/i9YBfEUJfeXYzOh2dM2rBX+AStsb/NYw=='
    BLOB_CONTAINER = os.environ.get(
        'BLOB_CONTAINER') or 'images'
    SQL_SERVER = os.environ.get(
        'SQL_SER') or 'udacity-nano-degree-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacitynanodegree-db'
    SQL_USER_NAME = os.environ.get(
        'SQL_USER_NAME') or 'adminudacity'
    SQL_PASSWORD = os.environ.get(
        'SQL_PASSWORD') or 'P@ssword1'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

        ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "u9m8Q~PbUvpv3LMPBS8M04.marxrURCnHRa_KaHh"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/common"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "dad03134-e222-4cfc-b1ce-4baf3b83e556"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/auth-token"

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session