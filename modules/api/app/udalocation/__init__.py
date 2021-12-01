from app.udalocation.models import Location# noqa
from app.udalocation.schemas import LocationSchema # noqa


def register_routes(api, app, root="api"):
    from app.udalocation.controllers import api as udalocation_api

    api.add_namespace(udalocation_api, path=f"/{root}")
