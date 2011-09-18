from dexy.dexy_filter import DexyFilter

class SillyHandler(DexyFilter):
    ALIASES =['com.example.silly']

    def process_text(self, input_text):
        return "you said: '%s'\n that's SOOOO silly!\n" % input_text
