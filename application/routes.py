from .views import frontend

def setup_routes(app):
	app.router.add_route('GET', '/', frontend.index)
	app.router.add_route('GET', '/users', frontend.users)
	app.router.add_route('GET', '/by-id', frontend.by_id)
	app.router.add_route('GET', '/by-login', frontend.by_login)