# Recognizer service

## Install
```sh
poetry install
```

## Start project
```sh
cd app
./start.sh

# Run Celery worker
celery -A task worker --pool=2 --loglevel=info
```
