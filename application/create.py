from aiohttp import web
import jinja2
import aiohttp_jinja2
import asyncpgsa
from .routes import setup_routes
from .settings import config


async def create_app():
	app = web.Application()
	app['config'] = config
	aiohttp_jinja2.setup(app, loader = jinja2.PackageLoader('application', 'views'))
	setup_routes(app)
	app.on_startup.append(on_start)
	app.on_cleanup.append(on_shutdown)
	return app

async def on_start(app):
	config = app['config']
	app['db'] = await asyncpgsa.create_pool(dsn = config['db_url'])

async def on_shutdown(app):
	await app['db'].close()