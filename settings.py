from envparse import Env

env = Env()

REAL_DB_URL = env.str(
    'DB_URL',
    default='postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres'
)
