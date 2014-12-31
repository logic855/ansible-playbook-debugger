

class TaskInfo(object):
    """ Class to describe a target task """
    def __init__(self, module_name, module_args, vars, complex_args, **kwargs):
        self.module_name = module_name
        self.module_args = module_args
        self.vars = vars
        self.complex_args = complex_args
        for key, value in kwargs.items():
            setattr(self, key, value)


class ErrorInfo(object):
    """ Class to describe the error on a task execution. """
    def __init__(self, failed=False, reason='', result='', error=None):
        self.failed = failed
        self.reason = reason
        self.result = result
        self.error = error


class NextAction(object):
    """ The next action after an interpreter's exit. """
    REDO = 1
    CONTINUE = 2
    EXIT = 3

    def __init__(self, result=EXIT):
        self.result = result

    def set(self, result):
        self.result = result
