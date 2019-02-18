import aiohttp
from aiohttp_jinja2 import template
from sqlalchemy import select
from .. import db

@template("index.html")
async def index(request):
	pass

async def users(request):
	async with request.app['db'].acquire() as conn:
		query = select([db.users.c.id, db.users.c.login]).where(db.users.c.status)
		result = await conn.fetch(query)
		str_res = []
		for row in result:
			str_res.append("id: {0} \t login: {1}".format(row[0], row[1]))

	sep = "\n"
	return aiohttp.web.Response(body = sep.join(str_res))

async def by_id(request):
	user_id = int(request.rel_url.query['id'])
	async with request.app['db'].acquire() as conn:
		query = select([db.users.c.login, db.users.c.status]).where(db.users.c.id == user_id)
		result = await conn.fetch(query)
		if result and result[0][1]:
			str_res="id: {0} \t login: {1}".format(user_id, result[0][0])
		else:
			str_res="No match found"

	return aiohttp.web.Response(body = str_res)

async def by_login(request):
	user_login = request.rel_url.query['login']
	async with request.app['db'].acquire() as conn:
		query = select([db.users.c.id, db.users.c.status]).where(db.users.c.login == user_login)
		result = await conn.fetch(query)
		if result and result[0][1]:
			str_res="id: {0} \t login: {1}".format(result[0][0], user_login)
		else:
			str_res="No match found"

	return aiohttp.web.Response(body = str_res)