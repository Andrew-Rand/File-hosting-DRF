from decouple import config


timezone = 'UTC'
task_track_started = True
task_time_limit = 30 * 60
broker_url = config('CELERY_BROKER_HOST') + config('CELERY_BROKER_PORT')
