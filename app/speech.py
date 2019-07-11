# -*- coding: utf-8 -*-

from aip import AipSpeech

# 语音识别模块。。
# baidu app use my tel to login
class Speech(object):
    def __init__(self):
        self.APP_ID = '16250780'
        self.APP_KEY = 'xcnrNwkhe61iYGoaZVRNpnma'
        self.SECRET_KEY = 'rjHGH6zwDmGcx2lGisXYGilE2bnol7e9'
        self.client = AipSpeech(self.APP_ID, self.APP_KEY, self.SECRET_KEY)

    def get_file_content(self, filePath='audio.pcm'):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def asr(self, filepath):
        back = self.client.asr(self.get_file_content(filepath), 'pcm', 16000, {
            'dev_pid': 1536,
        })
        print back
        return back.get('result')[0].encode('utf-8')

