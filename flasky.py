# -*- coding: utf-8 -*-

import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, PoseToLocation


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# migrate 的新建 我们需要扫描到这些文件我们才能创建
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, PoseToLocation=PoseToLocation)


# 单元测试
@app.cli.command()
def test():
    """ run the unit tests """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
