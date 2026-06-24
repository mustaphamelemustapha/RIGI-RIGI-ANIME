import multiprocessing
import os

# Binding details
bind = "0.0.0.0:8000"

# Gunicorn process manager configurations
workers = (2 * multiprocessing.cpu_count()) + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Timeout parameters for downloading streams
keepalive = 120
timeout = 120

# Logging parameters
loglevel = os.getenv("LOG_LEVEL", "info")
accesslog = "-"
errorlog = "-"
