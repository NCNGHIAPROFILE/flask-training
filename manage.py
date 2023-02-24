import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint

# Link: https://thaitpham.com/huong-dan-lap-trinh-flask-phan-4-su-dung-co-so-du-lieu/
# link: https://viblo.asia/p/xay-dung-ung-dung-web-crud-voi-python-va-flask-phan-mot-naQZRyydKvx
# Link: https://flask-restplus.readthedocs.io/en/stable/api.html
# Link: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
# Link: https://thaitpham.com/huong-dan-lap-trinh-flask
# Link: https://www.youtube.com/watch?v=yh-28ksEXwY&t=3s

from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
# chuyển các thể hiện dbvà MigrateCommandtới add_commandgiao diện của managerđể hiển thị tất cả các lệnh di chuyển
# cơ sở dữ liệu thông qua Flask-Script.

@manager.command

def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()