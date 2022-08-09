from fastapi import FastAPI
from custom_logging import CustomizeLogger
from pathlib import Path
from fastapi import Request
import uvicorn
import logging
import os
# from elasticapm.contrib.starlette import make_apm_client, ElasticAPM

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")

def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger

    return app


# apm = make_apm_client({
#     # Set required service name. Allowed characters:
#     # a-z, A-Z, 0-9, -, _, and space
#     'SERVICE_NAME': 'PYTHON_FLASK_TEST_APP',
#
#     # Set custom APM Server URL (default: http://localhost:8200)
#     'SERVER_URL': 'http://apm-server:8200',
#
#     'DEBUG': True,
# })
app = create_app()
# app.add_middleware(ElasticAPM, client=apm)


@app.get('/custom-logger')
def customize_logger(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    a = 1 / 0
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}


@app.get('/info')
def log_info(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    return {'data': "Successfully Implemented Custom Log"}


@app.get('/error')
def log_error(request: Request):
    request.app.logger.error("Here Is Your Error Log")
    return {'data': "Successfully Implemented Custom Log"}


@app.get('/exception')
def customize_logger(request: Request):
    request.app.logger.info("Here Is Your Info Log")
    try:
        a = 1 / 0
    except Exception as e:
        request.app.logger.exception("Here Is Your Exception Log")
    return {'data': "Successfully Implemented Custom Log"}


import os

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=int(os.environ['WEBAPP_PORT']),
                access_log=True)
