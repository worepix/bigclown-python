import threading


class Thread:
    def __init__(self):
        pass

    def add(self, group):
        def inner(func):
            threading.Thread(target=func, name="{0}: {1}".format(
                             group, threading.active_count())).start()
            return func
        return inner

    def synchronize(self, variable):
        def inner(func):
            lock = threading.RLock()
            lock.acquire()
            s_variable = variable
            lock.release()
            return func(s_variable)
        return inner

    def running_list(self):
        return threading.enumerate()

    def running_count(self):
        return threading.active_count()
