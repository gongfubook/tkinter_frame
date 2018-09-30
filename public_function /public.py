import time 


def log(*args, **kwargs):
    ''' log运行记录 '''
    localtime = time.asctime(time.localtime(time.time()))
    print('log:', localtime, '\n', *args, **kwargs)
