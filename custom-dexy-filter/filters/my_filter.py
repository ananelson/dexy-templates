from dexy.handler import DexyHandler

class SillyHandler(DexyHandler):
    ALIASES =['com.example.silly']

    def process_text(self, input_text):
        return "you said: '%s'\n that's SOOOO silly!\n" % input_text
