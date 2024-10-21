class IOStream():
    """
    Logging to screen and file
    """
    def __init__(self):
        self.f = open('run.log', 'w')
        

    def cprint(self, text):
        to_print = text
        self.f.write(to_print + "\n")
        self.f.flush()

    def close(self):
        self.f.close()
