import multiprocessing
import os

workers = multiprocessing.cpu_count() * 2
workers = 1  # dev mode

if os.environ.get('TRAVIS') == 'true':
    workers = 2

bind = ('0.0.0.0:8000', )
keepalive = 15
pidfile = '/run/lock/api-hour-demo.pid'
backlog = 10240000
