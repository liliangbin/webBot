from app.speech import Speech
from . import main
from .. import db
from ..models import User
from flask import render_template, request
import time
from ..models import PoseToLocation


@main.route('/')
def index():
    return render_template('index.html', name='index')


@main.route('/query')
def query():
    user = User()
    user.username = 'user_name_test' + str(time.time())
    db.session.add(user)
    db.session.commit()
    print 'commit '
    return render_template('web_wideo.html')


@main.route('/asr')
def asr():
    audio = request.args.get('audio')
    print audio
    if audio is None:
        return render_template('asr.html')
    else:
        speech = Speech()
        result = speech.asr(audio)
        print result  # we will know the message in the pcm file
        pose_to_location = PoseToLocation.query.filter_by(location=result).first()
        print pose_to_location.linear_x + 'LOCATION '

        # TODO // we will send a move_base_simple/goal topic with a pose message and then navigation the robot

        return render_template('asr.html')
