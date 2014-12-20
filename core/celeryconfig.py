BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# In Debug Mode this value be setting true 
CELERY_ALWAYS_EAGER = True


#celery setting
from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'query_transactions': {
        'task': 'django_bitcoin.tasks.query_transactions',
        'schedule': timedelta(seconds=10),
    },
    'sync_alladdress_balance': {
        'task': 'django_bitcoin.tasks.sync_alladdress_balance',
        'schedule': timedelta(seconds=10),
    },                       
}