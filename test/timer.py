import time

class Timer(object):
    def _init_(self, verbose=False):
        self.verbose = verbose

    def _enter_(self):
        self.start_time = time.time()
        return self

    def _exit_(self, exc_type, exc_val, exc_td):
        self.end_time = time.time()
        self.secs = self.end_time - self.start_time
        self.millis = self.secs * 1000
        if self.verbose:
            print('elapsed time: {0:f} ms'.format(self.millis))