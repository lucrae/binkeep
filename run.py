import os
from project import app

def check_environment_variables():
    if os.environ.get('SECRET_KEY') == None:
        print("Warning: SECRET_KEY not set as environment variable")
    if os.environ.get('MYSQL_ROOT_PASSWORD') == None:
        print("Warning: MYSQL_ROOT_PASSWORD not set as environment variable")

if __name__ == '__main__':
    check_environment_variables()
    app.run()