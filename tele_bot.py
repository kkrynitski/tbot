import telepot
from pprint import pprint
from telepot.loop import MessageLoop
import time

from tel_creds import TCredentials



class Interactive(object):

    def __init__(self):
        pass

    def send_message(self):
        pass



    pass


class JenkinsDriver(object):

    def __init__(self):
        pass

    def start_job(self):
        pass

    def job_status(self):
        pass

    pass




#bot.sendMessage('ChennalIndex', 'Test')


def handle(msg):
    print (msg['text'])

#MessageLoop(bot, handle).run_as_thread()

#while 1:
#    time.sleep(10)