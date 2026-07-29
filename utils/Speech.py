import threading
import pyttsx3
from typing import Optional

class Speech():

    engine: Optional[pyttsx3.engine.Engine] = None
    t = None
    

    @staticmethod
    def say(text, end_listner = None):
        ''' Say something using the system text to speech, use end listener function to call a function or a lambda at the end of speech. '''
        if Speech.engine == None:
            Speech.engine = pyttsx3.init()
            Speech.engine.setProperty("rate", 140)
            Speech.engine.setProperty("volume", 140)
        Speech.t = threading.Thread(target = lambda: Speech.sayOnThread(text, end_listner), daemon=True)
        Speech.t.start()

    @staticmethod
    def isBusy():
        assert Speech.engine is not None
        return Speech.engine.isBusy()

    @staticmethod
    def sayOnThread(text, end_listener = None):
        if Speech.engine:
            Speech.engine.say(text)
            Speech.engine.runAndWait()
            Speech.engine.stop()
            if end_listener:
                end_listener()
