from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.views.views import profiles_router
import os

DB_USERNAME = os.environ.get('DB_USERNAME','admin')
DB_PASSWORD = os.environ.get('DB_PASSWORD','12345')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
DB_PORT = os.environ.get('DB_PORT','5432')
DB_NAME = os.environ.get('DB_NAME','main')

TORTOISE_ORM = {
    'connections': {'default': f'postgres://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'},
    'apps': {
        'models': {
            'models': ['app.models.orm_models','aerich.models'],
            'default_connection': 'default',
        },
    },
}

def create_fast_api_app() -> FastAPI:
    app = FastAPI(title='Platzi Fast API Class')

    register_tortoise(
        app,
        db_url=TORTOISE_ORM['connections']['default'],
        modules={'models': TORTOISE_ORM['apps']['models']['models'][:-1]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

    app.include_router(profiles_router, prefix='/p',tags=['Profiles'])

    return app