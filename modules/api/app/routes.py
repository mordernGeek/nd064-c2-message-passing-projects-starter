def register_routes(api, app, root="api"):
    from app.udaconnect import register_routes as attach_udaconnect
	from app.udapersons import register_routes as attach_udapersons
	from app.udalocation import register_routes as attach_uda_location

    # Add routes
    attach_udaconnect(api, app)
	attach_udalocation(api, app)
	attach_udapersons(api, app_
