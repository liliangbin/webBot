# -*- coding: utf-8 -*-

from flask import request, render_template, redirect, url_for

from config import Config
from . import main


@main.route('/upload/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        audio = request.files.get('audio')
        # TODO // 对图像的后缀以及名字的合法性进行鉴定
        avter = request.form.get('desc')
        print avter
        print audio.filename
        audio.save(Config.UPLOAD_PATH + audio.filename)

        return redirect(url_for('.asr', audio=Config.UPLOAD_PATH + audio.filename))
