LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'error': {
            'format': 'TIME: {asctime} | LEVEL: {levelname} | PATH: {pathname} || STACK {exs_info} || MESSAGE: '
                      '{message}',
            'style': '{',
        },
    },
    'handlers': {
        'news': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'error',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'news': {
            'handlers': ['news'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['news'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
