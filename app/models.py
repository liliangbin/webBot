from app import db


class Role(db.Model):
    _tablename_ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r >' % self.name


class User(db.Model):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '< user %r>' % self.username


class PoseToLocation(db.Model):
    _tablename_ = 'pose_to_location'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(64), unique=True, index=True)
    position_x = db.Column(db.String(64), nullable=False)
    position_y = db.Column(db.String(64), nullable=False)
    position_z = db.Column(db.String(64), nullable=False)
    orientation_x = db.Column(db.String(64), nullable=False)
    orientation_y = db.Column(db.String(64), nullable=False)
    orientation_z = db.Column(db.String(64), nullable=False)
    orientation_w = db.Column(db.String(64), nullable=False)
