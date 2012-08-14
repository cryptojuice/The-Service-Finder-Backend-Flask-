import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = '0.0.0.0:18000'
proc_name = 'tsf_gunicorn'
pidfile = '/tmp/tsf_gunicorn.pid'
logfile = '/tmp/tsf_gunicorn.log'
worker_class = 'gevent'
debug = True
daemon = True
